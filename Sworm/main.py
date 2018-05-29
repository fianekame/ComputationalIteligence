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
c = [0.5,1,1]
r = [0.1,0.2]
v = [0.0,0.0,0.0,0.0]
particle = [[-2],[-1],[4],[5]]

epoch = 3

def potongdesimalangka(angka):
    return float("{0:.3f}".format(angka))

""" Fungsi Fitnes """
def fungsiFitnes(x):
    return x**2 + 5*x + 10

""" Pencarian Particel Terbaik """
def findBest(particle):
    hasil = []
    for part in particle:
        hasil.append(fungsiFitnes(part))
    idx = hasil.index(min(hasil))
    return particle[idx]

for iterasi in range (0,epoch):
    print("Iterasi Ke "+ str(iterasi))
    """ Pencarian PBest Tiap Paticel """
    allpbest = []
    for part in particle:
        allpbest.append(findBest(part))
    print("Pbest "+ str(allpbest))
    """ Pencarian PgBest Dari Kumpulan PBest """
    pgbest = findBest(allpbest);
    print("PGbest "+ str(pgbest))
    """ Mengudpate Velocity """
    velocity = []
    for t in range(0,len(v)):
        velo = c[0]*v[t]+(c[1]*r[0])*(allpbest[t]-particle[t][-1])+c[2]*r[1]*(pgbest-particle[t][-1])
        velocity.append(potongdesimalangka(velo))
    print("Hasil Velocity "+ str(velocity))
    """ Update Particel """
    for t in range(0,len(particle)):
        newpart = particle[t][-1] + velocity[t]
        isibaru = findBest([newpart,particle[t][-1]])
        particle[t][0] = potongdesimalangka(isibaru)
    print("Particle Baru "+ str(particle))

print("===========")
print("Hasil Akhir")
print("===========")
print("Particle Akhir"+ str(particle))
allpbest = []
for part in particle:
    allpbest.append(findBest(part))
pgbest = findBest(allpbest);
flatdata = [item for sublist in particle for item in sublist]
print("Terbaik Data Ke - "+str(flatdata.index(pgbest)) + " Nilai Akhir "+ str(pgbest))
