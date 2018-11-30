# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 20:25:23 2018

@author: pc
"""
from random import randint


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
             #se ecuentra en la posicion del salto, entonces los datos se intercambiarán
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

#entonces ejecutamos nuestro metodo shellsort dandole la lista desordenada
#e imprimos despues la lista ordenada
ShellSort(lista)
print("\nLista ordenada\n")
print(lista)