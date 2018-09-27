# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 19:30:19 2018

@author: pc
"""
import os
clear = lambda: os.system('cls')

#Aqui declaramos el arreglo y la variable que definirá el tamaño máximo de
#nuestra pila
pila=[]
#numerodatos=5

#Se define el metodo push, el cual se encarga: primero de verificar si la
#actual longitud de la pila es menor a el nuemero maximo da datos permitidos
#y de ser asi, procede a insertar en la pila el valor que es recibido
#como parametro en el metodo push:D
def metodopush(dato):
    if len(pila)<5:
        pila.append(dato)
        print(pila)
        #en caso de que la longitud de la pila este llena, se desplegará este
        #mensaje
    else:
            print('La pila se encuentra llena!\n')
            
            

     
            
#definimos el metodo pop, el cual se encargará de eliminar el ultimo elemento
#intoducido en la pila
def metodopop():
    #primero verifica si la pila tiene elementos para quitar con esta condición
    if len(pila)>0:
        #entonces, imprime el elemento que será borrado, lo borra e imprime
        #de nuevo la pila, para poder apreciar que el ultimo elemento fue
        #sacado de la pila
        print("\nEl valor que será borrado será el:") 
        print(pila[len(pila)-1])
        del (pila[len(pila)-1])
        print(pila)
        #en caso de que la pila no tenga elementos, se desplegará este mensaje
    else:
            print("No se pueden eliminar valores en una pila vacía")
            

#aqui definimos nuestro metodo peek
def metodopeek():
    #primero verificamos si la pila tiene elementos para continuar
    if len(pila)>0:
        
            
        #aqui esta el menu con los diferentes tipos de peeks solicitados
        print("Ingrese el tipo de peek que desea ejecutar")
        print("Introduzca 1 para peek ordinario")
        print("Introduzca 2 para peek buscador")
        print("Introduzca 3 para peek mostrador")
        #hacemos la entrada del usuario
        opcion=input();
   
    #para el primer caso, solo imprimimos el valor tope de la pila
    #esto lo conseguimos imprimiendo la posicion de la longitud de la pila
    #menos 1, recordando que los indices en la pila van desde el 0
    #por lo tanto, si la pila es de 5 elementos, las posiciones son
    # 0 1 2 3 4
        if (opcion=="1"):                            
            print("\nEl valor tope de la pila es:")
            print(pila[len(pila)-1])
            print("se encuentra en el indice")
            print(len(pila)-1)
        
            
           
           #para el segundo peek, colocamos un ciclo for para que compare
           #el numero ingresado por el usuario con los elementos de la pila
           #una vez que haya la coincidencia, imprime el valor y su posicion
           #con la funcion .index
        if (opcion=="2"):
            print("Introduzca el valor que desea buscar en la pila")
            vb=input();
            for Num in pila:
                if (Num==vb):
                    print("Valor encontrado en la pila")
                    print(vb)
                    print("Se encuentra en la posicion")
                    print(pila.index(Num))
                    opciones();
                  
            
            print("No se encontro el valor en la pila")
            
        if (opcion=="3"):
                
            print("La pila completa es esta:")
            print(pila)
           
                        
                        
    else:
        print("La pila se encuentra vacia")
        
        
def opciones():
    print("\nIntroduzca la opcion que desee")
    print("1:Metodo Push")
    print("2:Metodo Pop")
    print("3:Metodo Peek")
    print("4:Para salir")
    e=input();
    if (e=="1"):
        print("Introduzca el valor para la pila")
        v=input();
        metodopush(v)
        
        opciones();
    if(e=="2"):
        metodopop();
        
        opciones();
    
    if (e=="3"):
        metodopeek();
        
        opciones();
        
    if (e=="4"):
        print("Que tenga buen dia:D")
        
       
opciones();
       
       
       
       
       
       
   
