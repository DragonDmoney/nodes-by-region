from models import *
for region in Region.select():

    nodes = []

    for node in Node.select().where(Node.region==region):
        nodes.append(node)
    # print(US_regions)


    with open("regions/"+region.name+"-nodes.txt", "w") as out:
        for node in nodes:
            out.write(node.address+", \n")
