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

#g.add_edge(uniqueSymDictForGraph[interested[5]['baseAsset']],uniqueSymDictForGraph[interested[5]['quoteAsset']])

for i in interested:
    g.add_edge(uniqueSymDictForGraph[i['baseAsset']],uniqueSymDictForGraph[i['quoteAsset']])

g.shorte
print(objects['symbols'][2]['quoteAsset'])

#print(ans.content)