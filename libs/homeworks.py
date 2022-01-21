import repackage

repackage.up()

import json
import html
import requests as req
import base64
from datetime import datetime, timedelta
from libs.utils import getToken, getProxy


def getHomeworks():
    with open("config.json", "r") as f:
        secrets = json.load(f)

    assert "ecLogin" in secrets
    assert "ecPassword" in secrets

    LOGIN = secrets["ecLogin"]
    PASSWORD = secrets["ecPassword"]

    PROXY = getProxy()

    token, studentId = getToken(LOGIN, PASSWORD, PROXY)

    BASE_URL = "https://api.ecoledirecte.com"
    TOMORROW_DATE = (datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d")
    HOMEWORK_PATH = f"/v3/Eleves/{studentId}/cahierdetexte/2022-01-20.awp?verbe=get&v=1.11.0"
    QUERY_URL = BASE_URL + HOMEWORK_PATH

    homework_payload = {"data": "{}"}
    homework_headers = {"x-token": token}

    homework_req = req.post(QUERY_URL, data=homework_payload, headers=homework_headers, proxies=PROXY)

    response_subjects = homework_req.json()["data"]["matieres"]

    subjects = {}
    for subject in response_subjects:
        if not "aFaire" in subject:
            continue
        if not "contenu" in subject["aFaire"]:
            continue

        documents = []
        if "documents" in subject["aFaire"] and subject["aFaire"]["documents"]:
            for document in subject["aFaire"]["documents"]:
                documents.append(document["libelle"])

        subjects[subject["matiere"]] = {
            "teacher": subject["nomProf"].strip(),
            "content": html.unescape(base64.b64decode(subject["aFaire"]["contenu"]).decode("utf-8"))
            .replace("<p>", "")
            .replace("</p>", "")
            .replace("\n\n", "\n"),
            "interrogation": subject["interrogation"],
            "documents": documents,
        }

    homeworks = {"date": TOMORROW_DATE, "subjects": subjects}

    return homeworks
