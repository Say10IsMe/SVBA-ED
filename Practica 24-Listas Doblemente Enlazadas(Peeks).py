# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 20:07:02 2018

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
    
    
    
#para el metodo de leer por la izquierda, usamos el puntero Q
def PeekIzquierda():
    global Q
    #y hacemos la comparación de si el campo next de Q es diferente de none
    #si lo es, quiere decir que hay un nodo siguiente, entonces imprime el valor
    #actual de Q y mueve el puntero Q al siguiente nodo
    #se usa recursividad para llamar al nodo el numero de veces necesarias
    #hasta que next sea igual a none, lo que quiere decir que se encuentra
    #en el ultimo nodo
    if (Q.next!=None):
        print(Q.data)
        Q=Q.next
        PeekIzquierda();
    #cuando se está en el ultimo nodo, simplemente se imprime la info de este
    #y se imprime el mensaje de que se ha terminado la lista
    else:
        print(Q.data)
        print("La lista se ha terminado:c\n")
        
#para el metodo de leer por la derechaa, usamos el puntero F
def PeekDerecha():
    global F
     #y hacemos la comparación de si el campo prev de F (que esta siempre en
     #el ultimo nodo ingresado) es diferente de none si lo es, quiere decir
     #que hay un nodo anterior, entonces imprime el valor actual de Q 
     #y mueve el puntero F al siguiente nodo 
     #se usa recursividad para llamar al nodo el numero de veces necesarias
     #hasta que prev sea igual a none, lo que quiere decir que se encuentra
     #en el primer nodo, osea, la raiz
    if (F.prev!=None):
        print(F.data)
        F=F.prev
        PeekDerecha();
    #cuando se encuentra en el primer nodo, simplemente imprime la info de
    #este nodo y se imprime el mensaje de que se ha terminado la lista
    else:
        print(F.data)
        print("La lista se ha terminado:P\n")
        
        
#para el peek buscador, recibimos como parametro el dato que el usuario
#quiere buscar en la lista enlazada, seguiremos usando la variable Q como puntero
def PeekBuscador(valor):
    global Q
    #esta condición se encarga de verificar si el nodo
    #actual tiene una liga a uno siguiente que no sea
    #la raíz, de ser así, procede con las instrucciones:
    if(Q.next!=None):
        #comparamos el valor que el usuario quiere buscar en la lista
        #si hay coincidencia, entonces se imprime el mensaje
        #y el valor que se encontró
        if (Q.data==valor):
            print("\nSe encontró la coincidencia!")
            print(Q.data)
        #si no hay coincidencia en el nodo actual al que apunta
        #Q, entonces movemos Q al nodo siguiente y usamos
        #recursividad para ejecutar el metodo el numero de veces
        #necesarias hasta encontrar la coincidencia o no hacerlo
        else:
            Q=Q.next
            PeekBuscador(valor);
    #si en la posicion siguiente del nodo actual no se encuentra nada
    #entonces comparamos el valor del nodo actual (ultimo nodo en la lista)
    #con el dato ingresado
    else:
        #si son iguales, se imprime el mensaje y el dato encontrado
        if (Q.data==valor):
            print("\nSe encontró la coincidencia!\n")
            print(Q.data)
        #de no serlo, se imprime el siguiente mensaje:
        else:
            print("\nNo se encontró coincidendecia:c")





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

Q=R
PeekIzquierda();

PeekDerecha();

print("Busca un dato en la lista")
dat=input();
Q=R
PeekBuscador(dat);
