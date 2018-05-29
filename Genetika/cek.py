import sys
import IPython
import numpy as np
import pprint as pp
import sklearn
import matplotlib.pyplot as plt
from IPython.display import display
import random
from copy import deepcopy
import math

maxtotal = 25
beratbrg = [2,3,6,3,5,9,4,7,8,2]
valu = [5,10,5,15,25,30,20,5,10,20]
populasi = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 0],
            [1, 0, 0, 1, 0, 0, 0, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 0, 0, 0, 1],
            [0, 1, 1, 0, 0, 1, 0, 0, 0, 1],
            [0, 1, 1, 0, 1, 1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 1, 0, 1, 0, 1]
            ]

def crossOver(cross,i1,i2):
    newdata = []
    for c in range(0,2):
        xcross = deepcopy(cross[c])
        for i in range(0,len(xcross)):
            if i>=i1 and i<=i2:
                if c!=1:
                    xcross[i] = cross[1][i]
                else:
                    xcross[i] = cross[0][i]
        newdata.append(xcross)
    return newdata


akhir = [[0, 0, 1, 1, 1, 1, 0, 0, 0, 1], [0, 1, 1, 0, 1, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 1, 0, 1, 0, 1],[0, 1, 1, 1, 0, 0, 1, 1, 0, 1], [0, 1, 0, 1, 0, 0, 1, 1, 0, 1], [1, 0, 0, 1, 1, 0, 0, 1, 0, 1]]
for i in range(0,len(akhir)):
    kromosom = akhir[i]
    berat = 0
    tpoin = 0
    hasilfitnes = 0
    for i in range(0, len(kromosom)):
        if kromosom[i]==1:
            berat = berat + beratbrg[i]
            tpoin = tpoin + valu[i]
    if berat>maxtotal:
        berat = 0
    finalberat = 50 - (maxtotal - berat)
    print("----")
    print(berat)
    print(tpoin)
    print(finalberat + tpoin)
