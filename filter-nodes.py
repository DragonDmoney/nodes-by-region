import json
from urllib.parse import urlparse
import requests
from tqdm import tqdm
from models import *
import sys

# node_page = int(sys.argv[1])

nodes = json.loads(open(f"nodes.json").read())["result"]

api_url = "https://pro.ip-api.com/json/"
key = "?key=9JDYKj2XUeOiVJg"

for node in tqdm(nodes):
    # print(urlparse(node["service_url"]).hostname)
    try:
        hostname = urlparse(node["service_url"]).hostname
        response = requests.get(api_url+hostname+key).json()

        if not Country.select().where(Country.name == response["country"]).exists():
            country = Country.create(name = response["country"], code = response["countryCode"])
        else:
            country = Country.select().where(Country.name == response["country"])[0]

        if not Region.select().where(Region.name == response["regionName"]).exists():
            region = Region.create(name = response["regionName"], code = response["region"], country=country)
        else:
            region = Region.select().where(Region.name == response["regionName"])[0]

        node = Node.create(url = node["service_url"], hostname = hostname, region=region, address=node["address"])
    except Exception as e:
        print("error: ",e)
