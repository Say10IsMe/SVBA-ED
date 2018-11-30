# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 00:19:05 2018

@author: pc
"""
from random import randint
from datetime import datetime
from time import time



#definimos nuestro metodo de ordenamiento burbuja, que recibe como parametros
#la lista y un puntero x
def metodoburbuja(lista, x):
    #usamos la siguiente condicion para verificar si la variable x es menor
    #que la longitud del arreglo
    if x<len(lista):
        #si es menor, incrementa su valor en 1
        x+=1
        for i in range(len(lista)-x):
            #creamos un ciclo for que va desde 0 hasta la longitud del arreglo -1
            #checamos si el valor en el indice actual es mayor al valor en el indice siguiente
            if(lista[i]>lista[i+1]):
                #de ser asi, se crea una variable auxuliar t, que nos
                #servira para guardar momentaneamente el dato
                t=lista[i]
                #luego, el dato que se encuentra adelante se mueve atras al ser menor
                lista[i]=lista[i+1]
                #ahora, sustituimos el valor de adelante con el valor que se
                #encontraba atras, ya que este es mayor
                lista[i+1]=t
        #usamos recursividad para volver a llamar al metodo el numero
        #de veces necesario hasta terminar de ordenar la lista
        metodoburbuja(lista,x)
    else:
        #cuando la variable x ya no sea menor que la longitud del arreglo
        #se entiende que se ha terminado de ordenar, se imprime  el siguiete mensaje
        print("Lista ordenada")

        
        
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




#definimos nuestro metodo shellsort que recibe como parametro un arreglo
def ShellSort(lista):
     #definimos de cuanto será nuestro salto entre los datos del arreglo
     #dividimos la longitud entre 2 tomando solo el entero
     salto = len(lista) // 2
     
     #creamos un ciclo while con la condición de: mientras el salto
     #sea mayor que 0
     while salto > 0:
         #se ejecutará este ciclo for, en el rango de i hasta la longitud de la
         #lista
         for i in range(salto, len(lista)):
             #guardamos el numero que se encuentra en la posicion de i
             #en una variable e igualamos el puntero z a la posición de i
             num = lista[i]
             z = i
             #creamos un ciclo anidado while con las siguientes condiciones:
             #mientras el valor de z sea mayor o igual al valor del salto
             #y el dato que esta en la posicion de z menos el salto mayor
             #que el numero que guardamos en la variable num, osea el numero que
             #se ecuentra en la posicion del salto, entonces los datos se cabian
             while z >= salto and lista[z - salto] > num:
                 lista[z] = lista[z - salto]
                 #disminuiremos el valor de z en la cantidad da salto para
                 #ir avanzando en el arreglo y cambiar las posiciones cuando
                 #la condición se cumpla
                 z -= salto
            #a la posición de z en la lista, le asignamos el valor de num
             lista[z] = num
        #dividiremos el valor del salto entre 2 y obtendremos el valor
        #entero solamente despues de cada iteración
         salto //= 2
         
         
         
         
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
    global listab
    global listaq
    global listas
    global listam
    #si el contador sea menor que 50
    if (c<1000):
        #crea un numero aleatorio entre 0 y 100 y lo agrega a la lista
        #incrementa el valor del contador en 1 y se usa recursividad
        #para llamar al metodo hasta que que se hayan insertado los 50 elementos
        e=randint(0,1000)
        lista.append(e)
        c+=1
        insercion(lista,c)
    #cuando ya no se cumple la condicion, entonces imprimimos este mensaje2
    #y creamos diferentes listas (una para cada metodo de ordenamiento)
    #asignamos a cada una de las listas los datos de la original
    else:
        print("Insercion terminada")
        listab=lista
        listaq=lista
        listas=lista
        listam=lista


def menu():
    print("Crear una nueva lista aleatoria:1")
    print("Metodo Burbuja:                 2")
    print("Metodo QuickSort:               3")
    print("Metodo ShellSort:               4")
    print("Metodo MergeSort:               5")
    opc=int(input());
    if (opc==1):
        lista=[]
        c=0
        insercion(lista,c)
        menu();
    if (opc==2):
        n=0
        tib=time()
        metodoburbuja(listab,n);
        tfb=time()
        print("Lista ordenada por metodo burbuja")
        print(listab)
        print("Tiempo tomado para ordenamiento")
        print(tfb-tib)
        menu();
    if (opc==3):
        tiq=time()
        listaquick=QuickSortez(listaq);
        tfq=time()
        tq=(tfq-tiq)
        print("Lista ordenada por Quicksort")
        print(listaquick)
        print("Tiempo tomado para ordenamiento")
        print(tq)
        menu();
    if (opc==4):
        tis=time()
        ShellSort(listas);
        tfs=time()
        print("Lista ordenada por Shellsort")
        print(listas)
        print("Tiempo tomado para ordenamiento")
        print(tfs-tis)
        menu();
    if (opc==5):
        tim=time()
        MergeSort(listam);
        tfm=time()
        print("Lista ordenada por Mergesort")
        print(listam)
        print("Tiempo tomado para ordenamiento")
        print(tfm-tim)
        menu();
        
menu();

