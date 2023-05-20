'''
livinus felix bassey
Skilaverkefni 5 klasar
26.10.2017
'''
class Person:
    def _init_(self, n, kt):
        self.nafn = n
        self.kennitala = kt

    def display_person(self):
        print('Nafnið er:', self.nafn)
        print('kennitala er:', self.kennitala)


#profum klasann
n = input('skrauð nafn: ')
kt = input('skrauð kennitala: ')
jonas = person(n, kt)
jonas.nafn = 'Nonni'
#kt:1206582459
#jonas.input_name()
jonas.display_person()
    
