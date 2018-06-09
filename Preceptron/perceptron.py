w0 = 0.3
w1 = 0.2
w2 = 0.4
x0 = 1;
ephoclen = 9;
trashhold = 0.5
# AND
trtable = [[1,1,1],[1,0,0],[0,1,0],[0,0,0]]
# OR --komen diatas lalu unkomen table dibawah--
# trtable = [[1,1,1],[1,0,1],[0,1,1],[0,0,0]]

def changeWeight(w0,w1,w2,restes,value):
    if restes > value[2]:
        w0 = w0 - x0
        w1 = w1 - value[0]
        w2 = w2 - value[1]
    elif restes < value[2]:
        w0 = w0 + x0
        w1 = w1 + value[0]
        w2 = w2 + value[1]
    else :
        w0 = w0
        w1 = w1
        w2 = w2
    print("===============================================")
    print("Weight w0="+str(w0)+","+"Weight w1="+str(w1)+","+"Weight w2="+str(w2))
    print("===============================================")
    print()

for ephoc in range(0,ephoclen):
    print("Ephoc:"+ str(ephoc))
    for value in trtable:
        restes = 0
        netinput = (x0*w0) + (value[0]*w1) + (value[1]*w2)
        if netinput >= trashhold:
            restes = 1
        print("T:"+str(value))
        print("Hasil Netinput: "+str(netinput))
        print("Hasil Y: "+str(restes))
        changeWeight(w0,w1,w2,restes,value)
#fix some issue
