#nr.1
class FyrstiKlasi():
    def __init__(self,nafn,aldur):
        self.nafn = nafn
        self.aldur = aldur

    def display(self):
      print('Hallo:',self.nafn,'þú ert',self.aldur,'ára gamall')

    def math_task(self, tala1,tala2):
        tala = tala1 - tala2
        print( "það eru",tala,"tölur milli þessara tveggja talna")

firstInstance = FyrstiKlasi('konni','19')

firstInstance.display()
firstInstance.math_task(20, 10)
