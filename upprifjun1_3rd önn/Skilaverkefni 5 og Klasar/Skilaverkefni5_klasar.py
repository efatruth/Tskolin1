'''
livinus felix bassey
Skilaverkefni 5 klasar
26.10.2017
'''

#numer1
import math

class Hringur:
    def __init__(self, r):
        self.radius = r        
    
    def ummal(self):
        return 2*self.radius*math.pi
    
    def flatarmal(self):
        return 2*math.pow(self.radius,2)*math.pi

    def rummal(self):
        return 3*(math.pow(self.radius,3)*math.pi)/4

#prófa klasann hringur
rad = float(input("Sláðu inn radius "))
hringur1 = Hringur(rad)
print("Ummál hrings", hringur1.ummal())
print("flatarmal hrings", hringur1.flatarmal())
print("rummal hrings", hringur1.rummal())

class Jofnur:
    
    def jafna1(self, x):
        return 3*x+4+2*x*3 


    def jafna2(self, x, z):
        return (z*2+x*2)*4
    
#prófa klasann Jofnur
f_x =  float(input('sláðu inn gildi x'))
f_z =  float(input('sláðu inn gildi z'))
j1 = Jofnur()
print('gildi Y frá jöfnu 1 er:', j1.jafna1(f_x))
print('gildi Y frá jöfnu 2 er:', j1.jafna2(f_x, f_z))


#numer2
class Hnit:
    def __init__(self, x, y):
        self.stafa1 = x
        self.stafa2 = y
        
    def syna_hnit(self):
        upplysingar = "x hnitið er", self.stafa1,"og y hnitið er", self.stafa2
        return upplysingar

    def stadur(self):
        hluti = ""
        if x < 0 and y > 0:
            hluti = "1"
        elif x > 0 and y > 0:
            hluti = "2"
        elif x < 0 and y < 0:
            hluti = "3"
        elif x > 0 and y < 0:
            
        return hluti 

#profum klasann og föll
g1 = int(input('Sláðu inn fyrsta fjöldi: '))
g2 = int(input('Sláðu inn seinna fjöldi: '))
utgefa = Hnit(g1, g2)
print(utgefa.syna_hnit())
print("Hnitið er í hluta", utgefa.stadur())
h1 = Hnit(3, 7)
h2 = Hnit(-3, 1)
print("Hnit 1:")
print(h1.syna_hnit())
print("Hnit 2:")
print(h2.syna_hnit())
lengd = math.sqrt(abs(h1.stafa1-h2.stafa1)*2 +abs(h1.stafa2-h2.stafa2)*2)
print("Stysta leið milli hnitanna er:", lengd)

    



    

