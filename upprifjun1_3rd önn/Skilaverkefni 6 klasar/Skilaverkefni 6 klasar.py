'''
livinus felix bassey
Skilaverkefni 6 klasar
26.10.2017
'''

from random import *
herdeildA=[] #Bý til lista
herdeildB=[] #Bý til lista
class Herman: #Bý til klasa
    def __init__(self,lif,vopn,afl): #Bý til smið
        lif=randint(1,5) #lif = random tala á skalanum 1 til 5
        vopn=randint(1,3) #vopn = random tala á skalanum 1 til 3
        if vopn==1:
            vopn="sverd"
        elif vopn==2:
            vopn="spjot"
        elif vopn==3:
            vopn="exi"
        afl=randint(1,5) #afl = random tala á skalanum 1 til 5
        if len(herdeildA) < 5: #ef það eru minna en 5 hlutir í listanum
            herdeildA.append(self) #bætir hermanninn sem var verið að smíða í lista
        elif len(herdeildB) < 5: #annars ef það eru minna en 5 hlutir í listanum
            herdeildB.append(self) #bætir hermanninn sem var verið að smíða í lista
            
#Bý til hermenn
hermadur1=Herman(0,0,0) #Set núllin í staðin fyrir lif, vopn og afl
hermadur2=Herman(0,0,0)
hermadur3=Herman(0,0,0)
hermadur4=Herman(0,0,0)
hermadur5=Herman(0,0,0)
hermadur6=Herman(0,0,0)
hermadur7=Herman(0,0,0)
hermadur8=Herman(0,0,0)
hermadur9=Herman(0,0,0)
hermadur10=Herman(0,0,0)
print(herdeildA)
print(herdeildB)
print(hermadur1)

 spjót vinna hermann sem er með afl<= 4 og vopn exi.




    
