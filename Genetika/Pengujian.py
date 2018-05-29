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

import unittest


maxtotal = 25
beratbrg = [3,5,9,4,7,8]
valu = [15,25,30,20,5,10]
populasi = [[0, 1, 1, 1, 1, 0],
            [1, 1, 0, 0, 1, 0],
            [0, 0, 1, 1, 0, 1],
            [0, 1, 1, 1, 1, 1]
            ]

# fFitnes(populasi[0])
# fFitnes(populasi[1])
# fFitnes(populasi[2])
# fFitnes(populasi[3])
nilaifitnes = [130, 85, 106, 0]
class TesTerbaik(unittest.TestCase):
    def test_1terbaik(self):
        expected = [[0, 1, 1, 1, 1, 0]]
        self.assertEqual(cariterbaik(nilaifitnes, populasi,1), expected)
    def test_2terbaik(self):
        expected = [[0, 1, 1, 1, 1, 0], [0, 0, 1, 1, 0, 1]]
        self.assertEqual(cariterbaik(nilaifitnes, populasi,2), expected)

# indexcros = [[1, 3], [0, 2], [1, 2]]
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

# [populasi[0],populasi[1]]
# crossOver([populasi[2],populasi[3]],1,3)
def mutasi(populasi,awal,akhir):
    pophasil = []
    r = deepcopy(populasi)
    for idx in range(awal,akhir+1):
        if r[idx]==1:
            r[idx]=0
        else:
            r[idx]=1
    return r
populasi[0]
mutasi(populasi[3],1,3)
""" Fungsi Fitness """
def fFitnes(kromosom, maxt=50):
    berat = 0
    tpoin = 0
    for i in range(0, len(kromosom)):
        if kromosom[i]==1:
            berat = berat + beratbrg[i]
            tpoin = tpoin + valu[i]
    if berat>maxtotal:
        berat = 0
        return 0
    finalberat = 50 - (maxtotal - berat)
    return finalberat + tpoin
    # return finalberat, tpoin

# fFitnes([1,0,1,0,0,1])

""" Pencarian Terbaik N jumlah Untuk Proses Elitis """
def cariterbaik(fitnes, populasi, jml=2):
    list1, list2 = (list(x) for x in zip(
        *sorted(zip(fitnes, populasi), key=lambda pair: pair[0], reverse=True)))
    return list2[:jml]

fitnesterbaik = [fFitnes(kromosom) for kromosom in populasi]
fitnesterbaik
cariterbaik(fitnesterbaik, populasi,2)
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TesTerbaikc)
    unittest.TextTestRunner(verbosity=2).run(suite)
