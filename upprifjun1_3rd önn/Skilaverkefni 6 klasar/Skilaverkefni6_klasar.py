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
