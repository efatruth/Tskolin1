'''
livinus felix bassey 
12.10.17
'''
    if val == 1:
        print('þú hefur velið verkefni 2\n')
        telja_up = 0
        telja_down = 0
        temptala = 0
        ranlist = [] #þetta er listi fyrir tölur
        for x in range(100):#þetta keyrir 100 sinum
            temptala = randint(200,301)
            ranlist.append(temptala)#þetta er set in lista og kallar eftir random tölu frá 1 up í 500
            if temptala < 235:
                telja_down += 1
            else:
                temptala > 200:
                telja_up += 1
        #þetta þarf aðra forlykkju ekki range til að birta tölunnar
        for i in range(len(ranlist)):
            if i % 3 !=5:
                print(ranlist[i], end="\t")
            else:
                print(ranlist[i])
        print("")

        print("\Heildarsumma talnanna  er =", sum(ranlist))
        print("\meðaltal talan er =",format(sum(ranlist)/len(ranlist),".2f"))
        print("\nfjöldi talna undir 235 er", telja_down)
        print("\fjöldi talna yfir 200 er", telja_up)


elif val == 2:
    with open("hlutaprof.txt ", "r", encoding='utf-8') as f:
         print(f.read())
        
        prof1 = (100;,234)
        prof2 = (123;,345)
        prof3 = (456;,23)
    with open("hlutaprof3.txt ", "", encoding='utf-8') as f:
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
    with open("hlutaprof3.txt",'r',encoding = 'utf-8') as f:
    for line in f:
        print(line)
    summa = 0
    for c in hlutaprof.txt:
        if c.isdigit():
            summa = summa + int(c)
            print(summa)

elif val == 3:
    class KlasiEitt:

    def __init__(self, a, b):
        self.tala1 = a
        self.tala2 = b

    def samlagning(self):
        return self.tala1 + self.tala2

    def deiling(self):
        if self.tala2 == 0:
            return 0
        return self.tala1 / self.tala2

# Prófum klasann og föllin
t1 = int(input('Sláðu inn fyrri tölu: '))
t2 = int(input('Sláðu inn seinni tölu: '))
reikn = KlasiEitt(t1, t2)
print('Tölurnar lagðar saman:', reikn.samlagning())
print('Fyrri talan deilt með þeirri seinni:', round(reikn.deiling(), 2))

class KlasiTvo():

    def _init_(self,reidhjol,tolugirar ):
        self.reidhjol = reidhjol
        self.tolugirar  = tolugirar

    def display(self):
      print('ég er:',self.reidhjol,'og með',self.tolugirar ,'gira')
             
            
    
    
        

    
