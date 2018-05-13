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

""" Tahap Inisialisai """
sinput = [[1, 1, 0, 0],[0, 0, 0, 1],[1, 0, 0, 0],[0, 0, 1, 1]]
wvector = [[0.2, 0.6, 0.5, 0.9], [0.8, 0.4, 0.7, 0.3]]
lr = 0.6
jmlepoch = 1
""" Fungsi Pangkat 2 """
def pangkatkan(list, power=1):
    return [number**power for number in list]

""" Fungsi Pemotogna Desimal Ke 3 Angka Terhakir [list] """
def potongdesimalinlist(list):
    return [float("{0:.3f}".format(number)) for number in list]

def potongdesimalangka(angka):
    return float("{0:.3f}".format(angka))

""" Iterasi Setiap Data Input """
for epoch in range(1,jmlepoch+1):
    """ Iterasi Setiap Data Input """
    for i in range(0,len(sinput)):
        print("Code Vektor (Bobot) "+ str(wvector))
        datainput = sinput[i]
        print("Input "+ str(datainput))
        distance = []
        """ Perhitungan Distance """
        for w in range(0,len(wvector)):
            bobot = wvector[w]
            hasil = pangkatkan([x - y for x, y in zip(datainput, bobot)],2)
            hasil = potongdesimalinlist(hasil)
            jarak = potongdesimalangka(sum(hasil[0:len(hasil)]))
            distance.append(abs(jarak))
        print("Perhitungan Jarak "+ str(distance))
        wwinner = distance.index(min(distance))
        print("Epochke "+ str(epoch)+ " -- Data Ke "+ str(i) +" -- Bobot Winner "+ str(wwinner))
        """ Update Bobot Winner """
        print("Bobot Sebelum "+ str(wvector[wwinner]))
        ubahbobot = deepcopy(wvector[wwinner])
        for bobot in range(0,len(wvector[wwinner])):
            hasil = wvector[wwinner][bobot]+lr*(datainput[bobot]-wvector[wwinner][bobot])
            ubahbobot[bobot] = potongdesimalangka(hasil)
        print("Bobot Sesudah "+ str(ubahbobot))
        wvector[wwinner] = ubahbobot
    lr = 0.5*lr
print(wvector)

""" Testing Data """
tesdata = [[0, 1, 0, 1],[0,0,0,1],[1, 1, 0, 0],[0, 1, 1, 1]]
print("Data "+ str(tesdata))
for i in range(0,len(tesdata)):
    datainput = tesdata[i]
    distance = []
    """ Perhitungan Distance """
    for w in range(0,len(wvector)):
        bobot = wvector[w]
        hasil = pangkatkan([x - y for x, y in zip(datainput, bobot)],2)
        hasil = potongdesimalinlist(hasil)
        jarak = potongdesimalangka(sum(hasil[0:len(hasil)]))
        distance.append(abs(jarak))
    wwinner = distance.index(min(distance))
    print("Data Ke "+ str(i+1) + " Cluster "+ str(wwinner))
