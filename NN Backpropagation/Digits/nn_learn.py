import sys
import IPython
import numpy as np
import pprint as pp
import sklearn
import matplotlib.pyplot as plt
from IPython.display import display
import random
from copy import deepcopy
from sklearn.datasets import load_digits

""" Load Digit Data """
digits = load_digits()
x, y = digits.data, digits.target

""" Split Data & Get 50 / Class """
indextrain = []
for i in range(0, 10):
    foo_indexes = [n for n, x in enumerate(digits.target) if x == i]
    f = foo_indexes[0:50]
    indextrain = indextrain + f
xtrain, ytrain, xtest, ytest = [], [], [], []
for index in indextrain:
    xtrain.append(digits.data[index])
    ytrain.append(digits.target[index])
c = list(zip(xtrain, ytrain))
xtrain, ytrain = zip(*c)
random.shuffle(c)
xtest = [digits.data[i]
         for i in range(0, len(digits.data)) if i not in indextrain]
ytest = [digits.target[i]
         for i in range(0, len(digits.target)) if i not in indextrain]

""" Init Network """
def init_network(inputlayer, hiddenlayer, outputlayer):
    network = {}
    network['bobot_w'] = [[random.uniform(0.0, 0.001) for i in range(
        inputlayer + 1)] for i in range(hiddenlayer)]
    network['bobot_v'] = [[random.uniform(0.0, 0.001) for i in range(
        hiddenlayer + 1)] for i in range(outputlayer)]
    return network

""" One Hot Encoding """
def onehotouput(ytarget, size=10):
    res = [0] * size
    res[size - ytarget - 1] = 1
    return res

""" Sigmoid Function """
def aktivasi(nilainet):
    return 1.0 / (1.0 + np.exp(-nilainet))

""" ff = FEEDFORWARD PROSES """

""" Compute NetInput Y & Return The Activation Result """
def ffInputHidden(xdata, bobotw):
    y = [1]
    for bobot in bobotw:
        netinput = 0
        for i in range(0, len(xdata)):
            netinput = netinput + (bobot[i] * xdata[i])
        nety = aktivasi(netinput)
        y.append(nety)
    return y


""" Compute NetInput O & Return The Activation Result """
def ffHiddenOuput(ydata, bobotv):
    ok = []
    for bobot in bobotv:
        netinput = 0
        for i in range(0, len(ydata)):
            netinput = netinput + (bobot[i] * ydata[i])
        netok = aktivasi(netinput)
        ok.append(netok)
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
            deltavjk = bobot[j] + (lrate * delok * y[j])
            bobotv[i][j] = deltavjk
    return datadeltaok, bobotv


""" Compute DeltaW For New W Weight """
def bwHiddenInput(x, y, bobotw, datadeltaok, tempbobotv, lrate):
    for i in range(0, len(bobotw)):
        bobot = bobotw[i]
        hasildely = 0
        for j in range(0, len(datadeltaok)):
            hasildely = hasildely + (datadeltaok[j] * tempbobotv[j][i + 1])
        for k in range(0, len(bobot)):
            tes = lrate * (1 - y[i + 1]) * y[i + 1] * hasildely * x[k]
            deltaw = bobot[k] + tes
            bobotw[i][k] = deltaw
    return bobotw


""" Init Epoch,Input,Output,Hiddden,LRate """
jumlahepoch = 400
inputlayer = 64
hiddenlayer = 4
outputlayer = 10
lrate = 0.5

""" Create Network 64+(1),4+(1),10 """
network = init_network(inputlayer, hiddenlayer, outputlayer)

tempbobotw = deepcopy(network['bobot_w'])
ydata = []
odata = []
print("Wait - Training")
for epoch in range(1, jumlahepoch + 1):
    for iterasi in range(0, len(xtrain)):
        xdata = list(xtrain[iterasi])
        xdata.insert(0, 1)
        ytarget = ytrain[iterasi]
        target = onehotouput(ytarget)

        """ Feed Forward """
        ydata = ffInputHidden(xdata, network['bobot_w'])
        odata = ffHiddenOuput(ydata, network['bobot_v'])

        """ Backward """
        tempbobotv = deepcopy(network['bobot_v'])
        datadeltaok, network['bobot_v'] = bwOuputHidden(
            ydata, network['bobot_v'], odata, target, lrate)
        network['bobot_w'] = bwHiddenInput(
            xdata, ydata, network['bobot_w'], datadeltaok, tempbobotv, lrate)

    if epoch % 100 == 0:
        print("Epoch Ke = " + str(epoch) + " Selesai")
print()
print("New Weigh After Training")
# pp.pprint(network['bobot_w'])
# pp.pprint(network['bobot_v'])
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

    result = [0] * 10
    result[max_index] = 1
    if output == result:
        benar = benar + 1
    else:
        salah = salah + 1

prosentase = float("{0:.9f}".format((benar / (benar + salah)) * 100))
print("Total Benar: " + str(benar))
print("Total Salah: " + str(salah))
print("Presentase : " + str(prosentase) + " %")
