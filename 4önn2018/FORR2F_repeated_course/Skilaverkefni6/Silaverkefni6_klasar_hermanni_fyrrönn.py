'''
livinus felix bassey
Skilaverkefni 6 klasar
26.10.2017
'''
import random
herdeildA=[] #Bý til lista
herdeildB=[] #Bý til lista
class Hermann: #Bý til klasa
    def __init__(self, lif, vopn, afl, teljari): #Bý til smið
        self.lif = lif
        self.vopn = vopn
        self.afl = afl
        self.teljari = teljari

    def birta_upplysingar(self):
        print("hermadur", self.teljari)
        print("Líf:", self.lif)

# Klasinn tilbúinn

#búa til 5 hermenn í hvoru liði
herdeildA = []
for x in range(5):
    lif = random.randint(1,5) #lif = random tala á skalanum 1 til 5
    vopn = random.randint(1,3) #vopn = random tala á skalanum 1 til 3
    if vopn==1:
        vopn="sverd"
    elif vopn==2:
        vopn="spjot"
    elif vopn==3:
        vopn="exi"
    afl = random.randint(1,5) #afl = random tala á skalanum 1 til 5
    teljari = x + 1
    temp_hermadur = Hermann(lif, vopn, afl, teljari)
    herdeildA.append(temp_hermadur) #bætir hermanninn sem var verið að smíða í lista
    
herdeildB = []
for x in range(5):
    lif = random.randint(1,5) #lif = random tala á skalanum 1 til 5
    vopn = random.randint(1,3) #vopn = random tala á skalanum 1 til 3
    if vopn==1:
        vopn="sverd"
    elif vopn==2:
        vopn="spjot"
    elif vopn==3:
        vopn="exi"
    afl = random.randint(1,5) #afl = random tala á skalanum 1 til 5
    teljari = x + 1
    temp_hermadur = Hermann(lif, vopn, afl, teljari)
    herdeildB.append(temp_hermadur) #bætir hermanninn sem var verið að smíða í lista
    
        
print("Hermenn í hrdeild A:")
for herm in herdeildA:
    herm.birta_upplysingar()
    
print("Hermenn í hrdeild B:")
for herm in herdeildB:
    herm.birta_upplysingar()

# Núna þarf að láta þá berjast
# tekur fremsta hermann þur hvorum lista og berð saman afl
# sá sem vinnur fer aftast (.append) í sinn lista (herdeild)
# Þetta er endurtekið þar til allir hermenn í öðru liðnu eru fallnir (listinn er tómur)



'''
continuation from the question:
#Látið  þessar tvær fylkingar hermanna berjast einn hermann í hvoru liði í einu. Annar hvor hermaðurinn vinnur og ef sá sem tapaði á eftir líf fer hann aftur í herdeidina listann og tveir aðrir hermenn byrja að berjast. Þetta heldur áfram þar til allir hermennirnir í annari herdeildinn eru dauðir.Gott væri að fá að vita hvernig hver bardagi fór.
#Dæmi: hermaður1 í herdeildA tapaði fyrir hermann2 í herdeildB þar sem hermaður2 hafði afl=3 og vopn=spjót en hermaður2 hafðiafl 4 og exi
#Segið hvað margir hermenn eru eftir í sigur liðinu og hvað þeir eigi eftir mörg líf.
#Hannið sjálf leikreglurnar t.d er hægt að láta hermann sem er með afl>=3 og vopn spjót vinna hermann sem er með afl<= 4 og vopn exi.

livinus felix bassey
Skilaverkefni 6 klasar
26.10.2017


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
'''




    
