# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 01:43:45 2018

@author: pc
"""

#creamos la clase que se encargará de construir los nodos con 2 campos
#los cuales serán los del dato a guardar y la liga para el siguiente nodo
class Nodox(object):
    #en el constructor asignamos los valroes iniciales de cada campo,
    #en el caso de data, será un parametro enviado por el usuario
    def __init__(self,data):
        self.data=data
        self.next=None
        

#definimos nuestro metodo Push, el cual recibe el dato por el usuario
#como parametro, usamos las variables globales P y Q, que será nuestro punteros
def PushNodox(data):
    global Q
    global P
    #primero, creamos nuestro nodo y asignamos siempre el puntero P
    #a este nodo nuevo creado, además de que envíamos el dato ingresado
    #por el usuario al constructor de la clase
    P=Nodox(data);
    #luego, ligamos a Q (que en un principio, esta igualada con R)
    #con el nodo creado, el nodo creado (que siempre será P) lo ligamos
    #siempre con R (por que es una lista circular)
    #y para terminar, movemos a Q al nuevo nodo creado
    Q.next=P
    P.next=R
    Q=Q.next
    
        
        
        

#imprimimos este mensaje, creamos la raíz, igualamos los punteros en la
#misma posición e imprimimos al objeto como tal
print("Se ha creado la raíz")
R=Nodox("Raíz");
Q=R
print(Q.data)
print(Q)

#luego, pedimos la entrada del usuario y entonces mandamos el dato
#ingresado al metodo de push
print("\nIntroduzca un dato para la lista")
dat=input();
PushNodox(dat)
#imprimimos el dato del nuevo nodo y para verificar que el ultimo nodo
#esta ligado con la raíz, imprimimos el objeto que esta ligado a P.next
#que en todo caso ,siempre será igual al objeto que se imprimió a la hora
#de crear la raíz de la lista
print(Q.data)
print(P.next)

print("Introduzca un dato para la lista")
dat=input();
PushNodox(dat)
print(Q.data)
print(P.next)

print("Introduzca un dato para la lista")
dat=input();
PushNodox(dat)
print(Q.data)
print(P.next)

print("Introduzca un dato para la lista")
dat=input();
PushNodox(dat)
print(Q.data)
print(P.next)

print("Introduzca un dato para la lista")
dat=input();
PushNodox(dat)
print(Q.data)
print(P.next)
