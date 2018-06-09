import time
import sys
from copy import deepcopy
import numpy as np


def showMaps(maps, fix=False):
    for data in maps:
        for gen in data:
            if gen==0:
                sys.stdout.write(" ")
                # sys.stdout.flush()
                # print(" ",end='')
            else:
                sys.stdout.write(str(gen))
                # print(gen,end='')
        # print()
        sys.stdout.write("\n")
    sys.stdout.flush()


animation = "|/-\\"
terbaik = [[1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2]]
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

def stringMap(maps):
    hasil = ""
    for listin in maps:
        hasil =  hasil + "\t"
        for i in range(0,len(listin)):
            if listin[i] == 0:
                hasil =  hasil + " "
            else:
                hasil =  hasil + str(listin[i])
            if i==len(listin)-1:
                hasil =  hasil + str("\n")
    return hasil

def printAnim(maps):
    sys.stdout.write("\r" + stringMap(maps))
    sys.stdout.flush()
    # print()

roadmap = deepcopy(maps)
cpx = 1
cpy = 1
print()
for i in range(0,len(terbaik[0])):
    gen = terbaik[0][i]
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
    if gen==3:
        if maps[cpy+1][cpx]!=1:
            roadmap[cpy+1][cpx] = 4
            cpy = cpy + 1

    print("\r"+stringMap(roadmap))
    if i!=len(terbaik[0])-1:
        sys.stdout.write("\033[F"*(len(roadmap)+1))
    time.sleep(0.3)
    sys.stdout.flush()

print()
