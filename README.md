# How to run:

On a node with sufficient specs and rpc_timeout (in the config file)
````
>>> pocket query nodes --nodeLimit 100000 > nodes.json
````
copy that onto your local machine
````
>>> pip3 install -r requirements.txt

>>> python3 filter-nodes.py
````
this will take around 1 hr, and it will add all the nodes to the database with region and country
