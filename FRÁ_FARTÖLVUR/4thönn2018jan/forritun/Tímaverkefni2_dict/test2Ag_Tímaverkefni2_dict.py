'''
livinus felix bassey
14.03.2018
Tímaverkefni2
'''

from random import *
#a/b
def litina(liti):
    for x in range(len(liti)):
         print('Litur', x + 1, 'er', liti[x])  # útskrift af litini

#c
def fleiri_staf(lit):
    listi =[]
    for x in lit:
        if len(x) >= 6:
         listi.append(x)
    return listi
#d
tupla = ("RAUÐUR","APPELSÍNUGULUR","GULUR","GRÆNN","BLÁR","FJÓLUBLÁR")
rand_dict = {1: 'GULUR', 2: 'APPELSÍNUGULUR', 3: 'RAUÐUR', 4: 'GRÆNN', 5: 'BLÁR', 6: 'FJÓLUBLÁR'}

def makeDict(tup):
  dict = {}
  takennumbs = []
  for x in tup:
      Nr = randint(1,21)
      dict[Nr] = x
  print(dict)


#hérna byrja dæmi 2
#1. fall sem hefur bókstaf sem key og heiltölu sem value

def listiNafn(dict, nafn):
    listi=[]
    for x in dict:
        if x in nafn:
            listi.append(dict[x])
    return listi


#2 hérna er fall sem tekur inn streng(t.d.nafn) og dictionary úr lið 1 og skilar því í lista.
def streng(dict,nafn1):
    lista = []
    for x in dict:
        if x in nafn1:
            lista.append(dict[x])
    return lista

#3
def names3(listi):
    medaltal = sum(listi)/len(listi)
    return round(medaltal,2)

#4
def names4(dict,n1,n2):
    listi1 = streng(dict,n1)
    listi2 = streng(dict,n2)
    if sum(listi2)> sum(listi1):
        return n2
    else:
        return n1

    #n1 = stafir(n1)
    #n1split = n1.split(" ")
    sum1 = 0
    #for x in n1:
     #   sum1 = sum1 + int(x)

   # print("name1 = ",sum1)

# n2 = stafir(n2)
#n2split = n2.split(" ")
    sum2 = 0
    for x in n2:
        sum2 = sum2 + int(x)
    print("name2 = ",sum2)
    if sum1 > sum2:
        print("nafn1 er stærra en nafn2")
    else:
        print("name2 er stærra en nafn1")

#names4("bob","livinus")




on = True
while on:
    print("1.Tuples fall")
    print("2.Dictionary fall")
    print("3. Hætta")
    val = int(input("Hvað viltu gera"))

    if val ==1:
        litum_tuple = ('GULUR', 'APPELSÍNUGULUR', 'RAUÐUR', 'GRÆNN', 'BLÁR', 'FJÓLUBLÁR')  # dictionaryið er hannið
        #b. kalla fall sem skrifar út litina
        litina(litum_tuple)

        #c. kalla fall sem finnur þá liti sem hafa sex eða fleiri stafi  setur í lista
        print("Litir með fleiri en 6 stafi")
        print(fleiri_staf(litum_tuple))

        #d.
        print(makeDict(tupla))

    elif val ==2:
        #dæmi2. 1
        stafrof = {"a": 1, "b": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11, "m": 12,
                   "n": 13, "o": 14, "p": 15, "r": 16, "s": 17, "t": 18, "u": 19, "v": 20, "y": 21}


        #dæmi2. 2
        print(".2")
        nafnTek1 = input("sladu nafnið þiinn")
        tolurNafn = streng(stafrof, nafnTek1)
        print(tolurNafn)

        #dæmi2. 3
        print(".3")
        print("Meðaltal talnanna er", names3(tolurNafn))

        #dæmi2. 4
        print(".4")
        nafnTek2 = input("sladu nafnið þinn")
        nafnTek3 = input("sladu nafnið þinn")
        print("nafnið með hærri summu er:",names4(stafrof,nafnTek2,nafnTek3))

    elif val == 3:

        break



