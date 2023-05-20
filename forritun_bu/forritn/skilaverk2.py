#livinus felix bassey
#12.9.2017
#skilaverkefni föll

#fallið farenheit breytir celsius í farenheit
def celcius_farenheit(cels):
    farenheit_celcius =cels * 1.8 +32
    return farenh
#fallið celsius breytir farenheit í celcius
def celcius(farenh):
    cels = (farenh -32)/1.8
    return cels
#hér koma föllin hvert af öðru til dæmis
#celsius_kelvin(celsius):
#kelvin_celsius(kelvin):

#prófum við föllin með því að kalla í þau
val = -1
while val != 0:
    print("valmynd:")
    print("1. breyta celcius í farenheit eða öfugt.")
    print("2. breyta celcius í kelvin eða öfugt.")
    print("3. grunntölur og veldistölur.")
    print("4. tommur og sentimetra.")
    print("5. gallonum í litra.")
    print("6. nafn notanda og  kyn(kk/kvk) ")
    print("7. aðferðina kasta().")
    print("8. aðferð sem tekur inn tvo lista")
    print("0. til að hæta.")
    val = int(input("veldu lið úr valmynd?."))
    #eftir að búið er að taka við vali er farið í viðkomandi lið með if, elif og else
    if val == 1:
        svar = input("vedu a ef þú vilt breyta celcíus í farenheit\n"
                     "eða B ef þú vilt breyta farenheit í celsíus").upper()
        if svar == "A":
            hiti_c = float(input("hvað er hitinn í celcius ?"))
            #kalla í falli celcius_fahrenheit til að reikna
            hiti_f = celcius_fahrenheit (hítí_c)
            print(str(hiti_c) + "°C er" + format(hiti_f .2F) + "°F")
      elif svar == "B":
            hiti_f = float(input("hva er hitinn í farenheit ?"))
            #kalla í fallið fahrenheit celsius til að reikna
            hiti_c = fahrenheit_celsius(hiti_f)
            print(str(hiti_f)+ "°F er " + str(hiti_c)+ "°C")


    elif val == 2:
        print("þú hefur valið lið 2")

        svar = input("veldu A ef þú villt breyta celsius í kelvin\n eða B ef þú villt ")
        
        if svar == "A":
            hiti_c = float(input("hvað er hitinn í celsius?"))
            #kalla í fallið celsius kelvin til að reikna
            hiti_k = celsius_kelvin(hiti_c)
            print(str(hiti_c)+ "°C er " + str(hiti_k) + "°K")
        elif svar == "B":
            hiti_k = float(input("hvað er hitinn í kelvin ?"))
            #kalla í fallið kelvin celsius til að reikna
            hiti_c = kelvin_celsius(hiti_k)
            print(str(hiti_k)+ "°K er " + str(hiti_c) + "°C")

    elif val == 3:..
    



     elif val == 4:
            
            
            
        else:
            #allt annað en A eða B
            print("ég skil ekki")
            #elif val fyrir liði 2 til 8
            #enda á elif == 0 til að hætta og else sem skrifar villubod
        elif val == 0:
            print("takk fyrir að nota forritið.")
        else:
            #allt annað en þegar hefur verið skoðað
        print("þessi liður er ekki til.")
