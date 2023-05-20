'''
livinus felix bassey
07.03.18
FORR2FA05BU - SKRÁRVINNSLA_Skilaverkefni_4
'''

#Hérna er dæmi 1:
#1. fall sem býr til skrá sem innheldur allar sléttartölur frá 1 til 1000(gert með for slaufu)
#Makes a list of even numbers
def skrifaiSkra(listi, nafntxt):
    skra = open(nafntxt, "w", encoding ="utf-8" )
    for x in listi:
        skra.write(str(x) + " ")
    skra.close()

#fáll lista fyrir sléttar tölur
def slettarTolur(byrja, enda):
    talnalisti = []
    for x in range(byrja,enda, 2):
        talnalisti.append(x)
    return talnalisti

#a
def lesaSkra(nafntxt):
    skra = open(nafntxt, "r", encoding ="utf-8")
    listi = skra.read().split(" ")
    skra.close()
    listi.pop()
    listi = list(map(int,listi))
    return listi

#b
def reiknaMedaltal(listi):
    print(listi)
    return format(sum(listi) / len(listi), ".2f")

#c
def allarAtta(lis):
    listi2 = []
    for x in lis:
        if x % 8 ==0:
            listi2.append(x)
    return listi2
#d


#e
def prentaTiu(listi):
    teljari = 1
    for x in range(len(listi)):
        if teljari % 10 == 0:
            print(listi[x])
        else:
            print(listi[x], end =" ")
        teljari = teljari +1



#Hérna er Dæmi 2 sem býr til skrá sem innheldur prímtölurnar upp að 100. :
def primtala():
    plisti = []
    #byrja að finna  prímtölur
    for x in range(1, 1000 + 1):
        if x > 1:
            for stak in range(2, x):
                if (x % stak) == 0:
                    break
            else:
                plisti.append(x)
    return plisti


#Hérna Dæmi 3. forrit sem hefur að býr til skrá sem er með  þrjár tuples.

def skraTup(tupla, nafntxt, mode):
    with open(nafntxt, mode, encoding = 'utf-8') as f:
        f.write('(')
        for item in tupla:
            f.write(str(item) + ',')
        #f.write(")")
        # f.write("\n")eða
        f.write(')\n')

def finnaSummu():
    with open("þrja_tuple.txt", 'r', encoding='utf-8') as f:
        for line in f:
            print(line)
        f.seek(0)
        tuple_text = f.readline()
    summa = 0
    for c in tuple_text:
        if c.isdigit():
            summa = summa + int(c)
    print(summa)

    print("summa",sum(new_tuple))

def GeymirDict():
    with open("geymir_dict.txt", 'r', encoding='utf-8') as f:
        print(f.read())

    with open("geymir_dict.txt", "a", encoding='utf-8') as f:
        f.write('\n' + str(skra_dict1) + '\n' + str(skra_dict2))
    # di1 = {}
    # di2 = {}
    # di3 = {}
    with open("geymir_dict.txt", 'r', encoding='utf-8') as f:
        f.seek(0)
        # texti = f.readline()
        # di1 = eval(texti)

on = True
while on:
    print("1. skrá sem innheldur allar sléttartölur frá 1 til 1000")
    print("2. skrá sem innheldur prímtölurnar upp að 100")
    print("3. skrá sem er með  þrjár tuples.")
    print("4. forrit sem býr til skrá sem geymir dictionary")
    val = int(input("Hvað viltu gera"))
    if val == 1:
        #1., Make a list with even numbers and put it into the list evenNumbers
        evenNumbers = slettarTolur(2,1001)
        #Put the list evenNumbers to the file evenNums
        skrifaiSkra(evenNumbers,"evenNums.txt")

        #a., lesum úr skránni og prentum út
        print("a.")
        #Reading all the numbers from the file into slettarSkra,Then print the list
        slettarSkra = lesaSkra("evenNums.txt")
        print("Lesið úr skránni evenNums.txt")
        print(slettarSkra)

        #b.medalTalna
        print("b.")
        #print out the average of the list from the file
        print("meðtalainu er", reiknaMedaltal(slettarSkra))
        print()

        #c. fá lista af tölum sem ganga upp í 8
        print("c.")
        print("Allar tölur sem ganga upp í 8:")
        #Find all the nums that can be divided by 8 and put them in the list allEights
        allEights = allarAtta(slettarSkra)
        print(allEights)

        #d. fall sem tekur listann úr lið c og setið í aðra skrá (sumarslettartolur.txt)
        #Write the list of allEights to a file sumarSlettar.txt
        print("d.")
        skrifaiSkra(allEights,"summersletta.txt")

        #e. fall sem prentar út skrána með bil milli talna og 10 tölur í línu
        print("e.")
        prentaTiu(slettarSkra)
    elif val == 2:
        # make a list of all the prime numbers
        primeNums = primtala()
        #Write the list primeNums in a file primeNums.txt
        skrifaiSkra(primeNums,"primeNums.txt")

        #reading the numbers from primeNums.txt to a list
        primeNr = lesaSkra("primeNums.txt")
        print(primeNr)

    elif val == 3:
        #kalla fall sem býr til skrá sem er með  þrjár tuples.
        tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
        tuple2 = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
        tuple3 = ('konni', 1234, 'sæll', 'blessaður', 2468)
        skraTup(tuple1, "tupplur.text", "w")
        skraTup(tuple2, "tupplur.text", "a")
        skraTup(tuple3, "tupplur.text", "a")

    elif val == 4:
        # Hérna er Dæmi 4.forrit sem býr til skrá sem geymir dictionary.
        skra_dict = {'konni': 1, 'snorri': 2, 'kalli': 3, 'palli': 4}
        skra_dict1 = {'Jón': 2, 'Krístinn': 4, 'Páll': 6, 'Ólafur': 8}
        skra_dict2 = {'james': 5, 'kiki': 6, 'reuben': 7, 'aron': 9}


"""with open("primtolur.txt", 'w', encoding='utf-8') as f:
    for item in listir2:
        f.write(str(item) + ' ')

with open("primtolur.txt", 'r', encoding='utf-8') as f:
    print(f.read())

listir3 = []
"""