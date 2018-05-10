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
populasi = [[2, 1, 3, 4],
            [2, 1, 4, 3],
            [1, 4, 3, 2],
            [4, 1, 2, 3]
            ]

""" Fungsi Fitness """
def fFitnes(kromosom, max=50):
    hasilfitnes = 0
    for i in range(0,len(kromosom)-1):
        kota1 = kromosom[i]
        kota2 = kromosom[i+1]
        hasil = (kordinat[kota1][0] - kordinat[kota2][0])**2 + (kordinat[kota1][1] - kordinat[kota2][1])**2
        # print(hasil)
        hasilfitnes = hasilfitnes + math.sqrt(hasil)
    return max - hasilfitnes

def getSelection(fitprob):
    pick = random.uniform(0, 1)
    current = 0
    for i in range (0,len(fitprob)):
        nilai = fitprob[i];
        current = current + nilai
        if current > pick:
            return i



""" Hitung Fitnes Tiap Populasi"""
hasilfitnes = []
for kromosom in populasi:
    hasilfitnes.append(fFitnes(kromosom))
hasilfitnes



""" Roulette Wheels Selection // Seleksi Proses"""
jumlah = sum(hasilfitnes[0:len(hasilfitnes)])
jumlah
fitprob = []
for fitnes in hasilfitnes:
    probabilitas = (fitnes/jumlah)
    fitprob.append(probabilitas)
fitprob



hasilseleksi = [1,2,3,2]
populasiseleksi = []
for kotaseleksi in hasilseleksi:
    populasiseleksi.append(populasi[kotaseleksi-1])
populasiseleksi
""" Crossover """
pjgindividu = 4
indexcrossover = []
for i in range(0,pjgindividu):
    indexcrossover.append(random.choices(range(pjgindividu), k=2))
indexcrossover = [[1, 3], [0, 0], [1, 2], [0, 1]]
populasicrosover = []
for i in range(0,len(populasiseleksi)):
    r = deepcopy(populasiseleksi[i])
    ix,iy = indexcrossover[i][0],indexcrossover[i][1]
    x,y = populasiseleksi[i][ix],populasiseleksi[i][iy]
    r[ix] = y
    r[iy] = x
    populasicrosover.append(r)
print(populasicrosover)
""" Mutasi """
indexmutasi = []
for i in range(0,pjgindividu):
    indexmutasi.append(random.choices(range(pjgindividu), k=2))
indexmutasi = [[0, 3], [1, 3], [2, 1], [3, 0]]
populasimutasi = []
for i in range(0,len(populasicrosover)):
    r = deepcopy(populasicrosover[i])
    ix,iy = indexmutasi[i][0],indexmutasi[i][1]
    x,y = populasicrosover[i][ix],populasicrosover[i][iy]
    r[ix] = y
    r[iy] = x
    populasimutasi.append(r)
print(populasimutasi)
""" Hitung Fitnes Tiap Populasi Yang Sudah Dimutasi"""
hasilfitnesbaru = []
for kromosom in populasimutasi:
    hasilfitnesbaru.append(fFitnes(kromosom))
hasilfitnesbaru

""" KURANG KOMBINASI ANTAR TERBIAK SEBELUMNYA DAN SESDUAHNYA""""
