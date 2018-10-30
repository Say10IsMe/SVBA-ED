# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 17:34:09 2018

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
    
#definimos nuestro metodo peek, este en particular se encargará de
#mostrar todos datos almacenados en cada nodo en la lista y al final
#la raiz; usamos la variable global Q para nuestro puntero
def PeekNodox():
    global Q
    #de entrada, imprimimos el dato de Q (que anteriormente fue movida
    #a la raiz antes de la ejecución del metodo)
    print(Q.data)
    #en la siguiente condición nos checamos que la liga del nodo actual
    #no es la raíz; es decir, que no es el ultimo nodo en la lista,
    if (Q.next!=R):
        #la condicion se cumplirá siempre que haya un nodo
        #consecuente al que actcualmente esta apuntando Q
        #entonces,movemos el puntero Q a el nodo que esta ligado a
        #la actual posicion de Q, entonces usamos recursividad
        #para llamar de nuevo al metodo hasta que se termine la lista
        Q=Q.next
        PeekNodox();
    #cuando hemos alcanzado el utlimo nodo (que es cuando la liga
    #de este apunta a R) imprimimos el dato de R y desplegamos un mensaje
    #de aviso
    else:
        print(R.data)
        print("\nSe ha terminado la lista!\n")
        
        
        
#para el peek buscador, recibimos como parametro el dato que el usuario
#quiere buscar en la lista enlazada, seguiremos usando la variable Q como puntero
def PeekBuscador(valor):
    global Q
    #esta condición se encarga de verificar si el nodo
    #actual tiene una liga a uno siguiente, de ser así, procede
    #con las instrucciones:
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

#igualamos nuestro puntero Q a R para empezar a hacer el recorrido e ir
#imprimiendo los datos de todos los nodos hasta llegar a la raíz
Q=R
PeekNodox();

#pedimos al usuario la entrada del dato que desea buscar en la lista
print("\nIntroduzca el dato que desea buscar en la lista amiguico")
dat=input();
#movemos el puntero Q a la raiz porque desde ahí empezará a hacer las
#comparaciones y recorrer la lista hasta encontrar o no el dato requerido
Q=R
#le enviamos la peticion del usuario al metodo como parametro
PeekBuscador(dat);





















