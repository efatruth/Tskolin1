
with open("slettartolur.txt", 'w', encoding='utf-8') as f:
    for stak in range(2, 1001):
        if stak % 2 == 0:
            f.write(str(stak) + ' ')

listir = []
with open("slettartolur.txt", 'r', encoding='utf-8') as f:
    for line in f:
        print(line)

listir = []
with open("slettartolur.txt", 'r', encoding='utf-8') as f:
    line = f.read()
    line.strip()
    listir = (line.split(' '))
listir.remove('')
listir = list(map(int, listir))
