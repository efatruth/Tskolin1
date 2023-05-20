'''
livinus felix bassey
Lokaverkefni2
21.11.17
'''
from random import *

# clasinn nagdyr svo hægt sé að búa til mús, hamstur og rottur
class nagdyr:
    def __init__(self,tegund,stadsetning):
        self.tegundin = tegund
        self.stadur = stadsetning
        self.afl = randrange(2, 7, 2)
        
    def upplysingar(self):
        return "nagdyr (" + str(self.tegundin) + ", " + str(self.stadur) + ", " + str(self.aflid) + ")"
    
    def stadsetning(self):
        return self.stadur
    
    def tegund(self):
        return self.tegundin

    def aflid(self):
         return self.afl

    def prenta(self):
        print(self.tegundin,"sem er staðsettur",self.stadur,"og er með",self.afl,"sem afl.")
# end of class nagdyr

umferdir = 0
rottur = []
mus = nagdyr("mus",1)
hamstur = nagdyr("hamstur",randint(2,100))
for x in range(3):
    rottur.append(nagdyr("rotta", randint(2,100)))
print(mus.prenta())
print(hamstur.prenta())
for rotta in rottur:
    rotta.prenta()

while mus.stadur < 100:
    umferdir += 1
    # músin á leik
    teningur = randint(1,6)
    mus.stadur += teningur
    print("músin er núna á reit:", mus.stadur)
    if mus.stadur >= 100:
        break;
    for rotta in rottur:
        if mus.stadur == rotta.stadur:
            print("músin berst við rottu")
            if mus.afl > rotta.afl:
                mus.stadur += mus.afl
            elif rotta.afl > mus.afl:
                mus.stadur -= rotta.afl
            else:
                mus.stadur += mus.afl // 2
                rotta.stadur -=rotta.afl // 2

    if mus.stadur == hamstur.stadur:
        mus.stadur += hamstur.afl

           
    # rottur eiga leik
    for rotta in rottur:
        att = randint(0,1)
        teningur = randint(1,6)
        if att == 0:
            rotta.stadur += teningur
        else:
            rotta.stadur -= teningur
        if mus.stadur == rotta.stadur:
            print("rotta berst við músina")
            if mus.afl > rotta.afl:
                mus.stadur += 2
            elif rotta.afl > mus.afl:
                mus.stadur -= rotta.afl
            else:
                mus.stadur += mus.afl // 2
                rotta.stadur -=rotta.afl // 2

        if rotta.stadur == hamstur.stadur:
            print("rotta hittir hamstur")
            if att == 0:
                rotta.stadur -= 1
                hamstur.stadur += 1
            else:
                rotta.stadur += 1
                hamstur.stadur -= 1

    # hamstur á leik
    teningur = randint(1,6)
    if mus.stadur > hamstur.stadur:
        hamstur.stadur += teningur
    else:
        hamstur.stadur -= teningur
    
    if hamstur.stadur == mus.stadur:
        print("hamsturinn hittir músina og kastar henni áfram")
        mus.stadur += hamstur.afl

    for rotta in rottur:
        if hamstur.stadur == rotta.stadur:
            print("hamsturinn hittir rottu og fer upp, rotta fer niður")
            rotta.stadur -= 1
            hamstur.stadur += 1

    print("nú er músin á reit:", mus.stadur)
    print("nú er hamsturinn á reit:", hamstur.stadur)
    for rotta in rottur:
        print("nú er rotta á reit:", rotta.stadur)

print("Umferðir spilaðar voru:", umferdir)
