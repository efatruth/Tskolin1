'''
livinus felix bassey
hlutaprof_3
12.12.17
'''


    if val == 1:
        print('þú hefur velið verkefni 2\n')
        telja_up = 0
        telja_down = 0
        temptala = 0
        ranlist = [] #þetta er listi fyrir tölur
        for x in range(200):#þetta keyrir 200 sinum
            temptala = randint(100,201)
            ranlist.append(temptala)#þetta er set in lista og kallar eftir random tölu frá 1 up í 500
            if temptala < 160:
                telja_down += 1
            else:
                temptala > 150:
                telja_up += 1
        #þetta þarf aðra forlykkju ekki range til að birta tölunnar
        for i in range(len(ranlist)):
            if i % 3 !=5:
                print(ranlist[i], end="\t")
            else:
                print(ranlist[i])
        print("")

        print("\Heildarsumma talnanna  er =", sum(ranlist))
        print("\meðaltal talan er =",format(sum(ranlist)/len(ranlist),".3f"))
        print("\nfjöldi talna undir 160 er", telja_down)
        print("\fjöldi talna yfir 150 er", telja_up)


elif val == 3:
    with open("hlutaprof3_auka.txt ", "r", encoding='utf-8') as f:
         print(f.read())
        
        prof1 = (100;,234;,1234)
        prof2 = (123;,345;,234)
        prof3 = (456;,23;,1)
    with open("hlutaprof3_auka.txt ", "", encoding='utf-8') as f:
             f.write('(')
             for item in prof1:
                 f.write(str(item) + ',')
             f.write(')\n(')
             for item in prof2:
                f.write(str(item) + ',')
             f.write(')\n(')
             for item in prof3:
                f.write(str(item) + ',')
             f.write(')')
    with open("þrja_tuple.txt",'r',encoding = 'utf-8') as f:
    for line in f:
        print(line)
    summa = 0
    for c in hlutaprof3_auka.txt:
    if c.isdigit():
       summa = summa + int(c)
print(summa)
             
            
    
    
        

    
