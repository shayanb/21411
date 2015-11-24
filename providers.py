__author__ = 'sbeta'


import requests
import json


SCORECHAIN_TOKEN = ""




def get_scorechain(address):
    """
    get the json related to the address from scorechain
    token: XB0zBhmY
    """

    url = "https://www.scorechain.com/api_beta/address/%s?token=%s" %(address, SCORECHAIN_TOKEN)
    try:
        score_result = requests.get(url=url)
        ret_json = json.loads(score_result.json())
        return ret_json

    except Exception:
        print ("Scorechain failed for %s" %(address))
        return None