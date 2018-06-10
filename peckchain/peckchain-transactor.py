import requests
import pprint
import json
import random
import time

for i in range(0, 25):

    peck_trx = {
        "item": "WPL90/09",
        "bin": "A01A03",
        "sequence": "{}{}".format('A', i)
    }

    peck_trx_string = json.dumps(peck_trx)

    pprint.pprint(peck_trx)

    headers = {"Content-type": "application/json"}
    url = ""

    randomnumber = random.random()

    if randomnumber < 0.25:
        url = "http://localhost:5001"
    elif randomnumber < 0.50:
        url = "http://localhost:5002"
    elif randomnumber < 0.75:
        url = "http://localhost:5003"
    else:
        url = "http://localhost:5004"

    urlstring = "{}/txion".format(url)

    print("{}. Attempting transaction to {}...".format(i, urlstring))

    r = requests.post(urlstring, headers=headers, data=peck_trx_string)

    print("Results: {}".format(r.status_code))
    # pprint.pprint(r.json())

    urlstring = "{}/mine".format(url)
    print("Mining it...")
    r = requests.get(urlstring, headers=headers)

    print("Results: {}".format(r.status_code))
    #pprint.pprint(r.json())

    time.sleep(1)

    for url in ["http://localhost:5001", "http://localhost:5002", "http://localhost:5003", "http://localhost:5004"]:
        requests.get("{}/check".format(url))


