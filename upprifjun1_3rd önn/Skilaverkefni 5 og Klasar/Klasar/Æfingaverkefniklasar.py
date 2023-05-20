
'''
livinus felix bassey
Æfingaverkefni í klasar
26.10.2017
'''
#1.Búið til klasa sem nefnist FyrstiKlasi.
#Hafið tvö föll í klasanum. Búið til hlut úr klasanum sem nefnist konni.
#Fyrra fallið í klasanum á að taka inn færibreyturnar nafn og aldur.
#Fallið á að skrifa út textann:“Halló,nafn,þú ert,aldur ,ára gamall“.
#Seinna fallið tekur inn tvær tölur og skrifar út texta sem segir til
#um hvað það eru margar tölur milli þessara tveggja talna.
#Kallið í báðar aðferðirnar og skrifið út niðurstöður.
'''
class MyClass:
    "This is simple class with variable and function"
    a = 10
    def func(self):
        print('Hello')

print('Breytan a í klasanum MyClass hefur gildið', MyClass.a)
print(MyClass)          #<class '__main__.MyClass'>
print(MyClass.func)     #<function MyClass.func at 0x029D42B8>
print(MyClass.__doc__)  #This is simple class with variable and function
hlutur = MyClass()
hlutur.func()

class ComplexNumber:
    a = 1
    def __init__(self, r = 0, i = 0):
        self.real = r
        self.imag = i

    def getData(self):
        print("{0}+{1}j" .format(self.real, self.imag))

c1 = ComplexNumber(2,3)
c1.getData()
c2 = ComplexNumber(5)
c2.getData()
c2.attr = 10
print(c2.real, c2.imag, c2.attr)
#print(c1.attr) er ekki til
del c1.imag
#c1.getData() ekki lengur hægt
c2.getData()
del ComplexNumber.getData
#c2.getData() ekki lengur hægt
ComplexNumber.attr = 3
print(c1.attr, "", c2.attr)
c3 = ComplexNumber(4, 7)
print(c3.real, c3.imag, c3.attr)
c3.imag = 4
print(c3.real, c3.imag, c3.attr)
print(c2.real, c2.imag, c2.attr)
ComplexNumber.real = 8
print(c3.real, c3.imag, c3.attr)
print(c2.real, c2.imag, c2.attr)
del c3
#c3.getData() ekki hægt c3 ekki lengur til
print(c2.a)

'''
#nr.1
class FyrstiKlasi():

    def _init_(self,nafn,aldur):
        self.nafn = nafn
        self.aldur = aldur

    def display(self):
      print('Hallo:',self.name,'þú ert',self.aldur,'ára gamall')

    def math_task(self, math_opr, *arg):
        print( 'það eru margar tölur milli þessara tveggja talna')
konn = FyrstiKlasi('konni','19')

konn.display()
print(konn.nafn)
print(konn.aldur)


#nr.2 Búið til annan klasa sem nefnist AnnarKlasi.
#Þessi klasi á að hafa þrjú föll. Þið ákveðið sjálf hvernig föllin eru.
#Búið til þrjá hluti úr þessum klasa.
#Nefnið hlutina:h1,h2,h3. Sýnið virkni allra hlutanna.
class AnnarKlasi:

    def samlagning(self, a, b):
          return a + b

    def margfoldun(self, a, b):
        return a * b

    def deiling(self, a, b):
        if b == 0:
            return 0
        return a / b

# Prófum klasann og föllin
r1 = AnnarKlasi()
r2 = AnnarKlasi()
r3 = AnnarKlasi()

t1 = int(input('Sláðu inn fyrri tölu: '))
t2 = int(input('Sláðu inn seinni tölu: '))

print('Tölurnar lagðar saman:', r1.samlagning(t1, t2))
print('Tölurnar margfaldaðar saman:', r1.margfoldun(t1, t2))
print('Fyrri talan deilt með þeirri seinni:', round(r1.deiling(t1, t2), 2))

t1 = int(input('Sláðu inn fyrri tölu: '))
t2 = int(input('Sláðu inn seinni tölu: '))

print('Tölurnar lagðar saman:', r2.samlagning(t1, t2))
print('Tölurnar margfaldaðar saman:', r2.margfoldun(t1, t2))
print('Fyrri talan deilt með þeirri seinni:', round(r2.deiling(t1, t2), 2))

t1 = int(input('Sláðu inn fyrri tölu: '))
t2 = int(input('Sláðu inn seinni tölu: '))

print('Tölurnar lagðar saman:', r3.samlagning(t1, t2))
print('Tölurnar margfaldaðar saman:', r3.margfoldun(t1, t2))
print('Fyrri talan deilt með þeirri seinni:', round(r3.deiling(t1, t2), 2))




#nr.3 Búið til þriðja klasann sem þið nefnið ThridjiKlasi.
#Þessi klasi á að hafa smið sem tekur inn tvær tölur.
#Þessi klasi á að hafa þrjú föll. Fyrsta fallið leggur tölurnar saman.
#Annað fallið á að margfalda tölurnar saman.
#Þriðja fallið á að deila seinni töluna upp í þá fyrri.
class ThridjiKlasi:

    def __init__(self, a, b):
        self.tala1 = a
        self.tala2 = b

    def samlagning(self):
        return self.tala1 + self.tala2

    def margfoldun(self):
        return self.tala1 * self.tala2

    def deiling(self):
        if self.tala2 == 0:
            return 0
        return self.tala1 / self.tala2

# Prófum klasann og föllin
t1 = int(input('Sláðu inn fyrri tölu: '))
t2 = int(input('Sláðu inn seinni tölu: '))
reikn = ThridjiKlasi(t1, t2)
print('Tölurnar lagðar saman:', reikn.samlagning())
print('Tölurnar margfaldaðar saman:', reikn.margfoldun())
print('Fyrri talan deilt með þeirri seinni:', round(reikn.deiling(), 2))
'''


