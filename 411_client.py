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


def draw_me():


#     four11 = "____________/\\\_________/\\\______/\\\_         \n"\
# " __________/\\\\\_____/\\\\\\\__/\\\\\\\_        \n"\
# "  ________/\\\/\\\____\/////\\\_\/////\\\_       \n"\
# "   ______/\\\/\/\\\________\/\\\_____\/\\\_      \n"\
# "    ____/\\\/__\/\\\________\/\\\_____\/\\\_     \n"\
# "     __/\\\\\\\\\\\\\\\\_____\/\\\_____\/\\\_    \n"\
# "      _\///////////\\\//______\/\\\_____\/\\\_   \n"\
# "       ___________\/\\\________\/\\\_____\/\\\_  \n"\
# "        ___________\///_________\///______\///_ \n"

    four11 =    "$$\   $$\         $$\           $$\    \n"\
                "$$ |  $$ |      $$$$ |        $$$$ |   \n"\
                "$$ |  $$ |      \_$$ |        \_$$ |   \n"\
                "$$$$$$$$ |        $$ |          $$ |   \n"\
                "\_____$$ |        $$ |          $$ |   \n"\
                "      $$ |        $$ |          $$ |   \n"\
                "      $$ |      $$$$$$\       $$$$$$\  \n"\
                "      \__|      \______|      \______| \n"\
                "                                       \n"
    return four11



def look_it_up(address = None):
    if address is None:
        address = input("Please enter the Bitcoin address: ")
    sel_url = server_url + 'lookup?address=' + address
    answer = requests.get(url=sel_url.format())
    print (answer.json().get("ascii"))
    print ("=" * 30)
    print (json.dumps(answer.json().get("data", None), indent=4, sort_keys=True))



def cmd_info():
    sel_url = server_url
    answer = requests.get(url=sel_url.format())
    print (json.dumps(answer.json().get("data", None), indent=4, sort_keys=True))
    return answer.json().get("data, None")


if __name__ == '__main__':
    print (draw_me())
    if len(sys.argv) >= 2 and sys.argv[1] == "lookup":
        if sys.argv[2]:
            address = sys.argv[2]
        else:
            address = None
        look_it_up(address)
    else:
        info = cmd_info()
        print ("Name: %s \t Version: %s \n Description: %s \n\n Endpoint: /lookup?address=[address] \t Minimum Price: %s "
               % (info['name'],info['version'],info['description'],info['pricing']["/lookup"]["minimum"]))

        cont = input("Do you want to lookup a Bitcoin address? (Y/n) ")
        cont = cont or "y"
        if cont in ["y", "Y"]:
            look_it_up()



