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

def randomt(tup):
  dict = {}
  takennumbs = []
  for x in tupla:
     dict[randint(1,21)] = x


  print(dict)


#hérna byrja dæmi 2
#1
def listiNafn(dict, nafn):
    listi=[]
    for x in dict:
        if x in nafn:
            listi.append(dict[x])
    return listi

'''

def stafir(n):

    stafrof = {"a": 1, "b": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11, "m": 12,
               "n": 13, "o": 14, "p": 15, "r": 16, "s": 17, "t": 18, "u": 19, "v": 20, "y": 21}
    list = []
    for x in n:
        list.append(str(stafrof[x]))
    return ' '.join(list)

nafn = input("Sláðu inn nafn:")
print(nafn,"verður",stafir(nafn))
'''


#2 hérna er fall sem tekur inn streng(t.d.nafn) og dictionary úr lið 1 og skilar því í lista.
def streng(nafn,nafn1):
    lista = []
    for x in nafn:
        if x in nafn1:
            lista.append(nafn[x])
    return lista

#3
def names3(n1,n2):
    n1 = stafir(n1)
    n1split = n1.split(" ")

    sum1 = 0
    for x in n1split:
        sum1 = sum1 + int(x)


    n2 = stafir(n2)
    n2split = n2.split(" ")

    sum2 = 0
    for x in n2split:
        sum2 = sum2 + int(x)

    print("summa fyrir nafn1 =","{:.1f}".format(sum1/len(n1split)))
    print("summa fyrir nafn2 =","{:.1f}".format(sum2/len(n2split)))
names3("bob","livinus")

#4
def names(n1,n2):
    n1 = stafir(n1)
    n1split = n1.split(" ")

    sum1 = 0
    for x in n1split:
        sum1 = sum1 + int(x)

    print("name1 = ",sum1)

    n2 = stafir(n2)
    n2split = n2.split(" ")

    sum2 = 0
    for x in n2split:
        sum2 = sum2 + int(x)

    print("name2 = ",sum2)

    if sum1 > sum2:
        print("nafn1 er stærra en nafn2")
    else:
        print("name2 er stærra en nafn1")

names("bob","livinus")



litum_tuple = ('GULUR', 'APPELSÍNUGULUR', 'RAUÐUR', 'GRÆNN', 'BLÁR', 'FJÓLUBLÁR')#dictionaryið er hannið
rand_dict = {1: 'GULUR', 2: 'APPELSÍNUGULUR', 3: 'RAUÐUR', 4: 'GRÆNN', 5: 'BLÁR', 6: 'FJÓLUBLÁR'}

stafrof={"a":1, "b":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8, "j":9, "k":10, "l":11, "m":12, "n":13, "o":14, "p":15, "r":16, "s":17, "t":18, "u":19, "v":20, "y":21}

on = True
while on:
    print("1.")
    print("2.")
    print("3. Hætta")

    val = int(input("Veldu"))
    if val ==1:
        #kalla fall sem skrifar út litina
        litina(litum_tuple)

        #kalla fall sem finnur þá liti sem hafa sex eða fleiri stafi  setur í lista
        print("Litir með fleiri en 6 stafi")
        print(fleiri_staf(litum_tuple))


    elif val ==2:
        print(listiNafn(stafrof, "livinus"))

    elif val == 3:

        break



