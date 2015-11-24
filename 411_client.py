#!/usr/bin/python3

#
# Command line usage:
# $ python3 fortune-client.py		# Get pithy saying
# $ python3 fortune-client.py info	# Get server metadata
#

import json
import os
import sys

# import from the 21 Developer Library
from two1.commands.config import Config
from two1.lib.wallet import Wallet
from two1.lib.bitrequests import BitTransferRequests
import datetime
import tabulate

# set up bitrequest client for BitTransfer requests
wallet = Wallet()
username = Config().username
requests = BitTransferRequests(wallet, username)

# server address
server_url = 'http://localhost:21411/'


def look_it_up(address = None):
    if address is None:
        address = input("Please enter the Bitcoin address: ")
    #params = {'address':address}
    sel_url = server_url + 'lookup/?address=' + address
    answer = requests.get(url=sel_url.format())
    #print (answer.json().get("ascii"))
    #print ("Bang")
    print (answer)
    print (json.dumps(answer.json().get("data", None), indent=4, sort_keys=True))



def cmd_info():
    sel_url = server_url
    answer = requests.get(url=sel_url.format())
    print (answer.json().get("ascii"))
    print (json.dumps(json.loads(answer.text).get("data", None), indent=4, sort_keys=True))


if __name__ == '__main__':
    if len(sys.argv) >= 2 and sys.argv[1] == "lookup":
        if sys.argv[2]:
            address = sys.argv[2]
        else:
            address = None
        look_it_up(address)
    else:
        cmd_info()

