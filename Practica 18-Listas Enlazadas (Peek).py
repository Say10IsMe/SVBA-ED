# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 19:03:08 2018

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
        

#definimos nuestro metodo peek, este en particular se encargará de
#mostrar todos datos almacenados en cada nodo en la lista; usamos la
#variable global Q para nuestro puntero
def PeekNodox():
    global Q
    #de entrada, imprimimos el dato de Q (que anteriormente fue movida
    #a la raiz antes de la ejecución del metodo)
    print(Q.data)
    #hacemos la siguiente comparación, que se encargará de asegurarse
    #de que la lista aun tiene nodos, y en caso de no ser así, se 
    #imprimirá el mensaje que aparece en el else
    if (Q.next!=None):
        #la condicion se cumplirá siempre que haya un nodo
        #consecuente al que actcualmente esta apuntando Q
        #entonces,movemos el puntero Q a el nodo que esta ligado a
        #la actual posicion de Q, entonces usamos recursividad
        #para llamar de nuevo al metodo hasta que se termine la lista
        Q=Q.next
        PeekNodox();
    else:
        print("\nSe ha terminado la lista!\n")
        

#para el peek buscador, recibimos como parametro el dato que el usuario
#quiere buscar en la lista enlazada, seguiremos usando la variable Q como puntero
def PeekBuscador(valor):
    global Q
    #la siguiente condición se encarga de verificar si el nodo
    #actual tiene una liga a uno siguiente, de ser así, procede
    #con lo siguiente:
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
                
        
R=Nodox("Raiz")
Q=R
print("La raíz se ha creado!")
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
print((Q.data))
print("Introduzca el dato para el nodo")
z=input();
PushNodox(z)
print(Q.data)

#antes de ejecutar el metodo peek, movemos el puntero de Q hasta la raíz
#que es de donde empezará a imprimir los datos de los nodos
Q=R
PeekNodox();

#pedimos al usuario la entrada del dato que desea buscar en la lista
print("Introduzca el dato que desea buscar en la lista")
valor=input();
#movemos el puntero Q a la raiz porque desde ahí empezará a hacer las
#comparaciones y recorrer la lista hasta encontrar o no el dato requerido
Q=R
#le enviamos la peticion del usuario al metodo como parametro
PeekBuscador(valor)
        
        
