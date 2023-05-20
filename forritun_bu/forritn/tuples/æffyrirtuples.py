'''
livinus felix bassey
26.9.2017
tuples
'''

'''
print('..............valmynd.............')
print('1.tuple með sex stökum')
print('2.tuple innheldur 4 lista')
print('3.tuple innheldur 14 stafi')
print('4.tuple með tölunum(1,2,3,4,5).')
print('5.staf og athugar ')
print('6.hætta ')
print('.......................')
valm=input('veluðu lið')

if valm == '1':
    fyrsta_tuple = (2, 'ole', 'totti', 'sæll', 6, 'hæ')
    print('stak nr.3 er:', fyrsta_tuple[3])

    for x in fyrsta_tuple:
        print(x=":")

'''
# Hreyðraðar tuplur eða nested tuple
n_tuple = ("mús", [8, 4, 6], (1, 2, 3))
print(n_tuple[0][1], n_tuple[0][2])

for i in range(len(n_tuple)):
    for n in range(len(n_tuple[i])):
        print(n_tuple[i][n], end=' ')
    print()

for holf in n_tuple:
    for stak in holf:
        print(stak, end=' ')
    print()


my_tuple = ('p', 'e', 'r', 'm', 'i', 't')
print(my_tuple[:-4])

