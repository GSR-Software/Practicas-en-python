import time

print('****Calculadora con funciones***')

def suma():
    print('***Suma***')
    numero1 = int(input('ingresa el numero 1: '))
    numero2 = int(input('ingresa el numero 2: '))
    suma= numero1+numero2
    print(f'el resultado de {numero1}+{numero2} es {suma}\n')

def resta():
    print('***Resta***')
    numero1 = int(input('ingresa el numero 1: '))
    numero2 = int(input('ingresa el numero 2: '))
    resta= numero1-numero2
    print(f'el resultado de {numero1}-{numero2} es {resta}\n')

def multiplicaion():
    print('***Multiplicacion***')
    numero1 = int(input('ingresa el numero 1: '))
    numero2 = int(input('ingresa el numero 2: '))
    multi= numero1*numero2
    print(f'el resultado de {numero1}x{numero2} es {multi}\n')

def division():
    print('***Division***')
    numero1 = int(input('ingresa el numero 1: '))
    numero2 = int(input('ingresa el numero 2: '))
    division= numero1/numero2
    print(f'el resultado de {numero1}/{numero2} es {division}\n')


#programa principal
while True:
    print('Operacion a Realizar\n'
          '1 Suma\n'
          '2 Resta\n '
          '3 Multiplicacion\n'
          '4 Division\n'
          '5 Salir\n')
    seleccion = int(input('Escoje una opcion: '))
    if seleccion ==1:
        suma()
    elif seleccion==2:
        resta()
    elif seleccion ==3:
        multiplicaion()
    elif seleccion ==4:
        division()
    elif seleccion==5:
        break
    else:
        print(f'la opcion {seleccion} no se encuentra porfavor escoje una opcion valida')
        time.sleep(2)