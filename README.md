
Blockchain 411
============================

$$\   $$\         $$\           $$\
$$ |  $$ |      $$$$ |        $$$$ |
$$ |  $$ |      \_$$ |        \_$$ |
$$$$$$$$ |        $$ |          $$ |
\_____$$ |        $$ |          $$ |
      $$ |        $$ |          $$ |
      $$ |      $$$$$$\       $$$$$$\
      \__|      \______|      \______|



Blockchain Analytics
Lookup Bitcoin addresses based on their cluster and the clusters they've had transactions with

Running the server
------------------

	$ python3 411-server.py


Running the client
-------------------

	21 buy --maxprice 100 url http://10.151.47.208:21411/lookup?address=[BITCOIN_ADDRESS]

or for a nice command line interface:

	 wget https://goo.gl/JMBFev -O 411_client.py ; python3 411_client.py


API;

1. Get info
--------------

HTTP URI: /

Params: None

Result:


````
$$\   $$\         $$\           $$\
$$ |  $$ |      $$$$ |        $$$$ |
$$ |  $$ |      \_$$ |        \_$$ |
$$$$$$$$ |        $$ |          $$ |
\_____$$ |        $$ |          $$ |
      $$ |        $$ |          $$ |
      $$ |      $$$$$$\       $$$$$$\
      \__|      \______|      \______|


Name: Blockchain 411 	 Version: 104
Description: If I know, I would tell on you...
Endpoint: /lookup?address=[address] 	 Minimum Price: 100

Commandline usage: python3 ./411_client.py lookup [BITCOIN_ADDRESS]

Do you want to lookup a Bitcoin address? (Y/n)
````

Pricing:

	Free


2. Lookup and address
--------------

HTTP URI: /lookup?address=[address]

Params: bitcoin address

Result:

	{
	   "key": "1AAXXXXXXXXXXXXXXXXXXXXXXXXNSfRs",
	   "balance": {
	      "confirmed": 0,
	      "sent": 11.78123559,
	      "received": 11.78123559
	   },
	   "identity": {
	      "cluster": {
	         "name": "NucleusMarket",
	         "type": "darkweb",
	         "neighbours": 75301,
	         "id": "XJZNdo"
	      },
	      "web": {
	         "count": 0,
	         "detail": []
	      }
	   },
	   "count": {
	      "transactions": {
	         "total": 12,
	         "sent": 6,
	         "received": 6
	      }
	   },
	   "relationships": {
	      "rel_clusters_in": [
	         {
	            "name": "AgoraMarket",
	            "type": "darkweb",
	            "id": "x5BRmk",
	            "level": 1
	         }
	      ],
	      "tagged_addresses": []
	   }
	}

Pricing:

	100


TODO:
-----
* add more APIs
