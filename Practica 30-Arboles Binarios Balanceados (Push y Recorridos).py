# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 18:39:29 2018

@author: pc
"""


#creamos la clase que se encargará de construir los nodos con 2 campos
#los cuales serán los del dato a guardar y la liga para el siguiente nodo
class HojasRaiz(object):
    #en el constructor asignamos los valroes iniciales de cada campo,
    #en el caso de data, será un parametro enviado por el usuario
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
#definimos nuestro metodo Push, el cual recibe el dato por el usuario
#como parametro, usamos la variable global de Q, que será nuestro puntero
def PushHoja(data):
    global R
    global Q
    global P
    
 
    #comparamos la entrdada del usuario con el dato del nodo actual
    #si el dato del nodo actual es mayor, entonces el dato se insertara
    #en la rama izquierda al ser menor
    if (Q.data>data):
        #entonces, comprueba si la rama del nodo actual tiene un hijo izquierdo
        #si no lo tiene, entonces crea el nodo con el dato y liga la rama izquierda
        #con el nodo actualmente creado
        if (Q.left==None):
            P=HojasRaiz(data)
            Q.left=P
        #si no esta vacía, es decir, que ya hay un hijo en esa rama entonces 
        #descendemos el puntero Q a el hijo izquierdo del mismo, usamos 
        #recursividad para volver a llamar al metodo y ejecutarlo hasta que
        #la rama izquierda del nodo este vacía, entonces se insertará la hoja            
        else:            
            Q=Q.left
            PushHoja(data)
            
    #comparamos la entrdada del usuario con el dato del nodo actual
    #si el dato del nodo actual es menor, entonces el dato se insertara
    #en la rama derecha al ser mayor
    if (Q.data<data):
        #entonces, comprueba si la rama del nodo actual tiene un hijo derecho
        #si no lo tiene, entonces crea el nodo con el dato y liga la rama derecha
        #con el nodo actualmente creado
        if (Q.right==None):
            P=HojasRaiz(data)
            Q.right=P
        #si no esta vacía, es decir, que ya hay un hijo en esa rama entonces 
        #descendemos el puntero Q a el hijo derecho del mismo, usamos 
        #recursividad para volver a llamar al metodo y ejecutarlo hasta que
        #la rama izquierda del nodo este vacía, entonces se insertará la hoja
        else:
            Q=Q.right
            PushHoja(data)
    

#metodo para mover el puntero a su rama izquierda siempre que la rama del nodo
#actual tenga un hijo en la izquierda
def MoverIzPre(nodo):
    if(nodo.left!=None):
        nodo=nodo.left
        RecPreOrden(nodo)

#metodo para mover el puntero a su rama derecha siempre que la rama del nodo
#actual tenga un hijo en la derecha
def MoverDerPre(nodo):
    if(nodo.right!=None):
        nodo=nodo.right
        RecPreOrden(nodo)
    
#metodo para recorrer el arbol en preorden, se apoya de otros 2 metodos para
#recorrer el arbol izquierdo y el arbol derecho
#primero imrpime la raiz, luego el arbol izquierdo y enseguida el derecho
def RecPreOrden(nodo):
    print(nodo.data)
    MoverIzPre(nodo)
    MoverDerPre(nodo)




#metodo para mover el puntero a su rama izquierda siempre que la rama del nodo
#actual tenga un hijo en la izquierda
def MoverIzInor(nodo):
    if(nodo.left!=None):
        nodo=nodo.left
        RecInorden(nodo)

#metodo para mover el puntero a su rama derecha siempre que la rama del nodo
#actual tenga un hijo en la derecha
def MoverDerInor(nodo):
    if(nodo.right!=None):
        nodo=nodo.right
        RecInorden(nodo)
    
#metodo para recorrer el arbol en inorden, se ayuda de otros 2 metodos que ayudan
#a recorrer el arbol izquierdo, enseguida imprime la raiz y luego el subarbol
#derecho

def RecInorden(nodo):
    MoverIzInor(nodo)
    print(nodo.data)
    MoverDerInor(nodo)



#metodo para mover el puntero a su rama izquierda siempre que la rama del nodo
#actual tenga un hijo en la izquierda
def MoverIzPost(nodo):
    if(nodo.left!=None):
        nodo=nodo.left
        RecPostorden(nodo)

#metodo para mover el puntero a su rama derecha siempre que la rama del nodo
#actual tenga un hijo en la derecha
def MoverDerPost(nodo):
    if(nodo.right!=None):
        nodo=nodo.right
        RecPostorden(nodo)
        

#metodo para recorrer el arbol en postorden, se ayuda de 2 metodos auxiliares
#para recorrer primero el arbol izquierdo, luego el arbol derecho e imprimir la
#raiz al final, recibe como parametro el nodo raiz
def RecPostorden(nodo):
    MoverIzPost(nodo)
    MoverDerPost(nodo)
    print(nodo.data)




#pedimos una entrada del usuario para ponerle valor a la raíz e igualamos
#los punteros en la misma posicion
print("Introduzca un numero para la raíz")
dat=input();
R=HojasRaiz(dat);
Q=R


#pedimos la entrada del usuario una serie de veces para insertar los nodos
#antes de cada inserción, primero igualamos los punteros Q y R para irlos
#recorriendo hasta llegar a un nodo que tenga x rama desocupada
print("Introduzca el dato que desea ingresar")
Q=R
d=input();
#mandamos el metodo push el dato que el usuario ingreso para el nodo
PushHoja(d)


print("Introduzca el dato que desea ingresar")
Q=R
d=input();
PushHoja(d)


print("Introduzca el dato que desea ingresar")
Q=R
d=input();
PushHoja(d)

print("Introduzca el dato que desea ingresar")
Q=R
d=input();
PushHoja(d)

print("Introduzca el dato que desea ingresar")
Q=R
d=input();
PushHoja(d)

print("Introduzca el dato que desea ingresar")
Q=R
d=input();
PushHoja(d)

print("Introduzca el dato que desea ingresar")
Q=R
d=input();
PushHoja(d)


#ejecutamos el recorrido del arbol en preorden llamando al metodo y mandandole la 
#raiz como parametro
print ("\nRecorrido preorden")
RecPreOrden(R)


#ejecutamos el recorrido del arbol en preorden llamando al metodo y mandandole la 
#raiz como parametro
print ("\nRecorrido inorden")
RecInorden(R)


#ejecutamos el recorrido del arbol en preorden llamando al metodo y mandandole la 
#raiz como parametro
print ("\nRecorrido postorden")
RecPostorden(R)
