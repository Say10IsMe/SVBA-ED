# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 18:09:16 2018

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
            print('La pila se encuentra llena!')
            
            
            
#Ejecutaremos el metodo push 6 veces para llenar la pila y la 6ta nos
#servira para apreciar el mensaje cuando se intenta introducir un valor
#en una pila llena
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
            







