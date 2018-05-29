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
beratbrg = [3,5,9,4,7,8]
valu = [15,25,30,20,5,10]
populasi = [[1, 0, 1, 0, 1, 0],
            [1, 1, 0, 0, 1, 0],
            [0, 0, 1, 1, 0, 1],
            [0, 1, 1, 1, 0, 0]
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

def mutasi(populasi,indexnya):
    pophasil = []
    r = deepcopy(populasi)
    for idx in range(indexnya[0],indexnya[1]+1):
        if r[idx]==1:
            r[idx]=0
        else:
            r[idx]=1
    return r

mutasi([0,1,1,1,0],[0,1])

""" Fungsi Fitness """
def fFitnes(kromosom, maxt=50):
    hasilfitnes = 0
    berat = 0
    tpoin = 0
    for i in range(0, len(kromosom)):
        if kromosom[i]==1:
            berat = berat + beratbrg[i]
            tpoin = tpoin + valu[i]
    if berat>maxtotal:
        berat = 0
    finalberat = 50 - (maxtotal - berat)
    return finalberat + tpoin

# fFitnes(populasi[4])

""" Pilih Random Untuk Routhele Wheel """
def ambilParent(fitprob):
    pick = random.uniform(0, 1)
    current = 0
    for i in range(0, len(fitprob)):
        nilai = fitprob[i]
        current = current + nilai
        if current > pick:
            return i


""" Pencarian Terbaik N jumlah Untuk Proses Elitis """
def cariterbaik(fitnes, populasi, jml=3):
    list1, list2 = (list(x) for x in zip(
        *sorted(zip(fitnes, populasi), key=lambda pair: pair[0], reverse=True)))
    return list2[:jml]


print("Populasi Awal " + str(populasi))
jumlahgen = 1
for gen in range(0, jumlahgen):
    print("Generasi Ke - " + str(gen))
    """ Hitung Fitnes Tiap Populasi"""
    hasilfitnes = [fFitnes(kromosom) for kromosom in populasi]
    print("Hasil Fitnes " + str(hasilfitnes))
    terbaikawal = cariterbaik(hasilfitnes, populasi)
    print("Terbaik Awal " + str(terbaikawal))
    """ Roulette Wheels Selection // Seleksi Proses"""
    jumlah = sum(hasilfitnes[0:len(hasilfitnes)])
    fitprob = [fitnes / jumlah for fitnes in hasilfitnes]
    hasilseleksi = [ambilParent(fitprob) for i in range(6)]
    # hasilseleksi = [0,1,2,1]
    print("Hasil Seleksi " + str(hasilseleksi))
    populasiseleksi = [populasi[i] for i in hasilseleksi]
    print("Hasil Rank " + str(populasiseleksi))
    """ Crossover """
    pjgindividu = 10
    jmlindividu = 6
    indexcrossover = [random.choices(range(pjgindividu), k=2) for i in range(0, int(jmlindividu/2))]
    # indexcrossover = [[1, 3], [0, 0], [1, 2]] contoh index crossover miasl 6 maka diperlukan cuma 3 data indexcross
    indexcrossover = [sorted(i) for i in indexcrossover]
    print("Index Crossover " + str(indexcrossover))
    populasicrosover = []
    indexcrosnya = 0
    for i in range(0,jmlindividu,2):
        i1,i2 = indexcrossover[indexcrosnya][0],indexcrossover[indexcrosnya][1]
        newl1 = deepcopy(populasiseleksi[i])
        newl2 = deepcopy(populasiseleksi[i+1])
        hasilcross = crossOver([newl1,newl2],i1,i2)
        hasilcross
        populasicrosover.append(hasilcross[0])
        populasicrosover.append(hasilcross[1])
        indexcrosnya = indexcrosnya + 1
    print("Populasi Crossover " + str(populasicrosover))
    """ Mutasi """
    indexmutasi = [random.choices(range(pjgindividu), k=2)
                   for i in range(0, jmlindividu)]
    indexmutasi = [sorted(i) for i in indexmutasi]
    # indexmutasi = [[0, 3], [1, 3], [2, 1], [3, 0]] contoh mutas jika da 6 data berarti dibtuh 6 data index juga
    print("Index Mutasi " + str(indexmutasi))
    populasimutasi = []
    for i in range(0, len(populasicrosover)):
        indexnya = indexmutasi[i]
        hasilmut = mutasi(populasicrosover[i],indexnya)
        # r = deepcopy(populasicrosover[i])
        # for idx in range(indexnya[0],indexnya[1]+1):
        #     if r[idx]==1:
        #         r[idx]=0
        #     else:
        #         r[idx]=1
        populasimutasi.append(hasilmut)
    print("Populasi Mutasi " + str(populasimutasi))
    # print(populasimutasi)
    """ Hitung Fitnes Tiap Populasi Yang Sudah Dimutasi"""
    hasilfitnesbaru = [fFitnes(kromosom) for kromosom in populasimutasi]
    terbaikmutasi = cariterbaik(hasilfitnesbaru, populasimutasi)
    print("Hasil Fitnes (Mutasi) " + str(hasilfitnesbaru))
    print("Terbaik Mutasi " + str(terbaikmutasi))
    """ ELITIS """
    populasi = terbaikawal + terbaikmutasi
    print("Populasi Baru " + str(populasi))
    print("=================")

fitnesterbaik = [fFitnes(kromosom) for kromosom in populasi]
terbaik = cariterbaik(fitnesterbaik, populasi, 1)
print("Hasil Akhir " + str(terbaik))
