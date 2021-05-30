#program by kevin alvaro

def hitunggenap(dataasli,iterasi=0,panjang=1):
    data=str(dataasli)
    data=list(data)
    panjang=len(data)
    if panjang==iterasi:
        return 0
    ambil=data[iterasi]
    ambil=int(ambil)

    if ambil % 2 ==0:
        return hitunggenap(dataasli,iterasi+1,panjang)+ambil
    else:
        return hitunggenap(dataasli,iterasi+1,panjang)

data=123493684220+8
#2+4+6+8+4+2+2= 36
print(hitunggenap(data)) 
