# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 18:37:03 2018

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
#como parametro, usamos la variable global de Q, que será nuestro puntero
def PushNodox(data):
    global Q
    #c
    #if(Q.next==None):
    #creamos un nodo nuevo llamando a nuestra clase y enviandole el parametro
    #que el usuario anteriormente capturó, entonces al campo de Q.next le
    #asignamos el nuevo nodo creado con el puntero P y seguido, igualamos
    #los punteros en la misma locación de memoria (que es en la que se ha
    #creado nuestro nuevo nodo)
    P=Nodox(data)
    Q.next=P
    Q=P
    #else:
        #Este bloque no se ejecuta por que Q.next nunca será diferente
        #de none, debido a que despues de cada push, inmediatamente
        #movemos Q al nodo nuevo, el cual siempre tendrá por
        #predeterminación el valor de none en su campo next
        #print("Este bloque no se ejecuta")
        

#priermo, creamos nuestra raiz que lleva el dato predefinido de "raiz",
#entonces asignamos el puntero de Q a la locación de memoria a la que apunta
#R
R=Nodox("Raíz")
Q=R
#imprimimos este mensaje para anunciar que la raiz se ha creado y tambien
#imprimimos el valor que hay en esta
print("La raíz se ha creado!")
print(Q.data)

#pedimos al usuario la entrada de datos, mandamos al metodo push la entrada
#del usuario, entonces, el metodo envia el mismo dato al constructor de la
#clase y lo asigna al campo, entonces imprimimos el dato que el usuario recien
#introdujó
print("Introduzca el dato para el nodo")
z=input();
PushNodox(z)
print(Q.data)
print("Introduzca el dato para el nodo")
z=input();
PushNodox(z)
print(Q.data)
print("Introduzca el dato para el nodo")
z=input();
PushNodox(z)
print(Q.data)
print("Introduzca el dato para el nodo")
z=input();
PushNodox(z)
print(Q.data)

"""CODIGO QUE VERIFICA QUE LOS NODOS ESTAN ENLAZADOS
print(R.data)
Q=R
Q=R.next
print(Q.data)
P=Q
P=Q.next
print(P.data)


