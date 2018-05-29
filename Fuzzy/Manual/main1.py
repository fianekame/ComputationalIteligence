import sys
import IPython
import numpy as np
import pprint as pp
from IPython.display import display
import sklearn
import matplotlib.pyplot as plt
from MembershipFunc import MemberFunc

# import Membership
class FuzzyLogic(object):
    """docstring for FuzzyLogic."""
    def __init__(self, data2tes):
        super(FuzzyLogic, self).__init__()
        self.allrule = [];
        self.endResult = {};
        self.MemberFunc = MemberFunc()
        self.nilai = data2tes[0]
        self.pendapatan = data2tes[1]
        # self.interview = data2tes[2]
        self.fuzzyFucation()

    def findMew(self,x,data):
        res = 0;
        if x <= data[0] or x >= data[3]:
            res = 0
        if data[0] <= x <= data[1]:
            res = (x-data[0]) / (data[1]-data[0])
        if data[1] <= x <= data[2]:
            res = 1
        if data[2] <= x <= data[3]:
            res = (data[3]-x) / (data[3]-data[2])
        return float("{0:.2f}".format(res))

    def fuzzyFucation(self):
        self.nilai_data = {'low': [0,0,0,2], 'medium': [1.5,2.5,2.5,3.5], 'high': [3,4,4,4]}
        self.pendapatan_data = {'low': [0,0,3,5], 'medium': [3,5,5,7], 'high': [5,7,10,10]}
        self.beasiswa_data = {'sedikit': [0,0,1,2], 'banyak': [1,2,3,3]}

        self.nilai_range = np.arange(0, 4, 0.1)
        self.pendapatan_range = np.arange(0, 20, 1)
        self.beasiswa_range = np.arange(0, 5, 1)

        # self.mew_akademik = {'mhigh':self.findMew(self.academy,self.nilai['high']),'mvhigh':self.findMew(self.academy,self.nilai['vhigh'])}
        self.mew_nilai = {'low':self.findMew(self.nilai,self.nilai_data['low']),'medium':self.findMew(self.nilai,self.nilai_data['medium']),'high':self.findMew(self.nilai,self.nilai_data['high'])}
        self.mew_pendapatan = {'low':self.findMew(self.pendapatan,self.pendapatan_data['low']),'medium':self.findMew(self.pendapatan,self.pendapatan_data['medium']),'high':self.findMew(self.pendapatan,self.pendapatan_data['high'])}

    def newRule(self,ismin,candidate):
        tomin = min(ismin)
        resbawah = []
        if candidate[0] == candidate[1]:
            for x in range(0,5):
                resbawah.append(self.MemberFunc.leftTrapezoid(x,tomin,candidate))
        if candidate[1] == candidate[2]:
            for x in range(0,5):
                resbawah.append(self.MemberFunc.centerTriangular(x,tomin,candidate))
        if candidate[2] == candidate[3]:
            for x in range(0,5):
                resbawah.append(self.MemberFunc.rightTrapezoid(x,tomin,candidate))
        self.allrule.append(resbawah)

    def addRule(self):
        rule1 = self.newRule([self.mew_nilai['low'],self.mew_pendapatan['low']],self.beasiswa_data['sedikit'])
        rule2 = self.newRule([self.mew_nilai['medium'],self.mew_pendapatan['medium']],self.beasiswa_data['sedikit'])
        rule3 = self.newRule([self.mew_nilai['high'],self.mew_pendapatan['medium']],self.beasiswa_data['sedikit'])
        rule4 = self.newRule([self.mew_nilai['high'],self.mew_pendapatan['low']],self.beasiswa_data['banyak'])

    def doCompute(self):
        bawahPerRule = np.array(self.allrule)
        # pp.pprint(bawahPerRule)
        agregasi = bawahPerRule.max(axis=0)
        # pp.pprint(agregasi)
        defuz = 0
        atas = 0
        for i in range (0,5):
            atas = atas + (i*agregasi[i])
        defuz = atas / np.sum(agregasi)
        self.endResult['pembilang'] = atas
        self.endResult['penyebut'] = np.sum(agregasi)
        self.endResult['hasil'] = defuz


    def show(self):
        print()
        print("=== Proses Mew Tiap Inputan ===")
        print("nilai:"+str(self.nilai)+" | pendapatan:"+str(self.pendapatan))
        print()
        print("=== Proses Mew Tiap Inputan ===")
        # pp.pprint(self.allrule)
        pp.pprint(self.mew_nilai)
        pp.pprint(self.mew_pendapatan)
        print()
        print("=== Proses Perhitungan Rule Dan Penentuan Agregasi ===")
        # pp.pprint(bawahPerRule)
        # pp.pprint(agregasi)
        print() #ini belum tau apa yang mau ditampilakn disini
        print("=== Proses Hasil Akhir ===")
        pp.pprint(self.endResult)
        print()

myFuzzy = FuzzyLogic([3.5,2.5])
myFuzzy.addRule()
myFuzzy.doCompute()
myFuzzy.show()
