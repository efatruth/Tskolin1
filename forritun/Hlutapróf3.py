#livinus felix bassey
#26.04.2017
#hlutapróf3

import random
aftur = "já"
val = 0
while val != 4:

    print("1. skrifa út tölurnar 200-400 í eina línu")
    print("2. vinna með tilviljanakenndar (random)tölur.")
    print("3. vinna með texti (streng)")
    print("4. hæta")
    val = int(input("hvaða lið velurðu ?"))

    print('-----------------------------------')
    
    if val == 1:
        for x in range(200,400+1):
            print(x)


    if val == 2:
        listi = []
        for x in range(50):
            listi.append(random.randint(20,30))
        print("summu talnanna ",(sum(listi),".2f"))
        print(listi.count(20))
        for x in listi:
            if x > 25:
                print(x, end=' ')

        for x in listi:
            if x % 3 == 0:
                print(x, end=' ,')
        print()


    if val == 3:
        print("Núna verður þú beðinn um að skrifa þrjá textinn")
        listi = []
        for x in range(3):
            textinn = input("Skrifaðu inn eitt textinn")
            listi.append(textinn)
        lengstanafn = max(listi,key=len)
        print("Lengsta textinn er =",max(listi, key=len),"og er það",len(lengstanafn),"stafir")
        stafur = input("Veldu einn staf sem er í nafni þínu ")
        print(textinn.replace(stafur, "@",3))
        stafur = input("skrifar textinn")
        print(textinn.count(stafur, 'borða' ,3))
        print()
        


        
        
        

            


        
