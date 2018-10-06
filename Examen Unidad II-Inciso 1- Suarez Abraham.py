# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 21:28:58 2018

@author: pc
"""
#Definimos las variables que utilizaremos durante la ejecución del programa
indice=0
valor=1
resultado=0

#definimos nuestro metodo de suma
def sumajojo():
    #declaramos las variables globales para poder trabajar con ellas en este
    #metodo
    global indice
    global valor
    global resultado
    
    #establecemos la condición que detendrá la recursividad, en este caso
    #será cuando el indice alcance el nuermo 9
    if (indice==9):
        #entonces se imprime el mensaje siguiente:
        print("El valor maximo ha sido alcanzado!")
        #y en seguida el resultado de la suma
        print(resultado)
        #cuando no se da la condición de detención, se ejecutará este bloque
        #de codigo
    else:
        #a la variable resultado, le incrementaremos el el valor de la variable
        #"valor", la cual va constantemente aumentando en 1, al mismo tiempo
        #aumentamos el valor de la variable indice, que es la servirá en la
        #comparación para detener la recursividad
        resultado+=valor
        valor+=1
        indice+=1
        #aqui se hace uso de la recursividad, se llamará al metodo el numero
        #necesario de veces hasta que la condición se cumpla
        sumajojo();
        
        
#ejecutamos el metodo de suma        
sumajojo();
        