#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 19:32:10 2018

@author: root
"""

#tabel AND
AND = [
        [1,1,1,1],[1,1,0,0],[1,0,1,0],[1,0,0,0]
    ]

OR = [
        [1,0,0,0],
        [1,0,1,1],
        [1,1,0,1],
        [1,1,1,1]
    ]

x0 = 1

# x > x[0] / x[1]
# nyari_y(x[0],w)
def nyari_y(x,w):
    net=0
    for i in range(len(w)):
        net += x[i]*w[i]

    if net <= 0.5:
        return 0
    elif net > 0.5:
        return 1

# x > x[0] / x[1]
# nyari_y(y,x[0],w)
def cek_bobot(y,x,w):
    if y < x[3]:
        for i in range(len(w)):
            w[i] = w[i] + x[i]
            w[i] = round(w[i],2)
    elif y > x[3]:
        for i in range(len(w)):
            w[i] = w[i] - x[i]
            w[i] = round(w[i],2)
    return w

def perceptron(epoch,x,w):
    for z in range(epoch):
        for t in range(len(x)):
            y = nyari_y(x[t],w)
            #print('y',t+1,' ',y)
            w = cek_bobot(y,x[t],w)
            #print('w',t+1,' ',w)
    return w
(1*-2.7) + (1*2.2) + (1*1.4)
# epoch = (int(input("Masukkan Jumlah epoch : ")))
epoch = 10
weight = [0.3, 0.2, 0.4]
print("bobot akhir tabel AND epoch ",epoch," :",perceptron(epoch,AND,weight))
weight = [0.3, 0.2, 0.4]
print("bobot akhir tabel OR epoch ",epoch," :",perceptron(epoch,OR,weight))
