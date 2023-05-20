'''
Snorri Emilsson
'''

my_set = {1, 2, 3, 4, 3  }
print(my_set)

print('.................')
my_set = {1.0, "Halló", (1, 2, 3)}
print(my_set)

print('.................')
my_list = [1, 3, 7, 3]
print(my_list)

print('.................')
my_set = set(my_list)
print(my_set)

print('.................')
my_set.add(5)
print(my_set)

print('.................')
my_set.update([1, 2, 3, 4, 5], {6, 7, 8})
print(my_set)

print('.................')
my_set.discard(9)
print(my_set)

print('.................')
my_set.remove(6)
print(my_set)

# prófum að kasta streng í set og fikta í setinu
my_set = set("1FrábærForritari")
print(my_set)
print(sorted(my_set))
print('.................')
print(my_set.pop())

print('.................')
my_set.pop()
print(my_set)

print('.................')
my_set.clear()
del my_set
# print(my_set) #get ekki birt hlut sem er ekki til

print('.................')
# Vinnum með 2 sett (það er hægt aðvera með fleiri)
set_A = {1, 2, 3, 4, 5}
set_B = {4, 5, 6, 7, 8}

print(set_A | set_B)
print(set_A & set_B)
print(set_A.intersection(set_B)) # sama og að ofan með &
print(set_A - set_B)
print(set_B - set_A)
print(set_A.difference(set_B)) # sama og að nota mínus (-)
print(set_A ^ set_B)
print(set_B.symmetric_difference(set_A)) # sama og að nota ^
set_A.difference_update(set_B)
print(set_A)

print('.................')
# Hvað með char?
set_A = set("Frábær")
set_B = set("Forritari")
print(set_A | set_B)
print(set_A & set_B)
print(set_A.intersection(set_B)) # sama og að ofan með &
print(set_A - set_B)
print(set_B - set_A)
print(set_A.difference(set_B)) # sama og að nota mínus (-)
print(set_A ^ set_B)
print(set_B.symmetric_difference(set_A)) # sama og að nota ^
set_A.difference_update(set_B)
print(set_A)

print('.................')
# Hvað með char?
set_A = {"halló", "bless", "dagur"}
set_B = {"bless", "nótt", "velkominn"}
print(set_A | set_B)
print(set_A & set_B)
print(set_A.intersection(set_B)) # sama og að ofan með &
print(set_A - set_B)
print(set_B - set_A)
print(set_A.difference(set_B)) # sama og að nota mínus (-)
print(set_A ^ set_B)
print(set_B.symmetric_difference(set_A)) # sama og að nota ^
set_A.difference_update(set_B)
print(set_A)
