from typing import List
import json
import sys
import os

class Solution:
    def findCheapestPrice(n,flights,src,dst,k):
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            tmpPrices = prices.copy()

            for s, d, p in flights:  # s=source, d=dest, p=price
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices

        return -1 if prices[dst] == float("inf") else print (prices[dst])
    
if __name__ == '__main__':
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

    with open(os.path.join(__location__, 'data.json')) as f:
        data = json.load(f)
        f.close()

    for i in data:
        n = i['n']
        flights = i['flights']
        src = i['src']
        dst = i['dst']
        k = i['k']

    Solution.findCheapestPrice(n,flights,src,dst,k)
