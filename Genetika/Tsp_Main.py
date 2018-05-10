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

kordinat = [[],[2, 2], [5, 2], [5, 6], [2, 6]]
populasi = [[4, 1, 2, 3],
            [1, 4, 3, 2],
            [4, 2, 1, 3],
            [1, 2, 3, 4],
            ]
# list1, list2 = (list(x) for x in zip(*sorted(zip(l, populasi), key=lambda pair:pair[0], reverse=True )))

""" Fungsi Fitness """
def fFitnes(kromosom, max=50):
    hasilfitnes = 0
    for i in range(0,len(kromosom)-1):
        kota1 = kromosom[i]
        kota2 = kromosom[i+1]
        hasil = (kordinat[kota1][0] - kordinat[kota2][0])**2 + (kordinat[kota1][1] - kordinat[kota2][1])**2
        hasilfitnes = hasilfitnes + math.sqrt(hasil)
    return max - hasilfitnes

""" Pilih Random Untuk Routhele Wheel """
def ambilParent(fitprob):
    pick = random.uniform(0, 1)
    current = 0
    for i in range (0,len(fitprob)):
        nilai = fitprob[i];
        current = current + nilai
        if current > pick:
            return i

""" Pencarian Terbaik N jumlah Untuk Proses Elitis """
def cariterbaik(fitnes,populasi,jml=2):
    list1, list2 = (list(x) for x in zip(*sorted(zip(fitnes, populasi), key=lambda pair:pair[0], reverse=True )))
    return list2[:jml]

print("Populasi Awal "+ str(populasi))
jumlahgen = 5
for gen in range(0,jumlahgen):
    print("Generasi Ke - "+ str(gen))
    """ Hitung Fitnes Tiap Populasi"""
    hasilfitnes = [fFitnes(kromosom) for kromosom in populasi]
    print("Hasil Fitnes "+ str(hasilfitnes))
    terbaikawal = cariterbaik(hasilfitnes,populasi)
    print("Terbaik Awal "+ str(terbaikawal))
    """ Roulette Wheels Selection // Seleksi Proses"""
    jumlah = sum(hasilfitnes[0:len(hasilfitnes)])
    fitprob = [fitnes/jumlah for fitnes in hasilfitnes]
    hasilseleksi = [ambilParent(fitprob) for i in range(4)]
    # hasilseleksi = [0,1,2,1]
    print("Hasil Seleksi "+ str(hasilseleksi))
    populasiseleksi = [populasi[i] for i in hasilseleksi]
    print("Hasil Rank "+ str(populasiseleksi))
    """ Crossover """
    pjgindividu = 4
    indexcrossover = [random.choices(range(pjgindividu), k=2) for i in range(0,pjgindividu)]
    # indexcrossover = [[1, 3], [0, 0], [1, 2], [0, 1]]
    print("Index Crossover "+ str(indexcrossover))
    populasicrosover = []
    for i in range(0,len(populasiseleksi)):
        r = deepcopy(populasiseleksi[i])
        ix,iy = indexcrossover[i][0],indexcrossover[i][1]
        x,y = populasiseleksi[i][ix],populasiseleksi[i][iy]
        r[ix] = y
        r[iy] = x
        populasicrosover.append(r)
    print("Populasi Crossover "+str(populasicrosover))
    """ Mutasi """
    indexmutasi = [random.choices(range(pjgindividu), k=2) for i in range(0,pjgindividu)]
    # indexmutasi = [[0, 3], [1, 3], [2, 1], [3, 0]]
    print("Index Mutasi "+ str(indexmutasi))
    populasimutasi = []
    for i in range(0,len(populasicrosover)):
        r = deepcopy(populasicrosover[i])
        ix,iy = indexmutasi[i][0],indexmutasi[i][1]
        x,y = populasicrosover[i][ix],populasicrosover[i][iy]
        r[ix] = y
        r[iy] = x
        populasimutasi.append(r)
    print("Populasi Mutasi "+str(populasimutasi))
    # print(populasimutasi)
    """ Hitung Fitnes Tiap Populasi Yang Sudah Dimutasi"""
    hasilfitnesbaru = [fFitnes(kromosom) for kromosom in populasimutasi]
    terbaikmutasi = cariterbaik(hasilfitnesbaru,populasimutasi)
    print("Hasil Fitnes (Mutasi) "+ str(hasilfitnesbaru))
    print("Terbaik Mutasi "+ str(terbaikmutasi))
    """ ELITIS """
    populasi = terbaikawal + terbaikmutasi
    print("Populasi Baru "+ str(populasi))
    print("=================")

fitnesterbaik = [fFitnes(kromosom) for kromosom in populasi]
terbaik = cariterbaik(fitnesterbaik,populasi,1)
print("Hasil Akhir " + str(terbaik))
