import random
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
for litur in range(len(litum_tuple)):
    for para_lit in range(litur+1,len(litum_tuple)):
        lita_listi.append(litum_tuple[litur] + "-" + litum_tuple[para_lit])
print(lita_listi)

rand_dict = {}
lyklar = random.sample(range(1,21), 15)
for i in range(len(lita_listi)):
    rand_dict[lyklar[i]] = lita_listi[i]
print(rand_dict)



bokheil = {' ':0,'A':1,'B':2,'C':3,'D':4,'E':5,'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}

#tuple_a=('11','14','15','16','17','18','19')
nafn = input('Hað er nafn þinn ').upper()
for c in nafn:
     print(bokheil[c])










































































































































































































































































































































































































































'''
{' ':0,'A':2,'R':3,'B':4,'C':5,'F':6}

tuple_a=('11','14','15','16','17','18','19')
nafn = input('Hvað er nafn þinn').upper()
for c in nafn:
     print(bokheil[c], end=" ")
print()
'''
