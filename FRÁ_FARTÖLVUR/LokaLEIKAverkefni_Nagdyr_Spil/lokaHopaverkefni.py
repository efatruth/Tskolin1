#livinus felix bassey
#26.04.2017
#Loka hopaverkefni


lidur = 0
while lidur != 10:
    print("1 - Fótboltalið")
    print("2 - Þversumma")
    print("3 - Skæri, blað, steinn")
    print("4 - texti")
    print("5 - heiltolur")
    print("6 - Teningaspilið  Craps")
    print("7 - Þyngadrstuðull")
    print("8 - Teningar")
    print("9 - Byggingaupplýsingar úr Hópverkefni 1 ")
    print("10 - hætta")
    lidur = int(input("hvað viltu byrja"))

    if lidur == 1:
        thattakendur = int(input("slaður inn hvað mikið þáttakanda eru"))
        fjoldi_pr_lid = int(input("sláðu inn fjöldi í hverrju liði"))
        print("Niðurstöður:")
        print("Liðafjölði:" , thattakendur // fjoldi_pr_lid)
        print("varamenn:" , thattakendur % fjoldi_pr_lid )

    elif lidur == 2:
        plus = 0
        innstala = int(input('sláðu heiltölu'))
        
        for x in range(1, innstala+1, 1):
            if x == innstala:
                print(x, end="=")
            else:
                print(x, end="+")
            plus =  plus + x
        
        for x in range(innstala, 0, 1):
            if x == -1:
                print("(", x, ")",end="=")
            else:
                print("(", x, ")",end="+")
            plus =  plus + x
        print(plus)
        

        
    elif lidur == 3:
        summa_jafnt = 0
        summa_notandi_vinnur = 0
        summa_tolva_vinnur = 0
        notandi_velur = 0
        while notandi_velur != 4:
            nafn_notanda = input("Hvað heitirðu")
            aldur_notanda = input("hve gamall ertu")
            print("1. fyrir skeri")
            print("2. fyrir blað")
            print("3. fyrir steinn")
            print("4. fyrir að hætta")
            notandi_velur == input("hvern af þessum liðum viltu velja: ")
            tolvan_velur = random.randint(1,3)
            if tolvan_velur == notandi_velur:
                print("Jafnefli")
                summa_jafnt += 1
            elif tolvan_velur == 1 and notandi_velur == 2:
                print("Tölvan vinnur")
                summa_tolva_vinnur += 1
            elif tolvan_velur == 2:
                print("eftir að setja eitthvað hér")
            elif tolvan_velur == 3:
                print("eftir að setja eitthvað hér")

    elif lidur == 6:
        import random
        teningar1 = random.randint(1,6)
        teningar2 = random.randint(1,6)
        summu_teninga = teningar1 + teningar2
        print("þú kastaðir", summu_teninga)
        if summu_teninga == 7 or  summu_teninga == 11:
            print('þú vannst')
        elif summu_teninga == 2 or  summu_teninga == 3 or  summu_teninga == 12:
            print('þú tapast')
        else:
            print('Reyndu að fá sömu tölu')
            summateninga2 = 0
            while summateninga2 != summu_teninga and summateninga2 !=7:
                teningar1 = random.randint(1,6)
                teningar2 = random.randint(1,6)
                summateninga2 = teningar1 + teningar2
                print("þú kastaðir", summateninga2)
                if summateninga2 == summu_teninga:
                    print('stig leikmanns', summu_teninga)
                elif summateninga2 == 7:
                    print('þú tapast')
                else:
                     print('kastadast aftur')
            

            
    elif lidur == 10:
        print("Takk fyrir að nota forritiö mitt")

    else:
        print("Þú hefur ekki valið rétt")
