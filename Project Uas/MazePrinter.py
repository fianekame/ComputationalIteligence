import sys
import time
import IPython
import numpy as np
import pprint as pp
from copy import deepcopy

""" The Pretty Print For Maze """
class MazePrinter:

    """ Change List To String / Beatifull Concept """
    def toStringMaps(self,maps):
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

    """ To Print Maze Without Animation """
    def simplePrint(self, maps, judul):
        print("\n\t"+judul)
        print("\n"+self.toStringMaps(maps))

    """ Print Maze With Animation """
    def animPrint(self, maps, jalur, judul):
        print("\n\t"+judul)
        roadmap = deepcopy(maps)
        cpx = 1
        cpy = 1
        print()
        for i in range(0,len(jalur)):
            gen = jalur[i]
            laststop = []
            if gen==0:
                if maps[cpy-1][cpx]!=1:
                    roadmap[cpy-1][cpx] = 4
                    laststop = [cpy-1,cpx]
                    cpy = cpy - 1
            if gen==1:
                if maps[cpy][cpx+1]!=1:
                    roadmap[cpy][cpx+1] = 4
                    laststop = [cpy,cpx+1]
                    cpx = cpx + 1
            if gen==2:
                if maps[cpy][cpx-1]!=1:
                    roadmap[cpy][cpx-1] = 4
                    laststop = [cpy,cpx-1]
                    cpx = cpx - 1
            if gen==3 and cpy+1<10:
                if maps[cpy+1][cpx]!=1:
                    roadmap[cpy+1][cpx] = 4
                    laststop = [cpy+1,cpx]
                    cpy = cpy + 1
            print("\r"+self.toStringMaps(roadmap))
            if i!=len(jalur)-1:
                sys.stdout.write("\033[F"*(len(roadmap)+1))
            time.sleep(0.2)
            sys.stdout.flush()
            """ To Pritnt Player Movement Uncomment It """
            # if len(laststop)!=0 and i!=len(jalur)-1:
            #     roadmap[laststop[0]][laststop[1]] = 0
        print("\tTransversal Selesai\n")
