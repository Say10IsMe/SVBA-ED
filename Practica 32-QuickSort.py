# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 16:53:53 2018

@author: pc
"""
from random import randint
#definimos nuestro metodo quicksort, el cual recibe una lista como parametro
def QuickSortez(lista):
    #comparamos si la longitud de la lista es menor o igual a 1, lo que quiere
    #decir que se ha logrado partir y ordenar la lista en arreglos de hasta
    #dimensión 1, entonces, devuelve la lista
    if len(lista)<=1:
        return(lista)
    #creamos 3 arreglos, uno para los menores que el pivote, para los iguales
    #y para los mayores que el pivote
    menorespiv=[]
    igualespiv=[]
    mayorespiv=[]
    #definimos como pivote el numero que se encuentra justo a la mitad
    #de la lista
    pivote=lista[len(lista)//2]
    
    #iniciamos un ciclo for, que irá desde i hasta la longitud de la lista
    for i in lista:
        #si el dato que se encuentra en i es menor que el pivote, entonces
        #lo agregamos al arreglo de menores
        if i<pivote:
            menorespiv.append(i)
        #si el dato en la posicion de i es igual al pivote, lo agregamos
        #al arreglo de iguales
        elif i==pivote:
            igualespiv.append(i)
        #si no es ni menor ni igual, se entiende que es mayor, entonces
        #lo agregamos al arreglo de mayores
        else:
            mayorespiv.append(i)
    #retornaremos la concanetación de los arreglos
    #notese que se usa la recursividad en los arreglos de
    #menores y mayores para que en las posteriores ejecuciones
    #del metodo quicksort sobre estas listas, se repita el proceso de seleccionar
    #los mayores, menores e iguales y ponerlos a su vez en respectivas listas
    #esto se seguirá ejecutando hasta que la longitud de los arreglos sea <=1
    #entonces se irán retornando las listas arregladas por cada ejecución del
    #metodo quicksort hasta llegar a la primera ejecución, devolviendo entonces
    #la lista ordenada
    return QuickSortez(menorespiv)+igualespiv+QuickSortez(mayorespiv);


#creamos nuestra lista vacía
lista=[]
#definimos nuestro metodo para la inserción de numeros aleatorios, el cual
#recibe como parametro la lista y el contador
def insercion(lista,c):
    #si el contador sea menor que 50
    if c<50:
        #crea un numero aleatorio entre 0 y 100 y lo agrega a la lista
        #incrementa el valor del contador en 1 y se usa recursividad
        #para llamar al metodo hasta que que se hayan insertado los 50 elementos
        e=randint(0,100)
        lista.append(e)
        c+=1
        insercion(lista,c)
    #cuando ya no se cumple la condicion, entonces imprimimos este mensaje junto
    #con la lista
    else:
        print("Insercion terminada")
        print(lista)

#definimos el valor del contador en 0 y mandamos a llamar al metodo de insercion
#dandole el valor del contador y la lista vacia
c=0
insercion(lista,c)

#declaramos una variable en la cual se almacenará la lista final y concatenada
#del metodo quicksort, al mismo tiempo, le enviamos la lista con los valores
#insertados
listafinal=QuickSortez(lista)

#mostramos la lista final y ordenada
print(listafinal)
