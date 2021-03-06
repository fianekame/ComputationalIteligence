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
maps = [0] * (size*2+1)
finish = [size * 2,(size*2)//2]
maps = [0] * (size*2+1)
# generateMaze()
maps = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 2, 0, 0, 1, 0, 0, 0, 0, 0, 1 ],
 [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
 [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
 [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
 [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
 [1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1]]

def showMaps(maps):
    for data in maps:
        for gen in data:
            if gen==0:
                print(" ",end='')
            else:
                print(gen,end='')
        print()

populasi = [[0, 0, 0, 1, 1, 3, 1, 2, 2, 0, 3, 0, 3, 2, 0, 3, 3, 0, 0, 1],
 [1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 3, 3, 3, 1, 2, 2, 2, 3, 2, 3],
 [1, 0, 3, 0, 0, 1, 1, 0, 1, 2, 0, 1, 3, 3, 0, 2, 0, 3, 3, 2],
 [1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2],
 [2, 2, 0, 0, 2, 1, 3, 1, 2, 1, 3, 0, 3, 1, 0, 0, 0, 3, 0, 2],
 [1, 2, 2, 3, 0, 0, 1, 0, 0, 0, 1, 2, 3, 2, 2, 1, 0, 2, 3, 0]]
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
        if gen==3:
            if maps[cpy+1][cpx]!=1:
                cpy = cpy + 1
    jarak = (cpy - finish[0])**2 + (cpx - finish[1])**2
    return maxs - math.sqrt(jarak)

""" Pilih Random Untuk Routhele Wheel """
def ambilParent(fitprob):
    pick = random.uniform(0, 1)
    # print("random number ",pick)
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

def potongdesimalangka(angka):
    return float("{0:.2f}".format(angka))
# pp.pprint("Populasi Awal "+ str(populasi))
jumlahgen = 1
for gen in range(0,jumlahgen):
    # print("Generasi Ke - "+ str(gen))
    """ Hitung Fitnes Tiap Populasi"""
    hasilfitnes = [potongdesimalangka(fFitnes(kromosom)) for kromosom in populasi]
    # print("Hasil Fitnes "+ str(hasilfitnes))
    terbaikawal = cariterbaik(hasilfitnes,populasi)
    # print("Terbaik Awal "+ str(terbaikawal))
    """ Roulette Wheels Selection // Seleksi Proses"""
    jumlah = sum(hasilfitnes[0:len(hasilfitnes)])
    # print("Jumlah "+ str(potongdesimalangka(jumlah)))
    fitprob = [potongdesimalangka(fitnes/jumlah) for fitnes in hasilfitnes]
    # print("Probabilitas "+ str(fitprob))
    current = 0
    # for i in range(0,len(fitprob)):
    #     print("data ke ",i, "prob = ",current, " sampai ", current+fitprob[i])
    #     current = current+fitprob[i]

    hasilseleksi = [ambilParent(fitprob) for i in range(6)]
    hasilseleksi
    # hasilseleksi = [0,1,2,1]
    # print("Hasil Seleksi "+ str(hasilseleksi))
    populasiseleksi = [populasi[i] for i in hasilseleksi]
    print("Hasil Rank "+ str(populasiseleksi[0]))
    """ Crossover """
    jumlahgen = 20
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
    # print("Populasi Crossover "+str(populasicrosover[0]))
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
    print("Hasil Fitnes (Mutasi) "+ str(hasilfitnesbaru))
    print("Terbaik Mutasi "+ str(terbaikmutasi))
    """ ELITIS """
    populasi = terbaikawal + terbaikmutasi
    # print("Populasi Baru "+ str(populasi))
    # print("=================")

j = [4, 5, 6, 7, 1, 3, 7, 5]
if sum(i > 5 for i in j) > 0:
    print("heheh")

# fitnesterbaik = [fFitnes(kromosom) for kromosom in populasi]
# terbaik = cariterbaik(fitnesterbaik,populasi,1)
# print("Hasil Fitness " + str(fitnesterbaik))
# print("Hasil Akhir " + str(terbaik))
# print("=================")
# showMaps(maps)
# roadmap = deepcopy(maps)
# print("=================")
# cpx = 1
# cpy = 1
# for gen in terbaik[0]:
#     if gen==0:
#         if maps[cpy-1][cpx]!=1:
#             roadmap[cpy-1][cpx] = 4
#             cpy = cpy - 1
#     if gen==1:
#         if maps[cpy][cpx+1]!=1:
#             roadmap[cpy][cpx+1] = 4
#             cpx = cpx + 1
#     if gen==2:
#         if maps[cpy][cpx-1]!=1:
#             roadmap[cpy][cpx-1] = 4
#             cpx = cpx - 1
#     if gen==3:
#         if maps[cpy+1][cpx]!=1:
#             roadmap[cpy+1][cpx] = 4
#             cpy = cpy + 1
#
# print(cpy,cpx)
# showMaps(roadmap)
