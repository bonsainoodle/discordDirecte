import requests as req
from fp.fp import FreeProxy


def getProxy():
    proxy = FreeProxy().get()

    return {"http": proxy}


def getToken(LOGIN, PASSWORD, PROXY):
    LOGIN_URL = "https://api.ecoledirecte.com/v3/login.awp"

    login_payload = {
        "data": '{"identifiant": "%s", "motdepasse": "%s", "uuid": "", "isReLogin": false}' % (LOGIN, PASSWORD)
    }

    login_req = req.post(LOGIN_URL, data=login_payload, proxies=PROXY)

    token = login_req.json()["token"]
    id = login_req.json()["data"]["accounts"][0]["id"]

    return token, id
