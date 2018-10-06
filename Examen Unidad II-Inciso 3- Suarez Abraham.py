# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 01:10:26 2018

@author: pc
"""
#definimos el arreglo para la pila y el indice para las posiciones
listaregistros=[]
ind=1
#nuestro metodo para agregar registros
def ingresarregistro():
    #declaramos la variable global para poder utilizarla aquí
    global ind
    #agregamos el registro con el mismo numero del indice
    listaregistros.append(ind)
    #incrementamos el valor del indice para almacenar el registro en la
    #siguente posción
    ind+=1
    #desplegamos este mensaje y seguido la pila con los registros ingresados
    print("\nSe ha agregado el registro:")
    print(listaregistros)
    
#definimos el metodo obtener registro, lo que sería el POP de la pila
def obtenerregistro():
    global ind
    #definimos la condición para no hacer pop cuando la pila esta vacía
    if (len(listaregistros)>0):
        print("\nEl registro que será obtenido será el:") 
        print(listaregistros[len(listaregistros)-1])
        del (listaregistros[len(listaregistros)-1])
        print(listaregistros)
        ind-=1
    else:
        print("La lista de registros se encuentra vacía!, inserte antes un registro a obtener")


#definmos el metodo de visualización, el cual mostrará todas las migraciones
#de la mas reciente a la mas antigua
def vertodosregistros():
    #pero antes, compara la longitud de la pila, si esta es mayor de 0, es
    #decir, si no esta vacía, procede con la impresión utilizando un ciclo
    #for e imprimiendolos a la inversa en la que fueron ingresados
        if (len(listaregistros)>0):
            print("Las migraciones desde la mas nueva a la mas antigua:")
            for i in range(len(listaregistros)):
                print(listaregistros[len(listaregistros)-i-1])
        #si la pila esta vacia, se despliega este mensaje al usuario
        else:
            print("La lista de migraciones esta vacía! no hay registros que mostrar")

#creamos nuestro metodo para el menu, llamado opciones
def opciones():
    print("\nSi desea agregar una migracion, presione: 1")
    print("Si desea obtener la migracion mas reciente, presione: 2")
    print("Si desea ver todas las versiones, presione: 3")
    print("Si desea salir del programa, presiones: 4")
    s=int(input());
    
    #comparamos la entrada del usuario con cada una de las opciones del menu
    #y si hay coincidencia, ejecutamos el metodo deseado, además de usar
    #recursividad para volver al menu de opciones, llamandolo despues de cada
    #comparación
    if (s==1):
            ingresarregistro();
            opciones();
        
    if (s==2):
            obtenerregistro();
            opciones();
    if (s==3):
        vertodosregistros();
        opciones();
        
    #en el ultimo caso, no lloamamos al metodo de opciones ya que es la salida
    if (s==4):
            print ("\nQue tenga buen dia:D")
            

opciones();
        
