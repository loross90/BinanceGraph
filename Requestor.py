import requests
import json
from igraph import *

objects = json.loads(requests.get("https://api3.binance.com/api/v3/exchangeInfo").text)

interested = [item for item in objects['symbols'] if item['status'] == 'TRADING']

qAssets = list(map(lambda x: x.get('quoteAsset'), interested))
bAssets = list(map(lambda x: x.get('baseAsset'), interested))

uniqueSym = list(set(qAssets + bAssets))

uniqueSymDictForGraph = dict(zip(uniqueSym, list(range(len(uniqueSym)))))


g = Graph()

g.add_vertices(len(uniqueSymDictForGraph))
g.vs["name"] = list(uniqueSymDictForGraph.keys())

#g.add_edge(uniqueSymDictForGraph[interested[5]['baseAsset']],uniqueSymDictForGraph[interested[5]['quoteAsset']])

for i in interested:
    g.add_edge(uniqueSymDictForGraph[i['baseAsset']],uniqueSymDictForGraph[i['quoteAsset']])

path=g.get_shortest_paths("CREAM",to="USDT",mode=OUT,output='vpath')

for n in path[0]:
    print("{}".format(g.vs[n]['name']))

#print(objects['symbols'][2]['quoteAsset'])


#print(ans.content)