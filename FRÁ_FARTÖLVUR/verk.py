
#B�i� til forrit sem prentar allar t�lur � �kve�nu bili, t.d. fr� 10 upp � 100.
#�i� �kve�i� bili� sem er vali�.
for x in range(10,101):
    print(x)
#li�ur 2
#Skrifi� forrit sem les inn tv�r heilt�lur fr� lyklabor�i og prentar �t � skj�inn allar
#t�lur � bilinu � milli talnanna. Prenti� �t � skj�inn villuskilabo� ef engar t�lur
#finnast � bilinu �.e. t�lurnar eru jafn h�ar e�a �nnur a�eins einum h�rri en hin.
tala1=int(input("Sl��u inn t�lu  eitt"))
tala2=int(input("Sl��u inn t�lu tv� .H�n m+a ekki vera l�gri en tala eitt"))
if tala1==tala2:
          print("�essar t�lur eru jafnar")
elif (tala1+1)==tala2:# ef talan er einum h�rri
          print ("�a� eru engar t�lur � milli �essara talna")
else:
          for x in range(tala1,tala2+1):
              print(x)

#li�ur 3
#B�i� til forrit sem skrifar �t allar t�lur � �kve�nu bili fr� byrjunart�lu a� lokat�lu. 
#T.d. ef bili� er fr� 6 upp � 11 eiga a� skrifast �t t�lurnar 6 7 8 9 10 11 � �essari
#R��.  Ef vali� er bili� fr� 11 til 6 � a� skrifast 11 10 9 8 7 6 � �essari r��.
#Notandinn � a� �kve�a hva�a bil er vali�.
tala11=int(input("Sl��u inn t�lu  eitt"))
tala22=int(input("Sl��u inn t�lu tv� .ekki sama tala og tala eitt"))
if tala11 < tala22:
    for x in range(tala11,tala22+1):
        print(x)
else:
    for x in range(tala11,(tala22-1),-1):#byrjar � h�rri t�lunni og endar � l�gri steppar ni�ur
        print(x)

#li�ur 4
#(Oddatolur) B�i� til forrit sem skrifar �t allar oddat�lur � �kve�nu bili. T.d. ef
#bili� er fr� 6 upp � 11 eiga a� skrifast �t t�lurnar 7 9 og 11. Sama myndi skrifast
#�t ef vali� er bili� fr� 7 upp � 12.  Notandinn � a� �kve�a hva�a bil er vali�.
tala11=int(input("Sl��u inn t�lu  eitt"))
tala22=int(input("Sl��u inn t�lu tv� .ekki sama tala og tala eitt"))
if tala11 < tala22:
    for x in range(tala11,tala22+1):
        if x % 2==1:#allar oddat�lur
            print(x)
else:
    for x in range(tala11,(tala22-1),-1):#byrjar � h�rri t�lunni og endar � l�gri steppar ni�ur
        if x % 2==1:#allar oddat�lur
            print(x)

#li�ur 5 anna� veldi
#B�i� til forrit sem prentar allar t�lur � �kve�nu bili
#og hva� talan er � ��ru veldi.
#Til d�mis ef bili� er fr� 2 upp � 4 �� skrifast �t:
tala111=int(input("Sl��u inn t�lu  eitt"))
tala222=int(input("Sl��u inn t�lu tv� .ekki sama tala og tala eitt"))
for x in range(tala111,tala222+1):
    print(x," ",(x*x))

#li�ur 6 
tala3=int(input("Sl��u inn t�lu  eitt"))
tala4=int(input("Sl��u inn t�lu tv� .ekki sama tala og tala eitt"))
summa=0
for x in range(tala3,tala4+1):
    summa=summa+x
    if x < tala4:
        print(x,end="+")#skiptir ekki um l�nu
    else:
        print(x,end="")#�etta � a� gera � s��ast skipti�
        print("=",summa)

#B�i� til forrit sem skrifar �t  margf�ldunart�flu.
tafla=0
magfold=int(input("Hva�a margf�ldunart�flu viltu a� �g birti??"))
if magfold<=10:
    tafla=10
else:
    tafla=magfold
for x in range(tafla+1):#keyrir 10 sinnum
    print(x,"*",magfold,"=",(magfold*x))


'''
#li�ur H
#BMI e�a Body Mass Index er skilgreindur � eftirfarandi h�tt.
#BMI = �yngd � kg / (h�� � metrum)2
#B�i� til forrit sem spyr um h�� � metrum en forriti� s�nir BMI fyrir �essa h��, en fyrir
#�yngdir � milli 60 og 125 kg. �ar sem hlaupi� er � 5 kg. bilum.
haed=float(input("Sl��u inn h�� � metrum"))
print("BMI fyrir �essa h�� er:")
print("�yngd        BMI")
BMI=0
for x in range(60,126,5):#hleypur � 5kg bili
    BMI=x/(haed*haed)
   
    if x<100:
         print(x,"   ",format(BMI,".2f"))
    else:
        print(x,"  ",format(BMI,".2f"))'''





















        
