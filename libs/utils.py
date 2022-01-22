import requests as req
from fp.fp import FreeProxy


def getProxy():
    """
    Returns the first available proxy on FreeProxy

    Returns:
        [string]: http address of a proxy
    """
    proxy = FreeProxy().get()

    return {"http": proxy}


def getInfos(LOGIN, PASSWORD, PROXY):
    """
    Returns the login token and student id from Ecole directe

    Parameters:
        [string]: your Ecole directe login
        [string]: your Ecole directe password
        [string]: http adress of a proxy

    Returns:
        [string]: login token
        [string]: student id
    """
    LOGIN_URL = "https://api.ecoledirecte.com/v3/login.awp"

    login_payload = {
        "data": '{"identifiant": "%s", "motdepasse": "%s", "uuid": "", "isReLogin": false}' % (LOGIN, PASSWORD)
    }

    login_req = req.post(LOGIN_URL, data=login_payload, proxies=PROXY)

    token = login_req.json()["token"]
    id = login_req.json()["data"]["accounts"][0]["id"]

    return token, id
