# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 06:16:42 2018

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
    
    #primero preguntamos al usuario donde desea insertar su hoja
    print("Donde desea meter la hoja?")
    print("Izquierda: I")
    print("Derecha: D")
    #leemos la opcion del usuario
    choice=input();
    #comparamos la opcion del usuario con las posibles opciones
    if (choice=="I"):
        #si desea insertarlo en la izquierda, primero verificamos que
        #el actual nodo (en el cual, esta ubicado Q) no haya un hijo izquierdo
        #de ser así, entinces creamos el nodo con el dato del usuario
        #y enlazamos dicho nodo a la parte izquierda vacía de Q
        if (Q.left==None):
            P=HojasRaiz(data)
            Q.left=P
        #si no esta vacía, es decir, que ya hay un hijo en esa rama, entonces
        #le indicamos al usuario que ya se encuentra ocupado esta rama y descendemos
        #el puntero Q a el hijo izquierdo del mismo, usamos recursividad para
        #volver a llamar al metodo y ejecutarlo hasta que la rama izquierda del
        #nodo este vacía, entonces se insertará la hoja            
        else:            
            print("Este nodo ya tiene su hoja izquierda, desendiendo al sig nivel")
            Q=Q.left
            PushHoja(data)
            
    if (choice=="D"):
        #si desea insertarlo en la derecha, primero verificamos que
        #el actual nodo (en el cual, esta ubicado Q) no haya un hijo derecho
        #de ser así, entinces creamos el nodo con el dato del usuario
        #y enlazamos dicho nodo a la parte derecha vacia de Q
        if (Q.right==None):
            P=HojasRaiz(data)
            Q.right=P
        #si no esta vacía, es decir, que ya hay un hijo en esa rama, entonces
        #le indicamos al usuario que ya se encuentra ocupado esta rama y descendemos
        #el puntero Q a el hijo derecho del mismo, usamos recursividad para
        #volver a llamar al metodo y ejecutarlo hasta que la rama derecha del
        #nodo este vacía, entonces se insertará la hoja
        else:
            print("Este nodo ya tiene su hoja derecha, desendiendo al sig nivel")
            Q=Q.right
            PushHoja(data)
    


#creamos por determinación nuestra raiz e igualamos el puntero Q con R
R=HojasRaiz("Raiz");
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





