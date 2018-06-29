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

""" Menggenerate Maze Secara Dinamis"""
""" 5 Adalah Parameter Besar Maze"""
myMaze = MazeMaker(5)
mazePrinter = MazePrinter()
maps = myMaze.getMap()
finish = myMaze.getFinishPosition()
mazePrinter.simplePrint(maps,"Maze Awal")
print(maps)
