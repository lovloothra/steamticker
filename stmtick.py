#Steam Ticker - Lov Loothra

import stlib as SQ
import os
from ctypes import *

def printall(results):
    os.system("cls")
    windll.Kernel32.GetStdHandle.restype = c_ulong
    h = windll.Kernel32.GetStdHandle(c_ulong(0xfffffff5))
    for x in range(len(results)):
        if delta[x] > 0.0:
            windll.Kernel32.SetConsoleTextAttribute(h, 10)
        elif delta[x] < 0.0:
            windll.Kernel32.SetConsoleTextAttribute(h, 12)
        else:
            windll.Kernel32.SetConsoleTextAttribute(h, 15)
        print results[x]
    windll.Kernel32.SetConsoleTextAttribute(h, 15)
    print "\nTicks:", int(i)
    
inputs = open("queries.txt", "r")
queries = inputs.read().split("\n")
inputs.close()

maxlen = len(max(queries, key = len)) + 3
meanprice = [0.0 for i in range(len(queries))]
delta = [0.0 for i in range(len(queries))]

i = 1.0
while True:
    results = []
    for x in range(len(queries)):
        price = float(SQ.get_price(queries[x]))
        delta[x] = price - meanprice[x]
        sign = chr(30) if delta[x] >= 0.0 else chr(31)
        results.append("{:s}{:s}${:5.2f} {:s}{:4.2f}".format(queries[x], "."*(maxlen-len(queries[x])), price, sign, abs(delta[x])))
        meanprice[x] = round((meanprice[x] * (i - 1) + price)/i, 2)
    printall(results)
    i += 1
