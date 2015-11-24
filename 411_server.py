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
    if request.method == "POST":
        print (request.headers)
        price_paid = json.loads(request.headers.get("Bitcoin-Transfer"))['amount']
        print ("Paid: %s" %price_paid)
        request.headers.get("")
        if request.json and "address" in request.json:
            ret_json = {
                "address": request.json["address"],
                "price": price_paid,
                "time": time.time()
            }
            address = request.json["address"]

            ret_json['result'] = get_scorechain(address)

            print (json.dumps(ret_json))
            return json.dumps(ret_json), 201
        else:
            print ("Invalid request")
            return "Invalid request", 400



def draw_me():


    #PRINT ASCII HERE

    return None

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
    ret_json = {"ascii":draw_me(), "data":json.dumps(info_obj)}

    return json.dumps(ret_json)


if __name__ == '__main__':
    print ("411 running... ")
    app.run(host='0.0.0.0', port=21411, debug=True)
