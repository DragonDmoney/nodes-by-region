from models import *
import json

continents = json.loads(open("continents.json").read())

def get_country(continent, country):
    for country in Country.select().where(Country.name==country):
        regions = Region.select().where(Region.country==country)

        nodes = []

        for region in regions:
            _ = Node.select().where(Node.region == region)
            for node in _:
                nodes.append(node)
        # print(US_regions)


        with open("continents/"+continent+"-nodes.txt", "a") as out:
            for node in nodes:
                print(node.address+", \n")
                out.write(node.address+", \n")

for continent in continents.keys():
    for country in continents[continent]:
        get_country(continent, country)
