'''
livinus felix bassey
05.04.18
timaverkefni3
'''

import random
listi1 = []
listi2 = []
def bua_til_lista(random_min, random_max,fjoldi):
    listi=[]
    fjoldi=200

    for x in range (listi,fjoldi):
        listi.append(random.randint(random_min,random_max))
        listi.append(listi)

        return(listi)

tolulista=bua_til_lista(200,500)

def syna_lista(list):
    print('*'.join())

def summa_og_medaltal(listi):
    summa = sum(listi)
    lengd = len(listi)
    samtalSumma = summa/lengd
    print(round(samtalSumma,3))

def deiling_med_5_og_8(listi):
    for x in range(len(listi)):
        r = listi[x]
        if r % 5 == 0:
            print('im5',listi[x])
        elif r % 8 == 0:
            print('im 8',listi[x])

def skila_bili(listi,fra,til):
    for x in range(fra,til):
        print(listi[x])
        print(x)


bua_til_lista(100,200,300)
syna_lista(listi)
summa_og_medaltal(listi)
deiling_med_5_og_8(listi)
skila_bili(listi,fra,til)

class fyrriKlasi:
    def utreikningur(self,tal1,tal2,tal3,tal4):
        reikna = tal1*tal2*tal3*tal4
        utkoma = reikna/3
        print(round(utkoma,2))

class AnnaKlasi:
    def __init__(self,lid,stig):
        self.nafn_lida = lid
        self.fjoldi_stiga = stig

    def setning(self):


'''
'''
livinus felix bassey
05.04.18
timaverkefni3
'''
the second test after 1st failed one
import random
listiA = []
listiB = []
def bua_til_lista(random_min, random_max,fjoldi=100):
    listi=[]
    for x in range (fjoldi):
        tala = random.randint(random_min, random_max)
        listi.append(tala)
    return(listi)

def syna_lista(listi):
    for x in listi:
        print(x, end = "-")
    print()


def medaltal(listi):
    summa = sum(listi)
    lengd = len(listi)
    print("the sum is",summa)
    samtalSumma = summa/lengd
    return round(samtalSumma,3)

def deiling_med_9_og_15(listi):
    for x in range(len(listi)):
        r = listi[x]
        if r % 9 == 0:
            print('im9',r)
        elif r % 15 == 0:
            print('im 15',r)

def skila_bili(fra,til):
    temp =[]
    for x in range(fra,til):
        temp.append(x)
    return temp


listiA = bua_til_lista(200,300)
listiB = bua_til_lista(50,75,25)

syna_lista(listiA)

medal = medaltal(listiA)
print("meðaltal er:", medal)

deiling_med_9_og_15(listiB)

print(skila_bili(20,41))
print("listann er:", listiB)





#skila_bili(listi1,fra,til)


class fyrstiKlasi:
    def utreikningur(self,tal1,tal2,tal3,tal4):
        reikna = tal1*tal2*tal3*tal4
        utkoma = reikna/3
        print(round(utkoma,2))

class AnnaKlasi:
    def __init__(self,lid,stig):
        self.nafn_lids = lid
        self.fjoldi_stiga = stig

'''
        
