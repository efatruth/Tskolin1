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




for x in range(5):
    h1 = Herman(randint(1,5),randint(1,3),randint(1,5))
    herdeildA.append(h1)

for x in range(5):
    h1 = Herman(randint(1,5),randint(1,3),randint(1,5))
    herdeildB.append(h1)

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
    herdeildB[0].lif = herdeildB[0].afl-1
    print("herm 1 í herdeild A vann hermann 1 í herdeildB")

