# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 17:27:51 2018

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
    #como ingresaremos una serie de numeros, empezando con 1 (que será nuestra
    #raíz) comparamos si el parametro es igual a 1, y de ser así entonces
    #primero creará la raíz, además iguala a Q con la posiciónd de R
    #para las posteriores inserciones
    if (data==1):
        R=Nodox(data)
        Q=R
        print("La raíz ha sido creada!")
        #print(R)
        print(R.data)
    #cuando el dato no es 1, entonces procede con la creación normal
    #de nodos:
    #crea un nodo nuevo P con el dato del parametro, entonces liga a Q (que
    #se encuentrá en la misma posición de R, de momento) con el nodo nuevo
    #y el nodo nuevo lo liga con Q, además iguala a F con el ultimo nodo ingresado
    #y no lo mueve más
    else:
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
def LeerIzquierda():
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
        LeerIzquierda();
    #cuando se está en el ultimo nodo, simplemente se imprime la info de este
    #y se imprime el mensaje de que se ha terminado la lista
    else:
        print(Q.data)
        print("La lista se ha terminado:c\n")
        
#para el metodo de leer por la derechaa, usamos el puntero F
def LeerDerecha():
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
        LeerDerecha();
    #cuando se encuentra en el primer nodo, simplemente imprime la info de
    #este nodo y se imprime el mensaje de que se ha terminado la lista
    else:
        print(F.data)
        print("La lista se ha terminado:P\n")

#para borrar la raíz, usamos los punteros Q y R
def PopRaiz():
    global Q
    global R
    #primero, igualamos a Q con R en la posición
    Q=R
    #entonces, movemos a R al siguiente nodo en la lista
    R=Q.next
    #quitamos la ligas de Q (recordando que aun se encuentra en la posicion
    #de la raiz que esta por ser eliminada) y quitamos el valor que guardaba
    Q.next=None
    Q.prev=None
    Q.data=None
    #igualamos de nuevo Q con la nueva raiz e imprimimos este mensaje
    #y el dato que es la nueva raiz
    Q=R
    print("La nueva raíz es el siguiente nodo en la lista")
    print(R.data)
    



#definimos nuestro metodo pop nodo, el cual, se encargará de eliminar
#un nodo en con una información especifica dada por el usuario, razón
#por la cual, recibe un parametro
def PopNodo(valor):
    #usaremos los punteros Q,P y E
    global Q
    global P
    global E
    #primero comparamos si el valor a borrar es igual a la raíz de nuestra
    #lista, de ser así, se llama al metodo de PopRaíz, si no lo es
    #entonces procede con la eliminacion de nodo normal
    if (valor==1):
        PopRaiz();
    else:
        #primero, compara si el nodo tiene uno siguiente (Q y R se igualan
        #ante de ejecutar el metodo)
        if(Q.next!=None):
            #entonces, asignamos a P el nodo guardado en Q.next
            P=Q.next
            #comparamos el dato que contiene P con el valor del usuario
            if(P.data==valor):
                #de ser iguales, se imprime este mensaje y enseguida
                #se asigna al nodo siguiente de P (el cual, será eliminado)
                #la variable de E, entonces se liga a Q con P.next (osea, el nodo
                #siguiente del que esta por ser liminado) y se liga a dicho nodo
                #con el nodo que se encuentra antes de P
                #entonces, se procede a vacear la info del nodo P
                #asi como eliminar sus ligas
                print("Se encontró el valor a eliminar!")
                print(P.data)
                E=P.next
                Q.next=P.next
                E.prev=Q
                P.data=None
                P.next=None
                P.prev=None
                #si el dato de P no coincide con el valor del usuario, se procede
                #a mover el puntero Q al siguiente nodo y a usar recursividad
                #en el metodo Popnodo para repetir la operación las veces
                #necesarias
            else:
                Q=Q.next
                PopNodo(valor);
            #cuando se alcance el ultimo nodo, simplemente comparamos
            #la información de este con el dato del usuario        
        else:
            #si se cumple tal condición, imprime el valor a eliminar
            #y lo borra
            if(Q.data==valor):
                print("Se encontró el valor a eliminar!")
                print(Q.data)
                del(Q)
                #si no es así, se muestra el siguiente mensaje
            else:
                print("No se encontró coincidencia!")
    
    

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

    
    
#definimos nuestro método para hacer la inserción de los primeros 9 numeros
#naturales, el cual, recibe un parametro:
def Insercion1(data):
    #si dicho parametro es menor que 9 (de entrada es 0) entonces
    #aumenta el valor del parametro en 1 y envía este nuevo valor al
    #metodo de push, además, se usa recursividad para ejecutar el metodo
    #el numero de veces necesarias hasta que se deja de cumplir la condición
    if (data<9):
        data+=1
        PushNodox(data)
        Insercion1(data);
    #cuando ya no se cumple, simplemente muestra este mensaje:
    else:
        print("\nLa inserción de elementos fue hecha!\n")
        
        
print("Primero se hace la inserción de los elementos, incluyendo la raíz\n")
Insercion1(0)

print("\nLuego, leemos por la izquierda la lista\n")
#igualamos los punteros para hacer el recorrido y mostrarlos
Q=R
LeerIzquierda();

print("\nEntonces, leemos por la derecha\n")
LeerDerecha();

print("\nPusheamos un nodo más, el 10\n")
PushNodox(10);
print("\nPusheamos un nodo más, el 11\n")
PushNodox(11);
print("\nPusheamos un nodo más, el 13\n")
PushNodox(13);

print("\nLeemos por la izquierda para ver los cambios\n")
Q=R
LeerIzquierda();


print("\nHacemos pop al 1, osea, la raíz\n")
PopNodo(1);

print("\nLeemos por la izquierda para verificar que se realizó el pop\n")
LeerIzquierda();

#igualamos de nuevo los punteros para hacer el recorrido y buscar el dato
#a eliminar
Q=R
print("\nHacemos pop al dato mandado al metodo\n")
PopNodo(8);

#igualamos los punteros para hacer el recorrido y la impresión de los datos
Q=R
print("\nVolvemos a leer por la izquierda para verificar que se eliminó el 8\n")
LeerIzquierda();

print("\nImprimimos la raíz actual\n")
print(R.data)

print("\nImprimimos el final de la lista por la derecha\n")
print(R.data)

print("\nImprimimos el final de la lista por la izquierda\n")
print(F.data)

#igualamos siempre ambos punteros en la posición para hacer el recorrido y
#buscar el dato solicitado en la lista
Q=R
print("\nBuscamos el 0 en nuestra lista\n")
PeekBuscador(0);

Q=R
print("\nBuscamos el 7 en nuestra lista\n")
PeekBuscador(7);

Q=R
print("\nBuscamos el 8 en nuestra lista\n")
PeekBuscador(8);

Q=R
print("\nBuscamos el 11 en nuestra lista\n")
PeekBuscador(1);



    
"""
R=Nodox(1);
Q=R
print(R.data)

print(Q)

PushNodox(2)
print(P)
print(P.data)

Q=P.prev
print(Q.next)
print(P.prev)
"""