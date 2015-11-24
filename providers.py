__author__ = 'sbeta'


import requests
import json


SCORECHAIN_TOKEN = ""




def get_scorechain(address):
    """
    get the json related to the address from scorechain
    """

    url = "https://www.scorechain.com/api_beta/address/%s?token=%s" %(address, SCORECHAIN_TOKEN)
    try:
        score_result = requests.get(url=url)
        ret_json = score_result.json()
        print (ret_json)
        return ret_json

    except Exception as err:
        print ("Scorechain failed for %s: %s" %(address, err))
        return None