import time



print('Sistema de login y registro')

user = 'samuel'
password = '123456'
newUser = ''
newPass = ''

while True:
    print('1 login\n'
          '2 Registrarse\n'
          '3 Salir\n')
    opcion = int(input('Que quieres realizar: '))

    if opcion ==1:
        print('Login')
        us = input('Escribe tu usuario: ')
        pas = input('Escribe tu password: ')

        if us == user and pas == password or us == newUser and pas == newPass: # aqui estoy validando si los datos de usuario existente o nuevo usuario son correctos
            print('Iniciando Sesion....\n')
            time.sleep(1)
            print(f'Bienvenido {us}\n')
            print(f'{us} no hay mas nada para mostrar ')
            while True: # estoy creando otro bucles para mantener la secion activa hasta que el usuario quiera salir
                salir = int(input('Quieres salir del sistema 1 SI / 2 NO: '))
                if salir == 1:
                    print('Cerrando Sesion...\n')
                    time.sleep(1)
                    break




        elif us !=user:
            print('Usuario incorrecto')
        elif pas != password:
            print('Password incorrecta')

    elif opcion ==2:
        print('REGISTRO')
        newUser = input('Nuevo usuario: ')
        newPass = input('Nueva password: ')
        print('Realizando el registro...')
        time.sleep(1)
        print('su reistro fue exitoso porfavor inicie sesion')
        time.sleep(3)

    elif opcion==3:
        print('Saliendo del programa... \n'
              'Gracias')
        time.sleep(1)
        break
