import sys
import time
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
from MazeGenerator import MazeMaker
from MazePrinter import MazePrinter

""" Fungsi Untuk Menampilkan Maps """
def showMaps(maps):
    for data in maps:
        for gen in data:
            if gen==0:
                print(" ",end='')
            else:
                print(gen,end='')
        print()

""" Fungsi Fitness """
def fitnesFunc(kromosom, maxs=100):
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
def rwPick(fitprob):
    pick = random.uniform(0, 1)
    current = 0
    for i in range (0,len(fitprob)):
        nilai = fitprob[i];
        current = current + nilai
        if current > pick:
            return i

""" Pencarian Kromosom Terbaik Sebanyak N jumlah """
def getBestKromosom(fitnes,populasi,jml=3):
    list1, list2 = (list(x) for x in zip(*sorted(zip(fitnes, populasi), key=lambda pair:pair[0], reverse=True )))
    return list2[:jml]

"""  """
""" Menggenerate Maze Secara Dinamis"""
""" 5 Adalah Parameter Besar Maze"""
myMaze = MazeMaker(5)
mazePrinter = MazePrinter()
maps = myMaze.getMap()
finish = myMaze.getFinishPosition()
mazePrinter.simplePrint(maps,"Maze Awal")
"""  """
""" Inisialisasi Awal """
jmlGen = 50
jmlKromosom = 6
jmlGenerasi = 500

""" Pembuatan Populasi """
""" 0,3 = 0 Sampai 3 0 Atas 1 Kanan 2 Kiri 3 Bawah """
populasi = [[randint(0,3) for i in range(0,jmlGen)] for i in range(0,jmlKromosom)]

""" Proses Re-Generasi """
loading = [".","..","..."]
lastgen = 0
print("Proses Training",jmlGenerasi,"Generasi")
print()
for generasi in range(0,jmlGenerasi):
    """ Animasi Training  """
    time.sleep(0.1)
    sys.stdout.write("\r Training Generasi Ke-"+ str(generasi) + str(loading[generasi % len(loading)]))
    sys.stdout.flush()
    lastgen = generasi
    # print("Generasi Ke - "+ str(generasi))
    """ Hitung Fitnes Tiap Populasi """
    hasilfitnes = [fitnesFunc(kromosom) for kromosom in populasi]
    """ Menyimpan Kromosom Terbaik Di Awal """
    terbaikawal = getBestKromosom(hasilfitnes,populasi)

    """ Roulette Wheels Selection // Proses Penseleksi Dan Menciptakan Kromosom Baru"""
    jumlah = sum(hasilfitnes[0:len(hasilfitnes)])
    fitprob = [fitnes/jumlah for fitnes in hasilfitnes]
    hasilseleksi = [rwPick(fitprob) for i in range(jmlKromosom)]
    populasiseleksi = [populasi[i] for i in hasilseleksi]

    """ Proses Crossover """
    indexcrossover = [random.choices(range(jmlGen), k=2) for i in range(0,jmlKromosom)]
    populasicrosover = []
    for i in range(0,len(populasiseleksi)):
        r = deepcopy(populasiseleksi[i])
        ix,iy = indexcrossover[i][0],indexcrossover[i][1]
        x,y = populasiseleksi[i][ix],populasiseleksi[i][iy]
        r[ix] = y
        r[iy] = x
        populasicrosover.append(r)

    """ Proses Mutasi """
    indexmutasi = [random.choices(range(jmlGen), k=2) for i in range(0,jmlKromosom)]
    populasimutasi = []
    for i in range(0,len(populasicrosover)):
        r = deepcopy(populasicrosover[i])
        ix,iy = indexmutasi[i][0],indexmutasi[i][1]
        x,y = populasicrosover[i][ix],populasicrosover[i][iy]
        r[ix] = y
        r[iy] = x
        populasimutasi.append(r)

    """ Hitung Fitnes Tiap Kromosom Yang Sudah Dimutasi"""
    hasilfitnesbaru = [fitnesFunc(kromosom) for kromosom in populasimutasi]
    terbaikmutasi = getBestKromosom(hasilfitnesbaru,populasimutasi)

    """ Proses Elitis """
    populasi = terbaikawal + terbaikmutasi
    # print("="*18)
    fitnesterbaik = [fitnesFunc(kromosom) for kromosom in populasi]
    if fitnesterbaik[0]>=98.0:
        break
print()
print("\r Training Selesai Di Generasi-"+str(lastgen))
print()

fitnesterbaik = [fitnesFunc(kromosom) for kromosom in populasi]
terbaik = getBestKromosom(fitnesterbaik,populasi,1)
print("Hasil Fitness " + str(fitnesterbaik))
jalur = " ".join(str(x) for x in terbaik[0])
print("Alur Tranversal ",jalur)
mazePrinter.animPrint(maps,terbaik[0],"Tranversal Proses")
