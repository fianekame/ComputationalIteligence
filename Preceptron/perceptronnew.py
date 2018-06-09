w0 = 0.3
w1 = 0.2
w2 = 0.4
x0 = 1;
ephoclen = 10;
th = 0.5
# AND
trtable = [[1,1,1],[1,0,0],[0,1,0],[0,0,0]]
# OR --komen diatas lalu unkomen table dibawah--
# trtable = [[1,1,1],[1,0,1],[0,1,1],[0,0,0]]
def changeWeight(we0,we1,we2,restes,value):
    global w0,w1,w2
    if restes > value[2]:
        w0 = we0 - x0
        w1 = we1 - value[0]
        w2 = we2 - value[1]
    elif restes < value[2]:
        w0 = we0 + x0
        w1 = we1 + value[0]
        w2 = we2 + value[1]
    print("===============================================")
    print("Weight w0="+str(w0)+","+"Weight w1="+str(w1)+","+"Weight w2="+str(w2))
    print("===============================================")
    print()

""" Training Proses """
for ephoc in range(0,ephoclen):
    print("Ephoc:"+ str(ephoc))
    for value in trtable:
        restes = 0
        netinput = (x0*w0) + (value[0]*w1) + (value[1]*w2)
        if netinput >= th:
            restes = 1
        print("T:"+str(value))
        print("Hasil Netinput: "+str(netinput))
        print("Hasil Y: "+str(restes))
        changeWeight(w0,w1,w2,restes,value)

""" Testing Proses """
benar = 0
salah = 0
for datates in trtable:
    hasil = 0
    netinput = (x0*w0) + (datates[0]*w1) + (datates[1]*w2)
    if netinput >= th:
        hasil = 1
    if hasil == datates[2]:
        benar += 1
    else:
        salah +=0
    print(datates," Net=",netinput," Hasil=",hasil," Target=",datates[2])
print(benar)
print(salah)
