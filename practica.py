
print('practicando con class')

class Nombres:

    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad



    def persona(self):
        print(f'presentacion \n mi nombre es {self._nombre} {self._apellido} y mi edad es {self._edad}')

    # def get_nombre(self):
    #     return self._nombre

    # esta es otra forma de hacer esta funcion get
    @property
    def nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_apellido(self):
        return self._apellido

    def set_apellido(self, apellido):
        self._apellido = apellido

    def get_edad(self):
        return self._edad

    def set_edad(self, edad):
        self._edad = edad





if __name__ == '__main__':
    persona1 = Nombres('samuel','rodriguez','24')
    persona1.persona()

    #utilizamos el metodo set para modificar los datos
    persona1.set_nombre('juan')
    persona1.set_apellido('matos')
    persona1.set_edad('30')
    persona1.persona()

    # llamando la funcion de @property de manera mas facil sin utilizar set_
    print(f'nombre de la persona es {persona1.nombre}')