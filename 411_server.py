import time
import json

from two1.lib.wallet import Wallet
from two1.lib.bitserv.flask import Payment

from flask import Flask
from flask import request

from providers import get_scorechain

app = Flask(__name__)

wallet = Wallet()
payment = Payment(app, wallet)


@app.route('/lookup', methods=["POST", "GET"])
@payment.required(100)
def lookup():
    price_paid = json.loads(request.headers.get("Bitcoin-Transfer"))['amount']
    print ("Paid: %s" %price_paid)
    print (request.__dict__)
    address = str(request.args.get('address'))
    if address:
        ret_json = {
            "address": address,
            "price": price_paid,
            "time": time.time()
        }

        ret_json['data'] = get_scorechain(address)
        print (json.dumps(ret_json))
        return json.dumps(ret_json), 200
    else:
        print ("Invalid request")
        return "Invalid request", 400



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


@app.route('/')
def get_info():
    info_obj = {
	"name": "Blockchain 411",
    "description":"If I know, I would tell on you...",
	"version": 101,
        "pricing": {
            "/lookup" : {
                "minimum" : 100
            },
        }

    }
    ret_json = {"data":json.dumps(info_obj)}

    return ret_json


if __name__ == '__main__':
    print ("411 running... ")
    app.run(host='0.0.0.0', port=21411, debug=True)
