# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 19:08:18 2018

@author: pc
"""
#creamos nuestro metodo de busqueda binaria, el que recibe 4 parametros, la lista
#el dato, el puntero que marcará las mitdas y los 2 que marcaran el inicio y el final
def BusquedaBinaria(lista,dato,m,i,f):
    #de entrdada, obtenemos el punto medio con la suma de los 2 punteros (i y f)
    #y dividimos entre 2
    m=(i+f)//2
    
    #esta condición solo se aplicará cuando los punteros queden igualados en la
    #posición de M, lo que quiere decir que solo queda un elemento
    if (i==f):
        #comparamos el dato a buscar con el elemento restante en el arreglo
        #t de ser iguales decimos que hemos encontrado el dato a buscar
        if (dato==lista[m]):
            print("Dato encontrado!")
            print(lista[m])
            print("Encontrado en la posición:")
            print(m)
        #de no serlo, el dato a buscar no existe en la lista
        else:
            print("Dato no encontrado en la lista")
    else:
        #mientras los punteros no esten igualados, se ejecutará esta parte:
        #verificamos si el dato a buscar es mayor al punto medio, de ser así
        #entonces significa que el dato a buscar se encuentra en la parte superior
        #del arreglo, sumamos a la variable i el valor de m+1 para recorrerla
        #por encima del punto medio, usamos recursividad para ejecutar el metodo
        #de nuevo pero con los valores cambiados de los punteros
        if (dato>lista[m]):
            i=m+1
            BusquedaBinaria(lista,dato,m,i,f)
        else:
            #si el dato a buscar no es mayor que el punto medio, esto quiere
            #decir que se encuentra en la mitad inferior del arreglo, entonces debemos
            #recorrer el puntero al final del arreglo a una posición menos del punto medio
            if (dato<lista[m]):
                f=m-1
                #una vez recorrido, usamos recursividad para ejecutar el metodo de nuevo
                #pero con los valores cambiados de los punteros
                BusquedaBinaria(lista,dato,m,i,f)
                
                
                
#creamos una lista con x cantidad de datos, estos deben estar ordenados y no
#debe haber datos repetidos, si cualquiera de estas condiciones no se cumple
#entonces la lista no es apta para la busqueda binaria
lista=[1,2,3,4,5,6,7,8,9]
#pedimos la entrada del usuario
print("Ingrese el dato que desea buscar")
dato=int(input());
#definimos nuestros punteros y el valor de cada uno
i=0
f=len(lista)-1
m=0
#entonces, ejecutamos nuestro metodo de busqueda binaria enviandole
#como parametros los punteros, la lista y el dato a buscar en el arreglo
BusquedaBinaria(lista,dato,m,i,f)


