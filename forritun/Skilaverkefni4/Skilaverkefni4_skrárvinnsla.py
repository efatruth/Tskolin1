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
    for x in range(1, 100 + 1):
        if x > 1:
            for stak in range(2, x):
                if (x % stak) == 0:
                    break
            else:
                plisti.append(x)
    return plisti



on = True
while on:
    print("1.")
    print("2")

    val = int(input("Hvað viltu gera"))

    if val == 1:
        #Make a list with even numbers and put it into the list evenNumbers
        evenNumbers = slettarTolur(2,101)
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





