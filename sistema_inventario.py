import time

# funciones del sista


# almacen =  esto es un diccionario donde se agregaran los productos
almacen = [
     {'id':1, 'modelo':'dell 5440','descripcion':'i7 6ta generacion 256ssd y 8Ram','precio':5500,'cantidad':10},
     {'id':2, 'modelo':'dell 5440','descripcion':'i5 4ta generacion 320hdd y 8Ram','precio':4300,'cantidad':3},
     {'id':3, 'modelo':'dell 5440','descripcion':'i7 5ta generacion 500ssd y 16Ram','precio':1000,'cantidad':5},
     {'id':4, 'modelo':'dell 5440','descripcion':'i5 8va generacion 240ssd y 4Ram','precio':1500,'cantidad':1},
]

#Funcion para mostrar el inventario del almacen
def mostrar_almacen():
    for producto in almacen:
        print(f'id = {producto.get('id')} modelo {producto.get('modelo')} descripcion {producto.get('descripcion')} '
              f'precio {producto.get('precio')}cant {producto.get('cantidad')}')


#Funcion para agregar producto al almacen
def agregar_producto():
    print('**agregar producto**')
    id = int(input('id: '))
    modelo = input('modelo: ')
    descripcion = input('descripcion: ')
    precio = float(input('precio: '))
    cant = int(input('cantidad: '))

    anuevo_producto = {'id':id, 'modelo':modelo, 'descripcion':descripcion, 'precio':precio, 'cantidad':cant}
    almacen.append(anuevo_producto)
    print('producto agregado con exito..')
    time.sleep(2) # este time es para que el mensaje del prodcto agregado dure 2 segundos


#funcion para buscar los productos por el id
def buscar_producto_por_id():
    print('Bucardor')
    buscador = int(input('Ingresa el id del producto: '))
    for producto in almacen:
        if producto.get('id') == buscador:
            print('Producto encontrado\n')
            print(f'id: {producto.get('id')} Modelo: {producto.get('modelo')}'
                  f' Descripcion: {producto.get('descripcion')} Precio: {producto.get('precio')} Cant: {producto.get('cantidad')}')
            return

    print('Producto no encontrado')


#funcion para eliminar un producto
def eliminar_producto():
    print('** Eliminar un producto **')
    eliminar = int(input('Ingresa el ID del producto a eliminar: '))
    for producto in almacen:
        if producto.get('id') == eliminar:
            almacen.remove(producto)
            print(f"Producto con ID {eliminar} eliminado con éxito.")
            time.sleep(2)
            return
    print(f"No se encontró ningún producto con ID {eliminar}.")

#programa principal
print('**** Sistema de Inventario *****')

if __name__ == '__main__': #esto es para comprobar que se este ejecutando el programa desde el mismo archivo

    while True:
        print('__Menu__\n'
              '1 Mostrar inventario\n'
              '2 Agregar un producto\n'
              '3 buscar producto por id\n'
              '4 Eliminar un producto\n'
              '5 Salir \n')
        opcion = int(input('Escoje una opcion: '))

        if opcion == 1:
           mostrar_almacen()
        elif opcion ==2:
         agregar_producto()
        elif opcion ==3:
            buscar_producto_por_id()
        elif opcion ==4:
            eliminar_producto()
        elif opcion == 5:
            print('saliendo del sistema...\n !adios!')
            break
        else:
            print('opcion no valida ')






