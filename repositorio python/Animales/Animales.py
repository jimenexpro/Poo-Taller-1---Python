class animal:
    def __int__(self):
        self.sonido
        
    def sonido(self):
        print("El animal hace sonidos")

class perro(animal):
    def sonido(self):
        print("El perro hace gua gua")
       
class cerdito(animal):
    def sonido(self):
        print("EL cerdito hace oing oing")
       
class gallina(animal):
    def sonido(self):
        print("La gallina hace cooo")
       
class oveja(animal):
    def sonido(self):
        print("La oveja hace mee")
       
perro.sonido() 
cerdito.sonido()
gallina.sonido()
oveja.sonido()