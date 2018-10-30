# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 18:59:44 2018

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
                
            

#definimos nuestro metodo pop nodo, el cual, se encargará de eliminar
#un nodo en con una información especifica dada por el usuario, razón
#por la cual, recibe un parametro
def PopNodo(valor):
    #usaremos los punteros Q y P
    global Q
    global P
    #en esta condición sirve primordialmente para que al llegar al ultimo
    #elemento (en el cual, su campo next será igual a None) nos permita
    #revisar si su información es igual a la que el usuario solicita
    #eliminar
    #esta condición se cumplirá en todos los casos hasta llegar al
    #ultimo nodo
    if(Q.next!=None):
        #entonces, asignamos a P el nodo guardado en Q.next
        P=Q.next
        #comparamos el dato que contiene P con el valor del usuario
        if(P.data==valor):
            #de ser iguales, se imprime este mensaje y enseguida
            #se liga a Q con el nodo que se encuentra despues de P
            #entonces, se procede a vacear la info del nodo P
            #asi como eliminar su liga
            print("Se encontró el valor a eliminar!")
            print(P.data)
            Q.next=P.next
            P.data=None
            P.next=None
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
                        
            
        
            
           
#definimos el metodo para borrar la raíz
def PopRaiz():
    #usaremos los punteros de Q y R
    global Q
    global R
    #lo primero es igualar ambos punteros en la misma posición
    Q=R
    #seguido, movemos el puntero de R a al nodo que se encuentra en
    #Q.next, osea, el segundo nodo en la lista
    R=Q.next
    #entonces, imprimimos el siguiente mensaje y luego el dato
    #que será la nueva raíz
    print("\nLa nueva raíz es el siguiente nodo en la lista")
    print(R.data)
    #procedemos a dejar sin liga e información a la antigua raíz,
    #asi como apuntar de nuevo ambos punteros a la raíz nueva para
    #los demás metodos
    Q.next=None
    Q.data=None
    Q=R
    #imprimimos el valor de Q para verificar que, efectivamente
    #la nueva raíz es el que era entonces, el 2do nodo en la lista
    print(Q.data)
    

#definimos el metodo poplast, que eliminará el ultimo nodo ingresado
#en la lista
def PopLast():
    #usaremos los punteros globales de Q y P
    global P
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
            Q.next=None
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
    print("6: Para PEEK mostrador")
    print("7:Para salir")
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
        z=input();
        PushNodox(z)
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
        P=Q
        PopLast();
        Menu();
    if (choice==4):
        #para el pop a un elemento en particular, primero pedimos la entrada
        #del usuario del elemento que desea eliminar de la lista
        print("\nIntroduzca el dato que desea eliminar en la lista")
        valor=input();
        #igualamos nuestros punteros en la misma posición para el
        #recorrido de busqueda y mandamos al metodo el dato del usuario
        #como parametro
        Q=R
        P=Q
        PopNodo(valor);
        Menu();
    if (choice==5):
        #pedimos al usuario la entrada del dato que desea buscar en la lista
        print("\nIntroduzca el dato que desea buscar en la lista")
        valor=input();
        #movemos el puntero Q a la raiz porque desde ahí empezará a hacer las
        #comparaciones y recorrer la lista hasta encontrar o no el dato requerido
        Q=R
        #le enviamos la peticion del usuario al metodo como parametro
        PeekBuscador(valor)
        Menu();
    if (choice==6):
        #antes de ejecutar el metodo peek, movemos el puntero de Q hasta la raíz
        #que es de donde empezará a imprimir los datos de los nodos
        Q=R
        PeekNodox();
        Menu();
    if (choice==7):
        print("Saliendo del programa...")
        
#ejecutamos la clase de nodox y creamos nuestra raíz antes de la
#ejecución del programa, también igualamos los punteros en la raíz creada
R=Nodox("Raíz");
Q=R
print("La raíz se ha creado!\n")
print(Q.data)
Menu();



"""
print(Q.data)
print("\nIntroduzca el dato para el nodo")
z=input();
PushNodox(z)
print(Q.data)
print("\nIntroduzca el dato para el nodo")
z=input();
PushNodox(z)
print((Q.data))
print("\nIntroduzca el dato para el nodo")
z=input();
PushNodox(z)
print(Q.data)
print("\nIntroduzca el dato para el nodo")
z=input();
PushNodox(z)
print(Q.data)
print("\nIntroduzca el dato para el nodo")
z=input();
PushNodox(z)
print(Q.data)










print("\nIntroduzca el dato que desea eliminar en la lista")
valor=input();
Q=R
P=Q
PopNodo(valor);

Q=R
PeekNodox();


Q=R
P=Q
PopLast();
print("Se ejecuto este metodo")

Q=R
PeekNodox();
"""
        
        