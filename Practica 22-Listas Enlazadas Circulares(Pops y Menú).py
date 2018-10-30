# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 18:08:13 2018

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
        
        print(Q.next)
        print(R.data)
        print("\nSe ha terminado la lista!\n")
        
        
        
#para el peek buscador, recibimos como parametro el dato que el usuario
#quiere buscar en la lista enlazada, seguiremos usando la variable Q como puntero
def PeekBuscador(valor):
    global Q
    #esta condición se encarga de verificar si el nodo
    #actual tiene una liga a uno siguiente que no sea
    #la raíz, de ser así, procede con las instrucciones:
    if(Q.next!=R):
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
    if(Q.next!=R):
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
                        
            
#nuestro metodo auxiliar nos ayudará a quitar la liga del ultimo nodo
#con la que es ahora la raiz a eliminar:
def Recorrer():
    #usaremos el puntero de Q
    global Q
    #si el nodo Q no esta ligado a nada entonces se asigna al nodo
    #que esta enseguida la variable de Q (esta condición siempre se cumplirá)
    if(Q.next!=None):
        P=Q.next
        #entonces, comparamos si el campo next del nodo es igual a none
        #y de ser así, significa que P esta ubicada en la raiz a eliminar
        #y Q en el ultimo nodo, el cual aun tiene liga con esta raiz
        if(P.next==None):
            #entonces, simplemente enlazamos el ultimo nodo con la raiz nueva
            Q.next=R
        #cuando aun no se llega a los parametros para hacer la nueva liga
        #movemos el puntero de Q al siguiente nodo y usamos recursividad
        #para ejecutar el metodo el numero de veces necesarias hasta
        #enlazar la nueva raiz
        else:
            Q=Q.next
            Recorrer();
    else:
        Q=Q.next
        Recorrer();
        
        
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
    #entonces, cambiamos los campos del nodo Q (que es la raiz a eliminar)
    #a los siguientes; quitamos la liga del nodo con el siguiente
    Q.data="Vacio"
    Q.next=None
    #nuevamente igualamos los punteros en la nueva raiz y ejecutamos nuestro
    #metodo auxiliar:
    Q=R
    Recorrer();
    
    #entonces, imprimimos el siguiente mensaje y luego el dato
    #que será la nueva raíz
    print("\nLa nueva raíz es el siguiente nodo en la lista")
    print(R.data)    
    #procedemos a dejar sin liga e información a la antigua raíz,
    #asi como apuntar de nuevo ambos punteros a la raíz nueva para
    #los demás metodos
    #Q.next=None
    #Q.data=None    
           
    #imprimimos el valor de Q para verificar que, efectivamente
    #la nueva raíz es el que era entonces, el 2do nodo en la lista
    print(R)
    

#definimos el metodo poplast, que eliminará el ultimo nodo ingresado
#en la lista y ligará el nodo antecesor a este a la raíz
def PopLast():
    #usaremos los punteros globales de Q y P
    global P
    global Q
    #lo que haremos primero, será recorrer los punteros
    #hasta que la condición de Q.next sea igual a R, lo que
    #quiere decir que se ha llegado al ultimo nodo en la lista
    #(recordando que es una lista circular, por lo tanto
    #el ultimo nodo siempre estará ligado a R)
    if(Q.next!=None):
        #en esa condición, vamos recorriendo los punteros
        P=Q.next
        #cuando llegamos al ultimo nodo, la siguiente condición se cumple
        if(P.next==R):
            #se imprime el siguiente mensaje y el dato que será eliminado
            #se procede a elimiar la info que contenía este nodo y 
            #el nodo anterior a este obtiene la liga a la raíz
            print("\nSe eliminará el ultimo nodo!")
            print(P.data)
            P.data=None
            Q.next=R
        #cuando el valor de next en P no es R (lo que quiere decir
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
        PeekNodox();
        Menu();
    if (choice==7):
        print("Saliendo del programa...")
        


#ejecutamos la clase de nodox y creamos nuestra raíz antes de la
#ejecución del programa, también igualamos los punteros en la raíz creada
R=Nodox("Raiz");
Q=R
print("La raíz se ha creado!\n")
print(Q.data)
print(Q)
Menu();


"""
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


PopRaiz();
print("Aqui sale el pto error")


Q=R
PeekNodox();


Q=R
PopLast();

Q=R
PeekNodox();


print("Introduzca el valor que desea eliminar")
dat=input();
Q=R
PopNodo(dat);


Q=R
PeekNodox();
"""