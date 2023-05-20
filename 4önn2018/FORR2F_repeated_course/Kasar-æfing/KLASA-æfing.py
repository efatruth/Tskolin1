#1
class setning():
    def innStreng(self):
        self.strengur = input("slaðu inn strengur")

    def utStreng(self):
        print(self.strengur)

caseSetning = setning()
caseSetning.innStreng()
caseSetning.utStreng()


# #2.

class Adili():
    def __init__(self, nafnin,heiman, email, gsm):
        self.nafnin = nafnin
        self.heiman = heiman
        self. email =  email
        self. gsm = gsm

    def NaVari(self,n):
        pass
    def HeVari(self,h):
        pass
    def EmVari(self,e):
        pass
    def GsVari(self,h):
        pass
adili1= Adili("hækur","7778223","2468934","hækur@hækur.is")
adili2= Adili(" Aron","9933456","8462133","aron@nora.is")
listi=[adili1,adili2]
print(listi[0].nafn)
