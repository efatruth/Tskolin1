#livinus felix bassey
#17.01.18
#FOR1TÖ05BU –Æfingaverkefni_2 upprfjun

svar = "já" #þertta er sé liður sem ég myndi nota ef þurfti í liðum.
val = "já" # þetta er sé sem reður yfir while lykkjunni.
valmynd = 'já' #breyta sem notu er til að endurtaka while lykkju. 
while val == 'já': # while lykkju byrja hér # valmynd sem er  endurtekinn.
    print ('1. dæmi-fornöfn tveggja einstaklinga og hæð þeirra í sentimetrum.')
    print ('2. dæmi-lengd og breidd reits í metrum.')
    print ('3. dæmi-breidd reits sem er ferhyrningur')
    print ('4. dæmi-skammstöfun áfanga')
    print ('5. dæmi-prósentureiking')
    val = int(input('hvað viltu gera ?,veludu valmynd  - 1,2,3,4,5 eða 0 til að hætta'))

    if val == 1:
        while svar == "já":
            print('þú hefur valið lið 1')
            nafn1 = input("sláður inn fyrra nafnið")
            haed1 = int(input("sláðu inn hæð fyrir einstaklingur"))
            nafn2 = input("sláðu inn seinna nafnið")
            haed2 = int(input("sláður inn hæð seinni einstaklingur"))

            if haed1 < haed2:
                print(nafn2,"er hærri en",nafn1)
            elif haed1> haed2:
                print(nafn1,"er hærri en", nafn2)
            else:
                print(nafn1, "og", nafn2, "eru jafnhá")
                

    if val == 2:
        while svar == "já":
            lengd = int(input('hvar er lengd reitur'))
            breidd = int(input('hvar er breidd hana'))
            reitur = (lengd*breidd)/4046
            print('lengd í metrum:' ,lengd)
            print('breidd í metrum:' ,breidd)
            print('þessi reitur er' ,format(reitur,".3f"))
            svar = input('viltu gera þetta aftur  (já/nei)')
            print ('tákk fyrir')
        print('takk fyrir að nota forritið egðu goðan dag / nótt')

    if val ==3:
        while svar =="já":
            breidd = float(input("Sláðu inn breidd reits í ferhyrningur"))
            print("Breidd fernings í metrum:",breidd)
            print("stærð    Lengd í ekrum")
            ekrum=0
            for x in range(10,201,10):#hleypur á 10 bili
                ekrum=x/(breidd*breidd)
               
                if x<100:
                     print(x,"     ",format(ekrum,".6f"))
                else:
                    print(x,"    ",format(ekrum,".6f"))

            svar = input('viltu gera þetta aftur  (já/nei)')
            print ('tákk fyrir')
        print('takk fyrir að nota forritið egðu goðan dag / nótt')

    if val ==4:
        while svar =="já":
            afanganumer = input("sláðu inn áfanganúmer")
            if len(afanganumer)==7:
                nafn =  afanganumer[0:3]
                if nafn.isalpha() and nafn.isupper():
                    nr =  afanganumer[3:7]
                    if nr.isdigit():
                        print("þetta er rétt Skammstöfun á áfanga ")
                    else:
                        print("siðustu 4 stafirnir eru ekki réttir")
                else:
                     print(afanganumer,"Fyrstu þrir stafirnir eru ekki réttir,skammstöfun þar sem eru ekki hástafir")
            else:
                 print("Lengdin á Skammstöfun er ekki rétt, skammstöfun þar sem það vantar er tölustaf.")

    
    if val ==5:
        while svar =="já":
            heildartala = int(input("Hver er heildin? ?"))
            prosenta = int(input("Hver er % ?"))
            prosent = prosenta/100
            utkoma = heildartala*prosent
            print('Niðurstaðan:',utkoma)

    if val ==6:
        while svar =="já":
            on = 0
        else:
            print("...enda forritun herna.....takk fyrir....")

        
                    

                    
 
