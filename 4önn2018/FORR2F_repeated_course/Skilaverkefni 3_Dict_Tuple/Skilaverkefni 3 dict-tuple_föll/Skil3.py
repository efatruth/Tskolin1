import random
'''
livinus felix bassey
19.02.2018
Skilaverkefni 3
'''
#.........Danspörin föll...........#
def prenta_Tuple(tup):
    for x in tup:
        print (x, end=" ")

def paraRod(tup1, tup2):
    for x in range(len(tup1)):
        print(tup1[x], "and", tup2[x])

#?
def paraRandom(tup1, tup2):
    for x in range(len(tup1)):
        print(tup1[random.randint(0,5)], "og", tup2[random.randint(0,5)])

def paraRandomStrakur(tup1, tup2):
    kk = random.sample(tup1,len(tup1))
    kvk = random.sample(tup2,len(tup2))
    for x in range(len(tup1)):
        print(kk[x], "og", kvk[x])
#til

def finnaOllNofn(stafur, tup1, tup2):
    ollNofn=[]
    for x in tup1:
        if stafur in x:
            ollNofn.append(x)
    for x in tup2:
        if stafur in x:
            ollNofn.append (x)
    return ollNofn

def finnaNafn(stafur, tup2):
    nafnalisti=[]
    for x in tup2:
        if stafur == x[0]:
            nafnalisti.append(x)
    return nafnalisti

#?
"""def baedi_tup(nafn1, nafn2):
    nafnlisti3=[]
    for x in nafn1:
        num =
            nafnlisti3.append(x)
    return nafnlisti3

"""


#............föll fyrir Símaskrá..........#

#..........hérna er föll Skráning í bekk........#

tuple_dansherra = ('óláfur', 'ilma', 'viljam', 'danni', 'safi', 'jón')
tuple_domurnar = ('elsa', 'rósa', 'helga', 'sofia', 'erún', 'lovisa')
val = 0
while val != 4:
    print("---------------valmynd------------------")
    print("1. Danspörin.")
    print("2. Símaskrá.")
    print("3. Skráning í bekk.")
    print("4. Hætta.")

    val = int(input("Veldu hvað þu´vilt gera"))
    if val ==1:
        svar = input('hérna á að veludu A,B,C,D')

        if svar.upper() == "A":
            print()
            print("þetta eru dansherrarnir")
            prenta_Tuple(tuple_dansherra)
            print()
            print("þetta eru domurnar")
            prenta_Tuple(tuple_domurnar)
            print()

        elif svar.upper() == "B":
            paraRod(tuple_dansherra,tuple_domurnar)
            print()

        elif svar.upper() == "C":
            paraRandom(tuple_dansherra,tuple_domurnar)
            print()

        elif svar.upper() == "D":
            paraRandomStrakur(tuple_dansherra,tuple_domurnar)
            print()

        elif svar.upper() == "E":
            staf = input("slaðu inn staf")
            print(finnaNafn(staf, tuple_dansherra))
            print(finnaNafn(staf, tuple_domurnar))

        elif svar.upper()== "F":
            staf1 = input("slaðu inn staf")
            print(finnaOllNofn(staf1, tuple_dansherra,tuple_domurnar))

        elif svar.upper() == "G":
            nafn1 = []
            nafn2 = []
            for x in range(len(tup1)):
                print(baedi_tup(nafn1, nafn2))


    elif val ==2:
        pass
    elif val ==3:
        pass
    elif val ==4:
        pass
    else:
        print("Eitthvað rangt valið")
