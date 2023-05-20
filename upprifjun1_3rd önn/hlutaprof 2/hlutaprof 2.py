'''
livinus felix bassey
hlutaprof 2
12.10.17
'''
litum_tuple = ('GULUR','APPELSÍNUGULUR','RAUÐUR','GRÆNN','BLÁR','FJÓLUBLÁR')
for x in range(len(litum_tuple)):
    print('Litur', x+1, 'er', litum_tuple[x])# útskrift af litini
    
for lit in litum_tuple:
    if len(lit) >=6:
        print(lit)
lita_listi = []
for tumlist in range(len(litum_tuple)):
    for tum in range(tumlist+1,len(litum_tuple)):
        lita_listi.append(litum_tuple[tumlist]+'-'+litum_tuple[tum] )
print(lita_listi)

import random
rand_dict = {1:'GULUR',2:'APPELSÍNUGULUR',3:'RAUÐUR',4:'GRÆNN',5:'BLÁR',6:'FJÓLUBLÁR'}
for i in range(21):
   tala = random.randrange(1,21)
   print(tala)
   

bokheil = {' ':0,'A':1,'B':2,'C':3,'D':4,'E':5,'F':6, 'G':7, 'H':8, 'I':9,
           'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17,
           'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25,
           'Z':26}

#tuple_a=('11','14','15','16','17','18','19')
nafn = input('Hað er nafn þinn').upper()
sum_nafn = 0
for c in nafn:
    print(bokheil[c], end=" ")
    sum_nafn = sum_nafn + bokheil[c]# sum_nafn += bokheil[c]
print()

print(nafn, "gefur summuna", sum_nafn)

nafn2 = input('gefðu mér annað nafn ').upper()
sum_nafn2 = 0
for c in nafn2:
    sum_nafn2 = sum_nafn2 + bokheil[c]# sum_nafn += bokheil[c]

if sum_nafn2 > sum_nafn:
    print(nafn2, "er hærri summu en", nafn)
elif sum_nafn2 == sum_nafn:
    print(nafn2, "er með jafnháa summu og", nafn)
else:
    print(nafn2, "er lægri summu en", nafn)

setning_tolur = [8, 1, 12, 12, 15, 0, 8, 5, 9, 13, 21, 18]#[19, 14, 15, 18, 18, 9, 0, 5, 13, 9, 12, 19]
for d in setning_tolur:
    for key, value in bokheil.items():
        if d == value:
            print(key, end="")
print()
