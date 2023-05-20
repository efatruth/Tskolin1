'''
livinus
'''
'''
f = open("test.txt", 'w', encoding='utf-8')
f.write("þetta er fyrsta linan í skránni\n")
f.close()
'''


with open("skra.txt", 'w', encoding='utf-8')as f:
    f.write("sláðu inn textastreng: Bilbó.txt\n")
    f.write("Bilbo hefur verið skrifaður í skránna skrá.txt 2\n")
    f.write("það eru þrjár línur í þessu skjali\n")

'''with open("skra.txt.txt", 'a', encoding= 'utf-8')as f:
    f.write("bætum þessari linu við\n")
'''

with open("skra.txt",'r', encoding='utf-8')as f:
    print(f. read(4))
    print(f. read(4))
    print("Innihald skrárinnar skrá.txt er Bilbó", f.tell())
    print(f. readline())
    print(f. readlines())
    f.seek(0)
    for line in f:
        print(line,end='')

linulisti = []
with open("test.txt", 'r', encoding='utf-8')as file:
    linulisti = file.readlines()

print(linulisti)
for x in linulisti:
    print(x[3])