# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 21:45:22 2018

@author: pc
"""


#definimos el metodo de entrada para la potenciación
def entradapotencia():
    #las variables que utilizaremos para la ejecución:
    #el indice, que controlará el numero de veces que se llamará el metodo
    #a si mismo
    indice=1
    #el numero base sobre el cual se aplicará la potenciación, en este caso
    #predeterminado por el profesor :"2 "
    numerobase=2
    #variable que utilizaremos para la multipliación
    resultado=2
    #pedimos que el usuario ingrese la potencia deseada para el numero
    print("Introduzca la pontencia para el numero 2")
    p=input();
    #en seguida, mandamos como parametros todas las variables y la potencia
    #que pidió el usuario
    potenciajojo(p,indice,resultado,numerobase);

#definimos el metodo que se encargará de potenciar y asignamos los parametros
#que llegarán
def potenciajojo(p,i,r,nb):
    #esta es la condición de detención, cuando el indice alcance el valor
    #de la potencia, significa que el numero 2 ya fue multiplicado por si
    #mismo el numero de veces deseado
   if (i==int(p)):
       #entonces imprimimos este mensaje y en seguida el resultado de la
       #potenciación
        print("Se ha elevado el numero a la potencia deseada!")
        print(r)
        
   else:        
       #si no se cumple la condición, se ejecutará este bloque hasta que lo haga
       #se multiplica el numero base por resultado y asigna a la misma variable
       #el resultado de dicha multiplicación, desde aquí, la variable nb
       #será constante y el resultado será el valor de la potenciación anterior
           r=r*nb
           #incrementamos el valor de i cada vez que este bloque se ejecuta
           #para controlar las veces que se hará la potenciación
           i+=1
           #utilizamos la recursividad, mandando los datos nuevos como lo son
           #el resultado nuevo y el indice nuevo, solo nb y p permanecen constantes
           potenciajojo(p,i,r,nb);
       


#se ejecuta de primera instancia el metodo de entrada para la potencia        
entradapotencia();

        