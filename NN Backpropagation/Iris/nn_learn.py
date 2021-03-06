import sys
import IPython
import numpy as np
import pprint as pp
import sklearn
import matplotlib.pyplot as plt
from IPython.display import display
import random
from copy import deepcopy
from sklearn.datasets import load_iris

""" Load Digit Data """
irisset = load_iris()
x, y = irisset.data, irisset.target
y
""" Split Data & Get 20 / Class """
x1, x2, x3 = list(x[0:20]), list(x[50:70]), list(x[100:120])
xtrain = x1 + x2 + x3
xtrain
y1, y2, y3 = list(y[0:20]), list(y[50:70]), list(y[100:120])
ytrain = y1 + y2 + y3
# xtest
x1, x2, x3 = list(x[20:50]), list(x[70:100]), list(x[120:150])
xtest = x1 + x2 + x3
y1, y2, y3 = list(y[20:50]), list(y[70:100]), list(y[120:150])
ytest = y1 + y2 + y3

""" Init Network """


def init_network(inputlayer, hiddenlayer, outputlayer):
    network = {}
    network['bobot_w'] = [[random.random() for i in range(inputlayer + 1)]
                          for i in range(hiddenlayer)]
    network['bobot_v'] = [[random.random() for i in range(hiddenlayer + 1)]
                          for i in range(outputlayer)]
    return network


""" One Hot Encoding """


def onehotouput(ytarget, size=3):
    res = [0] * size
    res[size - ytarget - 1] = 1
    return res


""" Fungsi Pangkat 2 """


def pangkatkan(list, power=1):
    return [number**power for number in list]


""" Eror Function """


def hitungeror(target, ouput):
    hasil = pangkatkan([x - y for x, y in zip(target, ouput)], 2)
    hasil = sum(hasil[0:len(hasil)]) / len(target)
    hasil = 0.5 * hasil
    return hasil


""" Sigmoid Function """


def aktivasi(nilainet):
    return 1.0 / (1.0 + np.exp(-nilainet))


""" ff = FEEDFORWARD PROSES """
""" Compute NetInput Y & Return The Activation Result """


def ffInputHidden(xdata, bobotw):
    knety = []
    y = [1]
    for bobot in bobotw:
        netinput = 0
        for i in range(0, len(xdata)):
            netinput = netinput + (bobot[i] * xdata[i])
        knety.append(netinput)
        aktivy = aktivasi(netinput)
        y.append(aktivy)
    print("Net Input Y= ", knety)
    print("Aktivasi Y= ", y)
    return y


""" Compute NetInput O & Return The Activation Result """


def ffHiddenOuput(ydata, bobotv):
    knetok = []
    ok = []
    for bobot in bobotv:
        netinput = 0
        for i in range(0, len(ydata)):
            netinput = netinput + (bobot[i] * ydata[i])
        knetok.append(netinput)
        aktivok = aktivasi(netinput)
        ok.append(aktivok)
    print("Net Input OK= ", knetok)
    print("Aktivasi OK= ", ok)
    return ok


""" bw = Backward Proses """
""" Compute DeltaVJK For New V Weight """

def bwOuputHidden(y, bobotv, dataok, target, lrate):
    datadeltaok = []
    for i in range(0, len(bobotv)):
        bobot = bobotv[i]
        delok = (target[i] - dataok[i]) * (1 - dataok[i]) * dataok[i]
        datadeltaok.append(delok)
        for j in range(0, len(bobot)):
            # print(bobot[j]," ",lrate," ",delok," ",y[j])
            deltavjk = bobot[j] + (lrate * delok * y[j])
            bobotv[i][j] = deltavjk
    print("DelOk = ", datadeltaok)
    print("V =", bobotv)
    return datadeltaok, bobotv


""" Compute DeltaW For New W Weight """
def bwHiddenInput(x, y, bobotw, datadeltaok, tempbobotv, lrate):
    kdely = []
    for i in range(0, len(bobotw)):
        bobot = bobotw[i]
        hasildely = 0
        for j in range(0, len(datadeltaok)):
            hasildely = hasildely + (datadeltaok[j] * tempbobotv[j][i + 1])
        kdely.append(hasildely)
        for k in range(0, len(bobot)):
            tes = lrate * (1 - y[i + 1]) * y[i + 1] * hasildely * x[k]
            deltaw = bobot[k] + tes
            bobotw[i][k] = deltaw
    print("Del Y = ", kdely)
    print("W =", bobotw)
    return bobotw


""" Init Epoch,Input,Output,Hiddden,LRate """
jumlahepoch = 200
inputlayer = len(xtrain[0])
inputlayer
hiddenlayer = 3
outputlayer = 3
lrate = 0.05
# xtrain = [[5.1, 3.5, 1.4, 0.2]]
# ytrain = [0]
""" Create Network 4+(1),3+(1),3 """
network = init_network(inputlayer, hiddenlayer, outputlayer)
network
# network = {'bobot_v': [[0.3,
#                         0.05,
#                         0.1,
#                         0.4],
#                        [0.2,
#                         0.1,
#                         0.3,
#                         0.4],
#                        [0.2,
#                         0.3,
#                         0.1,
#                         0.3]],
#            'bobot_w': [[0.1,
#                         0.2,
#                         0.1,
#                         0.15,
#                         0.2],
#                        [0.3,
#                         0.4,
#                         0.1,
#                         0.3,
#                         0.2],
#                        [0.4,
#                         0.15,
#                         0.25,
#                         0.4,
#                         0.5]]}

tempbobotw = deepcopy(network['bobot_w'])
ydata = []
odata = []
print("Wait - Training")
for epoch in range(1, jumlahepoch + 1):
    print("Epoch Ke - ", epoch)
    for iterasi in range(0, len(xtrain)):
        xdata = list(xtrain[iterasi])
        xdata.insert(0, 1)
        ytarget = ytrain[iterasi]
        target = onehotouput(ytarget)
        print("Data X ", xdata, "Target", ytarget, target)
        print("Feed Forward")
        """ Feed Forward """
        ydata = ffInputHidden(xdata, network['bobot_w'])
        odata = ffHiddenOuput(ydata, network['bobot_v'])
        """ Backward """
        print("Back Backward")
        tempbobotv = deepcopy(network['bobot_v'])
        datadeltaok, network['bobot_v'] = bwOuputHidden(
            ydata, network['bobot_v'], odata, target, lrate)
        network['bobot_w'] = bwHiddenInput(
            xdata, ydata, network['bobot_w'], datadeltaok, tempbobotv, lrate)
        # lrate = 0.5*lrate
    if epoch % 50 == 0:
        print("Epoch Ke = " + str(epoch) + " Selesai")

print()
print("New Weigh After Training")
pp.pprint(network['bobot_w'])
pp.pprint(network['bobot_v'])
print(" --- Training Completed --- ")
""" Testing """
print()
print(" --- Do Testing --- ")
benar = 0
salah = 0
for i in range(0, len(xtest)):
    xdata = list(xtest[i])
    xdata.insert(0, 1)
    ytarget = ytest[i]
    output = onehotouput(ytarget)
    ydata = ffInputHidden(xdata, network['bobot_w'])
    odata = ffHiddenOuput(ydata, network['bobot_v'])
    max_index = odata.index(max(odata))
    result = [0] * 3
    result[max_index] = 1
    if output == result:
        benar = benar + 1
    else:
        salah = salah + 1

prosentase = float("{0:.2f}".format((benar / (benar + salah)) * 100))
print("Total Benar: " + str(benar))
print("Total Salah: " + str(salah))
print("Presentase : " + str(prosentase) + " %")
