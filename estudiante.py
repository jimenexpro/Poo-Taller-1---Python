class Estudiante:
    #Constructor - se ejecuta al crear un objeto
    def __init__(self, nombre, edad, carrera):
        self.nombre=nombre
        self.edad=edad
        self.carrera=carrera
        self.materias=[]
    #metodo para agregar materias 
    def inscribir_materias(self,materia):
        self.materias.append(materia)
        print(f"{self.nombre} se inscrbio en {materia}")
    #metodo para mostrar informacion
    def presentarse(self):
        print(f"Hola, soy {self.nombre}")
        print(f"Tengo {self.edad} años")
        print(f"Estudio {self.carrera}")
        print(f"Materias inscritas: {len(self.materias)}")
    #metodo estudiar
    def estudiar(self,horas):
        print(f"{self.nombre} estudió {horas} horas")
#crear objetos(instancias de la clase)
estudiante1=Estudiante("Ana garcia",20,"Ingenieria de sistemas")
estudiante2=Estudiante("Carlos perez", 22, "Ingenieria de sistemas")
estudiante3=Estudiante("Joan Jimenez", 18, "Ingenieria de sistemas")
#usar los metodos 
estudiante1.presentarse()
print("----")
estudiante1.inscribir_materias("POO")
estudiante1.inscribir_materias("Bases de datos")
print("----")
estudiante2.presentarse()
estudiante2.inscribir_materias("POO")
print("----")
estudiante3.presentarse()
print("----")
estudiante3.inscribir_materias("POO")
estudiante3.inscribir_materias("Bases de datos")
estudiante3.inscribir_materias("Calculo integral")
print("----")
estudiante3.estudiar(5)
