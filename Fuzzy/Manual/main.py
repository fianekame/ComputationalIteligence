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
        self.academy = data2tes[0]
        self.relevancy = data2tes[1]
        self.interview = data2tes[2]
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
        self.acad_data = {'high': [3.0,3.0,3.3,3.5], 'vhigh': [3.3,3.5,4.0,4.0]}
        self.rele_data = {'low': [0,0,2,5], 'medium': [2,5,5,8], 'high': [5,8,10,10]}
        self.inte_data = {'low': [0,0,2,5], 'medium': [2,5,5,8], 'high': [5,8,10,10]}
        self.cand_data = {'least': [0,0,2,4], 'less': [2,4,4,6], 'prefer': [4,6,6,8], 'most': [6,8,10,10]}

        self.acad_range = np.arange(3, 4, 0.1)
        self.rele_range = np.arange(0, 11, 1)
        self.inte_range = np.arange(0, 11, 1)
        self.cand_range = np.arange(0, 11, 1)

        self.mew_akademik = {'mhigh':self.findMew(self.academy,self.acad_data['high']),'mvhigh':self.findMew(self.academy,self.acad_data['vhigh'])}
        self.mew_relevansi = {'low':self.findMew(self.relevancy,self.rele_data['low']),'medium':self.findMew(self.relevancy,self.rele_data['medium']),'high':self.findMew(self.relevancy,self.rele_data['high'])}
        self.mew_interview = {'low':self.findMew(self.interview,self.inte_data['low']),'medium':self.findMew(self.interview,self.inte_data['medium']),'high':self.findMew(self.interview,self.inte_data['high'])}

    def newRule(self,ismin,candidate):
        tomin = min(ismin)
        resbawah = []
        if candidate[0] == candidate[1]:
            for x in range(0,11):
                resbawah.append(self.MemberFunc.leftTrapezoid(x,tomin,candidate))
        if candidate[1] == candidate[2]:
            for x in range(0,11):
                resbawah.append(self.MemberFunc.centerTriangular(x,tomin,candidate))
        if candidate[2] == candidate[3]:
            for x in range(0,11):
                resbawah.append(self.MemberFunc.rightTrapezoid(x,tomin,candidate))
        self.allrule.append(resbawah)

    def addRule(self):
        rule1 = self.newRule([self.mew_akademik['mhigh'],self.mew_relevansi['low'],self.mew_interview['low']],self.cand_data['least'])
        rule2 = self.newRule([self.mew_akademik['mhigh'],self.mew_relevansi['low'],self.mew_interview['medium']],self.cand_data['least'])
        rule3 = self.newRule([self.mew_akademik['mhigh'],self.mew_relevansi['low'],self.mew_interview['high']],self.cand_data['less'])
        rule4 = self.newRule([self.mew_akademik['mhigh'],self.mew_relevansi['medium'],self.mew_interview['low']],self.cand_data['least'])
        rule5 = self.newRule([self.mew_akademik['mhigh'],self.mew_relevansi['medium'],self.mew_interview['medium']],self.cand_data['less'])
        rule6 = self.newRule([self.mew_akademik['mhigh'],self.mew_relevansi['medium'],self.mew_interview['high']],self.cand_data['prefer'])
        rule7 = self.newRule([self.mew_akademik['mhigh'],self.mew_relevansi['high'],self.mew_interview['low']],self.cand_data['less'])
        rule8 = self.newRule([self.mew_akademik['mhigh'],self.mew_relevansi['high'],self.mew_interview['medium']],self.cand_data['prefer'])
        rule9 = self.newRule([self.mew_akademik['mhigh'],self.mew_relevansi['high'],self.mew_interview['high']],self.cand_data['prefer'])
        # pp.pprint(allrule)
        rule10 = self.newRule([self.mew_akademik['mvhigh'],self.mew_relevansi['low'],self.mew_interview['low']],self.cand_data['less'])
        rule11 = self.newRule([self.mew_akademik['mvhigh'],self.mew_relevansi['low'],self.mew_interview['low']],self.cand_data['less'])
        rule12 = self.newRule([self.mew_akademik['mvhigh'],self.mew_relevansi['low'],self.mew_interview['medium']],self.cand_data['prefer'])
        rule13 = self.newRule([self.mew_akademik['mvhigh'],self.mew_relevansi['low'],self.mew_interview['high']],self.cand_data['less'])
        rule14 = self.newRule([self.mew_akademik['mvhigh'],self.mew_relevansi['medium'],self.mew_interview['low']],self.cand_data['prefer'])
        rule15 = self.newRule([self.mew_akademik['mvhigh'],self.mew_relevansi['medium'],self.mew_interview['medium']],self.cand_data['most'])
        rule16 = self.newRule([self.mew_akademik['mvhigh'],self.mew_relevansi['medium'],self.mew_interview['high']],self.cand_data['prefer'])
        rule17 = self.newRule([self.mew_akademik['mvhigh'],self.mew_relevansi['high'],self.mew_interview['low']],self.cand_data['most'])
        rule18 = self.newRule([self.mew_akademik['mvhigh'],self.mew_relevansi['high'],self.mew_interview['medium']],self.cand_data['most'])

    def doCompute(self):
        bawahPerRule = np.array(self.allrule)
        # pp.pprint(bawahPerRule)
        agregasi = bawahPerRule.max(axis=0)
        # pp.pprint(agregasi)
        defuz = 0
        atas = 0
        for i in range (0,11):
            atas = atas + (i*agregasi[i])
        defuz = atas / np.sum(agregasi)
        self.endResult['pembilang'] = atas
        self.endResult['penyebut'] = np.sum(agregasi)
        self.endResult['hasil'] = defuz


    def show(self):
        print()
        print("=== Proses Mew Tiap Inputan ===")
        print("Academi:"+str(self.academy)+" | Relevancy:"+str(self.relevancy)+" | Interview:"+str(self.interview))
        print()
        print("=== Proses Mew Tiap Inputan ===")
        # pp.pprint(self.allrule)
        pp.pprint(self.mew_akademik)
        pp.pprint(self.mew_relevansi)
        pp.pprint(self.mew_interview)
        print()
        print("=== Proses Perhitungan Rule Dan Penentuan Agregasi ===")
        # pp.pprint(bawahPerRule)
        # pp.pprint(agregasi)
        print() #ini belum tau apa yang mau ditampilakn disini
        print("=== Proses Hasil Akhir ===")
        pp.pprint(self.endResult)
        print()

myFuzzy = FuzzyLogic([3.1,8,9])
myFuzzy.addRule()
myFuzzy.doCompute()
myFuzzy.show()
