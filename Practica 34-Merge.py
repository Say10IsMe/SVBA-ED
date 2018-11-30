# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 23:29:57 2018

@author: pc
"""
from random import randint
#definimos el metodo MergeSort el cual recibe una lista
def MergeSort(lista):
    #de entrada, comparamos si la longitud de la lista es mayor a 1
    #esto servirá poesteriormente cuando se llame de manera recursiva al
    #metodo enviandole listas divididas cada vez mas pequeñas
    if len(lista) >1:
        #calculamos el punto medio al dividor la longitud
        #del arreglo entre 2 y tomando solo el entero
        mid = len(lista)//2 
        #creamos 2 sublistas que abarcaran desde el inicio hasta el punto medio
        #osea, la lista izquierda y otra desde el punto medio hasta
        #el final de la lista,osea la lista derecha
        I = lista[:mid]
        D = lista[mid:] 
        #entonces, usamos la llamada recursiva al metodo al cual enviaremos
        #las listas divididas, que a su vez, se dividirán en más hasta que la
        #longitud sea 1
        MergeSort(I)
        MergeSort(D) 
        
        #utilizamos 3 punteros inicializados en 0
        x = 0
        y = 0
        z = 0
          
        #en esta parte, moveremos los datos de ambas sublistas
        #a la lista original, pero ordenandolos en el proceso
        #declaramos un ciclo while con doble condición:
        #mientras el valor de x sea menor que la longitud de la sublista
        #izuiqerda y el valor de y menor que la longitud de la sublista
        #derecha entonces:
        while x < len(I) and y < len(D): 
            #realiza la comparación:
            #si el elemento que esta en la primera posición de
            #la sublista izquierda es menor que el elemento que 
            #esta en la primera posición de la sublista derecha
            #entonces en la posicion de z de la lista original
            #almacena el dato de la sublista izquierda, al ser menor
            if I[x] < D[y]: 
                lista[z] = I[x] 
                #entonces incrementamos el valor del puntero x
                #para seguir recorriendo elementos hasta vacear la lista
                x+=1
            #si no es menor, entonces se entiende que el elemento de la
            #sublista derecha es menor que el de la sublista izquierda
            #entonces almacena ese elemento en la lista original
            else: 
                lista[z] = D[y] 
                #incrementamos el valor de y para seguir recorriendo y
                #moviendo elementos a la lista original
                y+=1
            #despues de cada comparación y movimiento de de elementos
            #aumentamos el valor del puntero de la lista original
            #para que el elemento siguiente quede insertado enseguida
            #del ultimo ingresado
            z+=1
            
            #en esta parte, verificamos que ningun elemento haya quedado
            #atrás sin mover a la lista original
            
        #el ciclo while con la condición:
        while x < len(I): 
        #mientras el valor de x sea menor que la longitud de la sublista izquierda
        #entonces en la posición de z en la lista original, se almacenará
        #el dato que se encuentra en la posición de x en la sublista izquierda
            lista[z] = I[x] 
            #despues de cada inserción de elementos de la sublista izquierda
            #a la lista original, incrementamos el valor de los punteros en 1
            #para proseguir con con el ciclo hasta que este deje de cumplirse
            x+=1
            z+=1
        #el ciclo while con la condición:
        while y < len(D):
            #mientras el valor de y sea menor que la longitud de la sublista derecha
            #entonces en la posición de z en la lista original, se almacenara
            #el dato que se encuentra en la posición de y en la sublista derecha
            lista[z] = D[y]
            #despues de cada inserción de elementos de la sublista derecha
            #a la lista original, incrementamos el valor de los punteros en 1
            #para proseguir con con el ciclo hasta que este deje de cumplirse
            y+=1
            z+=1
            

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

#entonces ejecutamos nuestro metodo mergesort dandole la lista desordenada
#e imprimos despues la lista ordenada
MergeSort(lista)
print(lista)
