# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 19:54:40 2018

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
        self.prev=None
        
        
        
        
#definimos nuestro metodo Push, el cual recibe el dato por el usuario
#como parametro, usamos la variable global de Q,P,R,F, que serán nuestro punteros
#en el caso de F, será nuestro puntero que indica el último nodo agregado
def PushNodox(data):
    global Q
    global P
    global R
    global F
    #crea un nodo nuevo P con el dato del parametro, entonces liga a Q (que
    #se encuentrá en la misma posición de R, de momento) con el nodo nuevo
    #y el nodo nuevo lo liga con Q, además iguala a F con el ultimo nodo ingresado
    #y no lo mueve más
    P=Nodox(data)
    Q.next=P
    #print(Q.data)
    #print(P.data)
    P.prev=Q
    #print(P.prev)
    #print(Q.next)
    Q=P
    F=Q
    
    

R=Nodox("Raíz");
Q=R
F=R
print(R.data)
print(R)
print("\nCapture un dato para el nodo")
dat=input();
PushNodox(dat);
print(Q)
print(Q.data)
print(Q.prev)

print("\nCapture un dato para el nodo")
dat=input();
PushNodox(dat);
print(Q)
print(Q.data)
print(Q.prev)

print("\nCapture un dato para el nodo")
dat=input();
PushNodox(dat);
print(Q)
print(Q.data)
print(Q.prev)

print("\nCapture un dato para el nodo")
dat=input();
PushNodox(dat);
print(Q)
print(Q.data)
print(Q.prev)

print("\nCapture un dato para el nodo")
dat=input();
PushNodox(dat);
print(Q)
print(Q.data)
print(Q.prev)

print("\nCapture un dato para el nodo")
dat=input();
PushNodox(dat);
print(Q)
print(Q.data)
print(Q.prev)