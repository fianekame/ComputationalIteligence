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

""" Maze Generator Using Binary Tree"""
class MazeMaker:

    def __init__(self, size):
        self.size = size
        self.maps = [0] * (size*2+1)
        self.lastroad = size * 2 - 1
        self.mazeSize = size
        self.start = [1,1]
        self.finish = [self.lastroad+1,(size*2)//2]
        self.generateMaze()

    def generateMaze(self):
        for i in range(len(self.maps)):
            self.maps[i] = [0] * (self.size*2+1)
        for i in range(0,self.size*2+1):
            for j in range(0,self.size*2+1):
                if i%2==0 or j%2==0:
                    self.maps[i][j] = 1
                if i==self.lastroad:
                    if j!=0 and j!=self.size*2:
                        self.maps[i][j] = 0
                if j==self.lastroad:
                    if i!=0 and i!=self.size*2:
                        self.maps[i][j] = 0
        for i in range(1,self.lastroad,2):
            for j in range(1,self.lastroad,2):
                jalanke = random.randint(0, 1)
                if jalanke==0:
                    self.maps[i+1][j]=0;
                else:
                    self.maps[i][j+1]=0;
        self.maps[1][1] = 2
        self.maps[self.lastroad+1][(self.size*2)//2] = 3

    def getMap(self):
        return self.maps

    def getStartPosition(self):
        return self.start

    def getFinishPosition(self):
        return self.finish
