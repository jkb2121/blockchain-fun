import requests
import pprint
import json
import random

peck_trx = {
    "item": "WPL90/09",
    "bin": "A01A03"
}

peck_trx_string = json.dumps(peck_trx)

pprint.pprint(peck_trx)

headers = {"Content-type": "application/json"}
url = ""

if random.random() < 0.5:
    url = "http://localhost:5005"
else:
    url = "http://localhost:5006"

urlstring = "{}/txion".format(url)

print("Attempting transaction to {}...".format(urlstring))

r = requests.post(urlstring, headers=headers, data=peck_trx_string)

print("Results: {}".format(r.status_code))
# pprint.pprint(r.json())

urlstring = "{}/mine".format(url)
print("Mining it...")
r = requests.get(urlstring, headers=headers)

print("Results: {}".format(r.status_code))
#pprint.pprint(r.json())


