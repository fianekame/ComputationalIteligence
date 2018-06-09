import sys
import IPython
import numpy as np
import pprint as pp
import sklearn
import matplotlib.pyplot as plt
from IPython.display import display
import random
from random import randint
from copy import deepcopy
import math
size = 5;
mustroad = size * 2 - 1
maps = [0] * (size*2+1)
finish = [mustroad+1,(size*2)//2]
def generateMaze():
    for i in range(len(maps)):
        maps[i] = [0] * (size*2+1)
    for i in range(0,size*2+1):
        for j in range(0,size*2+1):
            if i%2==0 or j%2==0:
                maps[i][j] = 1
            if i==mustroad:
                if j!=0 and j!=size*2:
                    maps[i][j] = 0
            if j==mustroad:
                if i!=0 and i!=size*2:
                    maps[i][j] = 0
    for i in range(1,mustroad,2):
        for j in range(1,mustroad,2):
            jalanke = random.randint(0, 1) #o atas 1 kanan
            if jalanke==0:
                maps[i+1][j]=0;
            else:
                maps[i][j+1]=0;
    maps[1][1] = 2
    maps[mustroad+1][(size*2)//2] = 3

maps = [0] * (size*2+1)
generateMaze()

def showMaps(maps):
    for data in maps:
        for gen in data:
            if gen==0:
                print(" ",end='')
            else:
                print(gen,end='')
        print()

populasi = [[randint(0,3) for i in range(0,50)] for i in range(0,6)]
showMaps(maps)
""" Fungsi Fitness """
def fFitnes(kromosom, maxs=100):
    cpx = 1
    cpy = 1
    for gen in kromosom:
        if gen==0:
            if maps[cpy-1][cpx]!=1:
                cpy = cpy - 1
        if gen==1:
            if maps[cpy][cpx+1]!=1:
                cpx = cpx + 1
        if gen==2:
            if maps[cpy][cpx-1]!=1:
                cpx = cpx - 1
        if gen==3 and cpy+1<10:
            if maps[cpy+1][cpx]!=1:
                cpy = cpy + 1
    jarak = (cpy - finish[0])**2 + (cpx - finish[1])**2
    return maxs - math.sqrt(jarak)

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
def cariterbaik(fitnes,populasi,jml=3):
    list1, list2 = (list(x) for x in zip(*sorted(zip(fitnes, populasi), key=lambda pair:pair[0], reverse=True )))
    return list2[:jml]

print("Populasi Awal "+ str(populasi))
jumlahgen = 800
for gen in range(0,jumlahgen):
    print("Generasi Ke - "+ str(gen))
    """ Hitung Fitnes Tiap Populasi"""
    hasilfitnes = [fFitnes(kromosom) for kromosom in populasi]
    # print("Hasil Fitnes "+ str(hasilfitnes))
    terbaikawal = cariterbaik(hasilfitnes,populasi)
    # print("Terbaik Awal "+ str(terbaikawal))
    """ Roulette Wheels Selection // Seleksi Proses"""
    jumlah = sum(hasilfitnes[0:len(hasilfitnes)])
    fitprob = [fitnes/jumlah for fitnes in hasilfitnes]
    hasilseleksi = [ambilParent(fitprob) for i in range(6)]
    hasilseleksi
    # hasilseleksi = [0,1,2,1]
    # print("Hasil Seleksi "+ str(hasilseleksi))
    populasiseleksi = [populasi[i] for i in hasilseleksi]
    # print("Hasil Rank "+ str(populasiseleksi))
    """ Crossover """
    jumlahgen = 50
    jumlahkromosom = 6
    indexcrossover = [random.choices(range(jumlahgen), k=2) for i in range(0,jumlahkromosom)]
    # indexcrossover = [[1, 3], [0, 0], [1, 2], [0, 1]]
    # print("Index Crossover "+ str(indexcrossover))
    populasicrosover = []
    for i in range(0,len(populasiseleksi)):
        r = deepcopy(populasiseleksi[i])
        ix,iy = indexcrossover[i][0],indexcrossover[i][1]
        x,y = populasiseleksi[i][ix],populasiseleksi[i][iy]
        r[ix] = y
        r[iy] = x
        populasicrosover.append(r)
    # print("Populasi Crossover "+str(populasicrosover))
    """ Mutasi """
    indexmutasi = [random.choices(range(jumlahgen), k=2) for i in range(0,jumlahkromosom)]
    # indexmutasi = [[0, 3], [1, 3], [2, 1], [3, 0]]
    # print("Index Mutasi "+ str(indexmutasi))
    populasimutasi = []
    for i in range(0,len(populasicrosover)):
        r = deepcopy(populasicrosover[i])
        ix,iy = indexmutasi[i][0],indexmutasi[i][1]
        x,y = populasicrosover[i][ix],populasicrosover[i][iy]
        r[ix] = y
        r[iy] = x
        populasimutasi.append(r)
    # print("Populasi Mutasi "+str(populasimutasi))
    # # print(populasimutasi)
    """ Hitung Fitnes Tiap Populasi Yang Sudah Dimutasi"""
    hasilfitnesbaru = [fFitnes(kromosom) for kromosom in populasimutasi]
    terbaikmutasi = cariterbaik(hasilfitnesbaru,populasimutasi)
    # print("Hasil Fitnes (Mutasi) "+ str(hasilfitnesbaru))
    # print("Terbaik Mutasi "+ str(terbaikmutasi))
    """ ELITIS """
    populasi = terbaikawal + terbaikmutasi
    print("Populasi Baru "+ str(populasi))
    print("=================")

fitnesterbaik = [fFitnes(kromosom) for kromosom in populasi]
terbaik = cariterbaik(fitnesterbaik,populasi,1)
print("Hasil Fitness " + str(fitnesterbaik))
print("Hasil Akhir " + str(terbaik))
print("=================")
showMaps(maps)
roadmap = deepcopy(maps)
print("=================")
cpx = 1
cpy = 1
for gen in terbaik[0]:
    if gen==0:
        if maps[cpy-1][cpx]!=1:
            roadmap[cpy-1][cpx] = 4
            cpy = cpy - 1
    if gen==1:
        if maps[cpy][cpx+1]!=1:
            roadmap[cpy][cpx+1] = 4
            cpx = cpx + 1
    if gen==2:
        if maps[cpy][cpx-1]!=1:
            roadmap[cpy][cpx-1] = 4
            cpx = cpx - 1
    if gen==3 and cpy+1<10:
        if maps[cpy+1][cpx]!=1:
            roadmap[cpy+1][cpx] = 4
            cpy = cpy + 1
print(cpy,cpx)
showMaps(roadmap)
