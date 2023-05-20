#livinus felix bassey
#17.01.18

val = "já"
while val == 'já': # while lykkju byrja hér  valmynd sem er  endurtekinn.
    print ('1. dæmi,forrit sem spyr um þrjár tölur')
    print ('2. dæmi,forrit sem spyr notanda að nafni og síðan um aldur')
    print ('3. dæmi,forrit sem biður um tölur þar til slegið er inn 0')
    print ('4. dæmi,reiknar yfirborðsflatarmál og rúmmál kúlu út frá radius kúlunnar')
    print ('5. dæmi,forrit sem biður um lykilorð')
    print ('6. dæmi,forrit sem spyr notanda um texta sem slá á inn')
    print ('7. dæmi,forrit sem les inn 2 tölur sem eru stærri en 0')
    val = int(input('hvað viltu gera ?,veludu valmynd - 1,2,3,4,5 eða 0 til að hætta..'))

    if val == 1:
        talnalisti = []
        print("sláður inn þrjar tölur hér fyrir neðan")
        for x in range(3):
            tala = int(input("sláður inn tölu"))
            talnalisti.append(tala)

        if talnalisti.count(tala)==3:
            print("allar tölurnar eru eins")
        else:
            talnalisti.sort()
            #print(talnalisti)
            for x in talnalisti:
                print(x, end=" ")
            print()
                
        
    elif val == 2:
        import datetime
        nafn = input(("hvað heitir þú "))
        aldur = int(input("Hversu gamall ert þú?"))
        nuna = datetime.datetime.now()
        aldurAldamot = (2100 -nuna.year) + aldur
        print(aldurAldamot)
        
        
    elif val == 3:
        nullListi = []
        tala = input("sláður inn tölu og notaðu 0 ef þú vilt breyta")
        while tala !=0:
            nullListi.append(tala)
            tala = input("sláður inn tölu og notaðu 0 ef þú vilt breyta")
            
            summa = sum(nullListi)
            fjtalna = len(nullListi)
            medaltal = summa/fjTalna
            print("Summa talnanna er:", summa,"Fjöldi talna sem slegin var inn:", fjtalna,"medaltal talnanna:",medaltal)

        
        
    elif val == 4:
        import math
        radius = float(input("sláðu inn radíus kúlunnar"))
        flatarmal = (4* math.pi*math.pow(radius,2))
        rummal = (4* math.pow(radius, 3)*math.pi)/3
        print("Yfirborðsflatarmál kúlunnar er:",format(flatarmal, ".5f"))
        print("Rúmmál kúlunar er :",format(rummal, ".2f") )
        
    elif val == 5:
        lykilord = input("sláðu inn lykilord")
        tala = 0
        stafur = 0
        if len(lykilord) == 6:
            for x in lykilord:
                if x.isdigit():
                    tala += 1
                if x.isalpha():
                    stafur += 1
            if tala > 0 and stafur > 0:
                print("Lykilorðið er í lagi")
                print("lykilorð hefur",tala,"tölustafi")
                print("lykilorð hefur",stafur,"bókstafi")
            else:
                print("það verða að vera bæði bókstafir og tölu")
        else:
            print("Röng lengd á lykilorði")
        
    elif val == 6:
        texti = input("sláður inn texti")
        stor = 0
        litill = 0
        for x in texti:
            if x.isupper():
                stor = stor +1
            if x.islower():
                litill = litill+1
        print("í þessum texta eru:", stor,"stórir stafir og ", litill,"litill stafir")
        
    elif val == 7:
        tala1 = int(input("sláðu inn tölu"))
        tala2 = int(input("sláðu inn tölu2"))
        if tala1 == 0 or tala2 ==0:
            print("þú mátt ekki nota 0 í þessum lið")
        else:
            samnefnari = 0
            for x in range(1, 100):
                if tala1 % x == 0 and tala2 % x == 0:
                    samnefnari = x
            print("Fyrri talan:", tala1)
            print("Siðari talan:", tala2)
            print("Stærsti samnefnarinn er:", samnefnari)
    elif val == 8:
        on = 0
    else:
        print("....þakk fyrir....")

                    
        
