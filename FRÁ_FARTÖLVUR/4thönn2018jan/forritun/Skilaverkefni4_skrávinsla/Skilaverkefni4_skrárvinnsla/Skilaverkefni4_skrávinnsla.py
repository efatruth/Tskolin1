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



#2. Hérna er Dæmi 2 sem býr til skrá sem innheldur prímtölurnar upp að 100. :
def primtala():
    plisti = []
    #byrja að finna  prímtölur
    for x in range(1, 100 + 1):
        if x > 1:
            for stak in range(2, x):
                if (x % stak) == 0:
                    break
            else:
                plisti.append(x)
    return plisti

#a. er frá fall sem heitir lesaskrá,

#b.
def listanUR(listann):
    print(listann)

#c
def innihald7(listann):
    teljari = 1
    for x in listann:
        if "7" in str(x):
            print(x )

#d.
def fjodaNr(listann2):
    lista = []
    teljari = 1
    for stak in listann2:
        if teljari % 4 ==0:
            lista.append(stak)
        teljari = teljari+1
    print("Fjórða hvert stak", lista)
    return lista

#e. það er fall sem prentar út skránna í d.



#Hérna er Dæmi 3. forrit sem hefur að býr til skrá sem er með þrjár tuples.
def skraTup(tupla, nafntxt, mode):
    with open(nafntxt, mode, encoding = 'utf-8') as f:
        f.write('(')
        for item in tupla:
            f.write(str(item) + ',')
        #f.write(")")
        # f.write("\n")eða
        f.write(')\n')
#a.
def Tupp(tup1,tup2,tup3):
    for item in tup1,tup2,tup3:
        print(item)

#b.
def falTup(prenTup):
        for i in prenTup:
            print([i])

#c.
def finnaSummu(fyrsTup):
    with open("tupplur.txt", 'r', encoding='utf-8') as f:
        for line in f:
            print(line)
        f.seek(0)
        tuple_text = f.readline()
    summa = 0
    for c in tuple_text:
        if c.isdigit():
            summa = summa + int(c)
    print("Summa tupplu 1 er:",summa)


#a. 4. Hérna er fall sem býr til skrá sem geymir dictionary
def GeymirDict(dict, nafntxt, mode):
    f = open(nafntxt,mode, encoding='utf-8')
    f.write('{')
    for x in dict:
        f.write(str(x) + ":"+ str(dict[x]) +',')
    f.write('}\n')
    f.close()


#b.
def lesaSkraDict(nafntxt):
    skra = open(nafntxt, "r", encoding ="utf-8")
    listi = skra.read().split("\n")
    skra.close()
    listi.pop()
    #print(listi)
    return listi

def skrif(utDict,utDict1):
    for x in utDict,utDict1:
        print([x])

#c.
def nyDict():
    myDict ={}
    for x in range(1,6):
        nafn=input("sladu nafn")
        myDict[x]=nafn
    return myDict


#d.
def eittEinu(dict):
    for i in dict:
        print(i)

on = True
while on:
    print()
    print("1. sléttartölur frá 1 til 1000")
    print("2. prímtölurnar upp að 100")
    print("3. þrjár tuples.")
    print("4. geymir dictionary")
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
        print(primeNums)
        #Write the list primeNums in a file primeNums.txt
        skrifaiSkra(primeNums,"primeNums.txt")

        #a. reading the numbers from primeNums.txt to a list
        print("a")
        primeNr = lesaSkra("primeNums.txt")
        print(primeNr)

        #b. kalla fall sem tekur inn listan úr a og prentar hann út
        print("b.")
        listanUR(primeNr)

        #c. kalla fall sem tekur inn listann úr a og prentar út allar tölur sem innihalda 7
        innihald7(primeNr)

        #d. kalla fall sem tekur inn listann úr a og prentar svo út fjórðu hverja tölu og setjið inn í aðra skrá.
        skrifaiSkra(fjodaNr(primeNr),"fjodaNrskra.txt")

        #e. kalla fall sem prentar út skránna í d.
        print("úr skránni", lesaSkra("fjodaNrskra.txt"))

    elif val == 3:
        #3. kalla fall sem býr til skrá sem er með  þrjár tuples.
        tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
        tuple2 = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
        tuple3 = ('konni', 1234, 'sæll', 'blessaður', 2468)
        skraTup(tuple1, "tupplur.txt", "w")
        skraTup(tuple2, "tupplur.txt", "a")
        skraTup(tuple3, "tupplur.txt", "a")

        #a.
        print("a.")
        print(Tupp(tuple1,tuple2,tuple3))

        # b.
        print("b.")
        # print(falTup(tuple1))

        #c.
        print("c.")
        print(finnaSummu(tuple1))


    elif val == 4:
        # Hérna er Dæmi 4.forrit sem býr til skrá sem geymir dictionary.
        skra_dict = {'konni': 1, 'snorri': 2, 'kalli': 3, 'palli': 4}
        skra_dict1 = nyDict()
        skra_dict2 = nyDict()

        GeymirDict(skra_dict, "dict.txt", "w")
        GeymirDict(skra_dict1, "dict.txt", "a")
        GeymirDict(skra_dict2, "dict.txt", "a")

        #a.
        print("a.")

        #b.
        print("b.")
        mydictFromFile =lesaSkraDict("Dict.txt")
        print(mydictFromFile)
#        print(skrif(skra_dict, skra_dict1))

        #c.
        print("c.")
        #is here above in a

        #d  mydict
        print("d.")
        #print(mydictFromFile[0])

        mydictFromFile[0][-2].replace(",","")
        print(mydictFromFile[0])
#        print(eittEinu(skra_dict, skra_dict1))


