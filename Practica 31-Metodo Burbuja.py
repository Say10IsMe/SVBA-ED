# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
#tenemos una lista con una serie de numeros desordenados
lista=[7,1,2,8,9,3,4,5,6]
#utilizaremos un puntero i con el valor inicial de 0
i=0
#definimos nuestro metodo burbuja enviandole como parametros la lista
#y el puntero i
def metodoburbuja(lista,i):
    #creamos un ciclo for con el rango de 0 hasta la longitud de la lista-1
    for i in range(0,len(lista)-1):
        #comparamos entonces los elementos:
        #si el elemento en i es mayor que el elemento de i+1
        #(osea, el que esta enseguida) entonces guardamos
        #el valor del elemento i+1 en una variable
        #reemplazamos el elemento actual de i+1 con el elemento posterior
        #dejando así el mas grande adelante y el mas chico atrás
        #y en la posicion de i ponemos el elemento guardado en la variable
        #temporal, incrementamos el valor de en 1 y usamos recursividad para
        #llamar de nuevo al metodo enviandole la lista con los 2 elementos
        #cambiados y el nuevo valor de i
        if (lista[i]>lista[(i)+1]):
            t=lista[(i+1)]
            lista[(i+1)]=lista[(i)]
            lista[(i)]=t
            i+=1
            metodoburbuja(lista,i);


#imprimimos el nuestra lista desordenada
print(lista)
#ejecutamos el nuestro metodoburbuja mandandole la lista y el puntero i
metodoburbuja(lista,i);
#imprimimos muestra lista ordenada
print(lista)

