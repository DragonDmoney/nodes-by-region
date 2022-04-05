from models import *
for country in Country.select():

    regions = Region.select().where(Region.country==country)

    nodes = []

    for region in regions:
        _ = Node.select().where(Node.region == region)
        for node in _:
            nodes.append(node)
    # print(US_regions)


    with open("countries/"+country.name+"-nodes.txt", "w") as out:
        for node in nodes:
            out.write(node.address+", \n")
