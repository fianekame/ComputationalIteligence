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

""" Inisialisasi Awal """
q = 1
titik = [0,1,2,3,4]
alpha = 1
beta = 1
rho = 0.5
jk = [[0, 4, 9, 11, 2],
         [4, 0, 3, 10, 8],
         [9, 3, 0, 5, 10],
         [11, 10, 5, 0, 7],
         [2, 8, 10, 7, 0]
         ]

to = [[0, 0.01, 0.01, 0.01, 0.01],
      [0.01, 0, 0.01, 0.01, 0.01],
      [0.01, 0.01, 0, 0.01, 0.01],
      [0.01, 0.01, 0.01, 0, 0.01],
      [0.01, 0.01, 0.01, 0.01, 0]
      ]

jarak = [[0, 0.25, 0.11, 0.09, 0.5],
         [0.25, 0, 0.33, 0.1, 0.125],
         [0.11, 0.33, 0, 0.2, 0.1],
         [0.09, 0.1, 0.2, 0, 0.14],
         [0.5, 0.125, 0.1, 0.14, 0]
         ]

""" Fungsi Pemotongan Desimal """
def potongdesimalangka(angka):
    return float("{0:.3f}".format(angka))

""" Pilih Random Untuk Routhele Wheel """
def ambilParent(fitprob,pick=-1):
    if pick==-1:
        pick = random.uniform(0, 1)
    current = 0
    for i in range (0,len(fitprob)):
        nilai = fitprob[i];
        current = current + nilai
        if current > pick:
            return i

""" Fungsi Menghitung Delta """
def jumlahDelta(delta,kombinasiant,skota):
    hasil = 0
    for i in range(0,len(kombinasiant)):
        semut = kombinasiant[i]
        stringkotasemut = ''.join(str(i) for i in semut )
        if skota in stringkotasemut:
            hasil = hasil + delta[i]
    return hasil

""" Fungsi Menghitung Total Awala """
def hitungTotal(kota,kotalewat):
    total = 0
    for i in range(0,len(jarak[kota])):
        if i not in kotalewat:
            total = total + (jarak[kota][i]*to[kota][i])
    return total

""" Pemilihan Kota Random Dengan Probabilitas Komulatif"""
def probKomulatif(kota,kotalewat,total):
    prob = []
    for i in range(0,len(jarak[kota])):
        if i not in kotalewat and i!=kota:
            hasil = potongdesimalangka((jarak[kota][i]*to[kota][i])/total)
            prob.append(hasil)
        else:
            prob.append(0)
    return prob

kota = 0
semut = 20
iterasike = 100
for x in range(0,iterasike):
    kombinasiant = []
    for j in range(0,semut):
        kotalewat = []
        setprob = [0.5,0.2,0.8]
        while len(kotalewat)!=5:
            iterasi = len(kotalewat)
            total = hitungTotal(kota,kotalewat)
            prob = probKomulatif(kota,kotalewat,total)
            kotalewat.append(kota)
            kota = ambilParent(prob)
            if len(kotalewat) == 3:
                kotalewat.append(kota)
                sisakota = [x for x in titik if x not in kotalewat]
                kotalewat.append(sisakota[0])
        kombinasiant.append(kotalewat)
        kota = kota + 1
        if kota == 5:
            kota = 0
    """ Menghitung Delta """
    delta = []
    for ant in kombinasiant:
        hasildelta = 0;
        for i in range(0,len(ant)-1):
            hasildelta = hasildelta + jk[ant[i]][ant[i+1]]
        delta.append(potongdesimalangka(q/hasildelta))
    """ Menghitung To Baru """
    for t in range(0,len(to)):
        tampung = to[t]
        to[t] = [(1-rho)*b for b in tampung]
    """ Update Pheromones """
    for i in range(0,len(to)):
        for j in range(0,len(to[i])):
            if i!=j:
                skota = str(i)+str(j)
                jd = jumlahDelta(delta,kombinasiant,skota)
                to[i][j] = to[i][j]+jd
    print("Iteraske "+str(x)+" : "+ str(kombinasiant))
