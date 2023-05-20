'''
livinus felix bassey
Skilaverkefni 5 klasar
05.04.2018
'''

# numer1.
import math


class Hringur():
    def __init__(self, r):
        self.radius = r

    def ummal(self):
        return 2 * self.radius * math.pi

    def flatarmal(self):
        return 2 * math.pow(self.radius, 2) * math.pi

    def rummal(self):
        return 3 * (math.pow(self.radius, 3) * math.pi) / 4
class Jofnur():

    def jafna1(self, x):
        return 3 * x + 4 + 2 * x * 3

    def jafna2(self, x, z):
        return (z * 2 + x * 2) * 4

on = True
while on:
    print("1. forrit sem hefur tvo hjálpar klasa. ")
    print("2. klasa sem nefnist Hnit . Klasinn tekur inn x og y hnit í gegnum smiðinn. ")
    val = int(input("Hvað viltu gera"))
    if val == 1:

        # prófa klasann hringur
        rad = float(input("Sláðu inn radius "))
        hringur1 = Hringur(rad)
        print("Ummál hrings", hringur1.ummal())
        print("flatarmal hrings", hringur1.flatarmal())
        print("rummal hrings", hringur1.rummal())

       # prófa klasann Jofnur
        f_x = float(input('sláðu inn gildi x'))
        f_z = float(input('sláðu inn gildi z'))
        j1 = Jofnur()
        print('gildi Y frá jöfnu 1 er:', j1.jafna1(f_x))
        print('gildi Y frá jöfnu 2 er:', j1.jafna2(f_x, f_z))


        # numer2.klasa sem nefnist Hnit
    elif val == 2:
        class Hnit():
            def __init__(self, x, y):
                self.x = x
                self.y = y

            def syna_hnit(self):
                print( "x hnitið er" ,self.x, "og y hnitið er", self.y)

            def stadur(self):
                hluti = ""
                if self.x < 0 and self.y > 0:
                    hluti = "1"
                elif self.x > 0 and self.y > 0:
                    hluti = "2"
                elif self.x < 0 and self.y < 0:
                    hluti = "3"
                elif self.x > 0 and self.y < 0:
                    return hluti


        # profum klasann og föll

        g1 = int(input('Sláðu inn x: '))
        g2 = int(input('Sláðu inn y: '))
        h1 = Hnit(g1,g2)
        h2 = Hnit(-3, 1)
        h1.syna_hnit()
        h2.syna_hnit()
        print("Hnitið er í hluta", h1.stadur())


        print("Hnit 1:")
        print(h1.syna_hnit())
        print("Hnit 2:")
        print(h2.syna_hnit())
        lengd = math.sqrt(abs(h1.x - h2.x) * 2 + abs(h1.y - h2.y) * 2)
        print("Stysta leið milli hnitanna er:", lengd)