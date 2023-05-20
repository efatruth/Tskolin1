#Livinus felix bassey
#22.4.18
#Lokaverkefni-Hrútuspilinn
from random import *
class Hrutar():
    def __init__(self, nafn, thyngd,mjolk,ulla,afkvema,laris,frjosemi,bak, malir):
        self.nafn=nafn
        self.thyngd=thyngd
        self.mjolk=mjolk
        self.ulla=ulla
        self.afkvema=afkvema
        self.laris=laris
        self.frjosemi=frjosemi
        self.bak=bak
        self.malir=malir
spila=[]
skra = open("hrutastokk.txt","r")
for lina in skra:
    spila.append(lina)
skra.close()

temp = []
hrutastokk = []

for stak in spila:
    temp = stak.split(",")
    hrutastokk.append(Hrutar(temp[0],temp[1],temp[2],temp[3],temp[4],temp[5],temp[6],temp[7],temp[8]))

for x in hrutastokk:
    print(x.nafn, x.thyngd, x.mjolk,x.ulla)


print(hrutastokk[0].nafn)
shuffle(hrutastokk)
print(hrutastokk[0].nafn)
user = []
computer = []
for x in range(26):
    user.append(hrutastokk[x])

for x in range(26,52):
    computer.append(hrutastokk[x])


on = 1
endur = 1
jafntal1 =[]

print("Spil notanda")
print("Nafn:", user[0].nafn)
print("Þyngd", user[0].thyngd)
print("mjolk", user[0].mjolk)
print("ulla", user[0].ulla)
print("afkvema", user[0].afkvema)
print("laris", user[0].laris)
print("frjosemi", user[0].frjosemi)
print("bak", user[0].bak)
print("malir", user[0].malir)
if user[0].thyngd > computer[0].thyngd:
    print("notandi vinnur leikinn")


print("Spil tölva")
print("Nafn:", computer[0].nafn)
print("Þyngd", computer[0].thyngd)
print("mjolk", computer[0].mjolk)
print("ulla", computer[0].ulla)
print("afkvema", computer[0].afkvema)
print("laris", computer[0].laris)
print("frjosemi", computer[0].frjosemi)
print("bak", computer[0].bak)
print("malir", computer[0].malir)



#top card for user or computer is user[0] or computer[0]
#To get the attribute for a card you use user[0].thyngd
while on ==1:
    userlen = len(user)
    complen = len(computer)
    print("user", userlen, "computer",complen)
    endur =1
    # ef notandi vinnur
    if complen <=0:
        print("Notandi vinnur leikinn")
        break
        #ef talvan vinnur
    elif userlen <=0:
        print("talvan vinnur leikinn")
        break
        #ef talva velur flokk
        talvaVal = flokkur(random.randint(1,8))
        print("talva velur flokkin:",talvaVal)

    lotaA = notandi[0].spila(talvaVal,talva[0])
    utkoma(notandi,talvaVal,jafntafli,lota)
    print("fjöldi spila í stokki notanda er",len(user))
    print("fjöldi spila í stokki tölvuna er", len(computer))

    complen = len(computer)
    userlen = len(user)
    print("computer",  complen, "user",userlen)
    if complen <=0:
        print("Notandi vinnur leikinn")
        break
    elif userlen <=0:
        print("talvan vinnur leikinn")
        break
        while endur == 1:
            notandi[0].prenta()
            print("1. þyngd í kilóum")
            print("2. mjölkurlagni dætra")
            print("3. einkunn ullar")
            print("4. fjöldi afkæma")
            print("5. einkunn læris")
            print("6. frjósemi")
            print("7. gerð bakvöðva")
            print("8. einkunn fyrir malir")

            val = random.randint(1,8)
            #talVal = int(input("veldur flokk"))
            #ef notandi velur flokk sem er ekki til
            if val < 1 or val > 8:
                print("Flokkur ekki til")
                endur = 1
            #ef notandi velur flokk sem er til
            else:
                print("fjöldi spila í stokki notanda er", len(user))
                print("fjöldi spila í stokki tölvuna er", len(computer))
                print("þú hefur valið flokkin:", flokkur(val))
                nafnVal = flokkur(val)

            lotaB = notanda[0].spila(nafnVal,talva[0])
            utkoma(notandi,talva,jafntafli,lotaB)
            print("fjöldi spila í stokki notanda er", len(user))
            print("fjöldi spila í stokki tölvuna er", len(computer))
            #endur = 0













