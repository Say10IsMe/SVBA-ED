# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 23:17:40 2018

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
            
            
#definimos el metodo poplast, que eliminará el ultimo nodo ingresado
#en la lista
def PopLast():
    #usaremos los punteros globales de Q, P y F
    global P
    global F
    global Q
    #lo que haremos primero, será recorrer los punteros
    #hasta que la condición de Q.next sea igual a none, lo que
    #quiere decir que se ha llegado al ultimo nodo en la lista
    if(Q.next!=None):
        #en esa condición, vamos recorriendo los punteros
        P=Q.next
        #cuando llegamos al ultimo nodo, la siguiente condición se cumple
        #y entonces
        if(P.next==None):
            #se imprime el siguiente mensaje y el dato que será eliminado
            #se procede a quitar la liga y la info almacenada en dicho nodo
            print("\nSe eliminará el ultimo nodo!")
            print(P.data)
            P.data=None
            P.next=None
            P.prev=None
            Q.next=None
            P=Q.next
            F=P
        #cuando el valor de next en P no es none (lo que quiere decir
        #que hay un nodo enseguida, osea que no es el ultimo nodo)
        #entonces se mueve el puntero al siguiente nodo de Q y
        #se usa recursividad para volver a llamar al metodo las 
        #veces necesarias hasta eliminar el ultimo nodo
        else:
            Q=Q.next
            PopLast();


#definimos nuestro menu para el usuario           
def Menu():
    #usaremos las variables globales como punteros
    global Q
    global R
    global P    
    print("\nIntroduzca la opción que desee:)")
    print("1: Para insertar un nodo en la lista")
    print("2: Para hacer POP a la raíz")
    print("3: Para hacer POP al ultimo elemento")
    print("4: Para hacer POP a un elemento en particular")
    print("5: Para PEEK buscador")
    print("6: Para PEEK por la izquierda")
    print("7: Para PEEK por la derecha")
    print("8:Para salir")
    #pedimos la entrada de dato del usuario y la comparamos con el resto
    #de opciones disponibles en el menu
    
    #todas las opciones, al completar la operación, usan recursividad para
    #regresar al menu hasta que el usuario escoja salir, solo en la 
    #opcion 7 no hay recursividad ya que es la salida
    
    choice=int(input());
    if (choice==1):
        #para el push, pedimos el dato que el usuario desea agregar a la lista
        #y mandamos tal dato como parametro al metodo push
        print("\nIntroduzca el dato para el nodo")
        dat=input();
        PushNodox(dat)
        Menu();
    if (choice==2):
        #para la opcion 2, simplemente ejecutamos el metodo e imprimimos el mensaje
        PopRaiz();
        print("Se ha eliminado la raíz predefinida")
        Menu();
    if (choice==3):
        #para el pop al ultimo elemento, primero debemos igualar nuestros
        #punteros en la misma posición (la de R) y entonces podemos ejecutar
        #el metodo sin problema
        Q=R
        PopLast();
        Menu();
    if (choice==4):
        #para el pop a un elemento en particular, primero pedimos la entrada
        #del usuario del elemento que desea eliminar de la lista
        print("\nIntroduzca el dato que desea eliminar en la lista")
        dat=input();
        #igualamos nuestros punteros en la misma posición para el
        #recorrido de busqueda y mandamos al metodo el dato del usuario
        #como parametro
        Q=R
        PopNodo(dat);
        Menu();
    if (choice==5):
        #pedimos al usuario la entrada del dato que desea buscar en la lista
        print("\nIntroduzca el dato que desea buscar en la lista")
        dat=input();
        #movemos el puntero Q a la raiz porque desde ahí empezará a hacer las
        #comparaciones y recorrer la lista hasta encontrar o no el dato requerido
        Q=R
        #le enviamos la peticion del usuario al metodo como parametro
        PeekBuscador(dat)
        Menu();
    if (choice==6):
        #antes de ejecutar el metodo peek, movemos el puntero de Q hasta la raíz
        #que es de donde empezará a imprimir los datos de los nodos
        Q=R
        PeekIzquierda();
        Menu();
        #para leer por la derecha, simplemente llamamos al metodo
        #para hacer dicha lectura y usamos recursividad para volver
        #al menu despues de su ejecución
    if (choice==7):
        PeekDerecha();
        Menu();
        
    if (choice==8):
        print("Saliendo del programa...")
        


#ejecutamos la clase de nodox y creamos nuestra raíz antes de la
#ejecución del programa, también igualamos los punteros en la raíz creada
R=Nodox("Raiz");
Q=R
print("La raíz se ha creado!\n")
print(Q.data)
print(Q)
Menu();
