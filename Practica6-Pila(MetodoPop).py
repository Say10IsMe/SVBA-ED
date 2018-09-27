# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 19:12:39 2018

@author: pc
"""

#Aqui declaramos el arreglo y la variable que definirá el tamaño máximo de
#nuestra pila
pila=[]
numerodatos=5

#Se define el metodo push, el cual se encarga: primero de verificar si la
#actual longitud de la pila es menor a el nuemero maximo da datos permitidos
#y de ser asi, procede a insertar en la pila el valor que es recibido
#como parametro en el metodo push:D
def metodopush(dato):
    if len(pila)<numerodatos:
        pila.append(dato)
        print(pila)
        #en caso de que la longitud de la pila este llena, se desplegará este
        #mensaje
    else:
            print('La pila se encuentra llena!\n')
            
            

print("Introduzca un valor para la pila")
p=input()
metodopush(p);
print("Introduzca un valor para la pila")
p=input()
metodopush(p);
print("Introduzca un valor para la pila")
p=input()
metodopush(p);
print("Introduzca un valor para la pila")
p=input()
metodopush(p);
print("Introduzca un valor para la pila")
p=input()
metodopush(p);
print("Introduzca un valor para la pila")
p=input()
metodopush(p);            
            
#definimos el metodo pop, el cual se encargará de eliminar el ultimo elemento
#intoducido en la pila
def metodopop():
    #primero verifica si la pila tiene elementos para quitar con esta condición
    if len(pila)>0:
        #entonces, imprime el elemento que será borrado, lo borra e imprime
        #de nuevo la pila, para poder apreciar que el ultimo elemento fue
        #sacado de la pila
        print("El valor que será borrado será el:") 
        print(pila[len(pila)-1])
        del (pila[len(pila)-1])
        print(pila)
        #en caso de que la pila no tenga elementos, se desplegará este mensaje
    else:
            print("No se pueden eliminar valores en una pila vacía")
            
#igual que con el metodo push, ejecutaremos el pop 6 veces para dejar vacia
#la pila y la 6ta para ver como se ejecuta el mensaje al tratar de eliminar
#un elemento en una pila vacia
print("\nSe eliminará un elemento de la pila")
metodopop();
print("\nSe eliminará un elemento de la pila")
metodopop();
print("\nSe eliminará un elemento de la pila")
metodopop();
print("\nSe eliminará un elemento de la pila")
metodopop();
print("\nSe eliminará un elemento de la pila")
metodopop();
print("\nSe eliminará un elemento de la pila")
metodopop();




