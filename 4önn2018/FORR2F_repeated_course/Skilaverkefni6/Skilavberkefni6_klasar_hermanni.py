'''
livinus felix bassey
Skilaverkefni 6 klasar
12.04.2018
'''
from random import *

herdeildA = []  # Bý til lista
herdeildB = []  # Bý til lista

class Herman:  # Bý til klasa
    def __init__(self, lif, vopn, afl):  # Bý til smið
        self.lif = lif  # lif = random tala á skalanum 1 til 5
        self.vopn = vopn  # vopn = random tala á skalanum 1 til 3
        if vopn == 1:
            self.vopn = "sverd"
        elif vopn == 2:
            self.vopn = "spjot"
        elif vopn == 3:
            self.vopn = "exi"
        self.afl = afl  # afl = random tala á skalanum 1 til 5


        def birta_upplysingar(self):
            print("Líf:", self.lif)


# Klasinn tilbúinn

# búa til 5 hermenn í hvoru liði
for x in range(5):
    h1 = Herman(randint(1,5),randint(1,3),randint(1,5))
    herdeildA.append(h1)

for x in range(5):
    h1 = Herman(randint(1,5),randint(1,3),randint(1,5))
    herdeildB.append(h1)



# Núna þarf að láta þá berjast
# tekur fremsta hermann þur hvorum lista og berð saman afl
# sá sem vinnur fer aftast (.append) í sinn lista (herdeild)
# Þetta er endurtekið þar til allir hermenn í öðru liðnu eru fallnir (listinn er tómur)



print("Herdeild A")
for x in herdeildA:
    print(x.lif, x.vopn, x.afl)

print("Herdeild B")
for x in herdeildB:
    print(x.lif, x.vopn, x.afl)

if herdeildA[0].afl < herdeildB[0].afl:
    herdeildA[0].lif = herdeildA[0].lif-1
    print("herm 1 í herdeild B vann hermann 1 í herdeildA")
elif herdeildA[0].afl > herdeildB[0].afl:
    herdeildB[0].lif = herdeildB[0].lif-1
    print("herm 1 í herdeild A vann hermann 1 í herdeildB")
