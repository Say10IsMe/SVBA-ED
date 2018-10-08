# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 13:25:03 2018

@author: pc
"""

ip=0
cola=[]
#definimos nuestro metodo create, el cual se encarga de declarar la cola global, la define con limite de 5 espacios
#e imprime el mensaje de que la cola ha sido creada
def metodocreate():
    global ip
    ip=0
    global cola
    cola=[0,0,0,0,0]
    print("Se ha creado la cola con longitud de 5 espacios")
    print(cola)
    
    
#el metodo push usa la variable ip, primero, comparamos el valor de ip con el limite de espacio de nuestra cola
#si la condicion se cumple, entonces procede a pedir al usuario un valor a insertar en la cola, lo mete en la posicion
#actual de ip, imprime la cola y aumenta el valor de ip en 1 para que la siguiente insercion sea en el siguiente espacio
def metodopushjojo():
            global ip
            if ip<5:
               # del (cola[ip])                        
                print("Introduzca un valor para la cola")
                v=input()
                cola[ip]=v
                #cola.append(0)
                print(cola)
                ip+=1 
                             
            else:
                print("La cola se encuentra llena!")        

  
        
#definimos nuestro metodo pop que se encargara de sacar el primer elemento ingresado a la cola
#en el, seguiremos usando la variable ip y ademas, la variable ie, que siempre tendra el mismo valor
#ya que el elemento que saldra siempre sera el primero, es decir, siempre estara en una sola posicion
def metodopopjojo():
    global ip
    ie=5 
    #primero comparamos si en la posicion actual de ip se encuentra un 0 (que en colas, es un espacio vacio)
    #y de ser asi, se entiende que la cola se encuentra vacia
    if ip==0:           
        print("La cola se encuentra vacia!")
        
        #de no ser asi, entonces se mostrara al usuario el valor que esta por ser borrado de la cola
        #lo borra y entonces agrega un 0 (espacio vacio) al final de la cola, ademas, incrementa el valor
        #de ip en uno para tener el control del nuermo de datos que han entrado y salido, para cuidar el underflow
    else:
        print("El valor que sera borrado de la cola es el:")
        print(cola[len(cola)-ie])
        del (cola[len(cola)-ie])
        cola.append(0)
        print(cola)
        ip-=1

"""
def metodopeekJOJO():
        #aqui esta el menu con los diferentes tipos de peeks solicitados
        global ip
        global cola
        print("Ingrese el tipo de peek que desea ejecutar")
        print("Introduzca 1 para peek ordinario")
        print("Introduzca 2 para peek buscador")
        print("Introduzca 3 para peek mostrador de toda la cola")
        print("Introduzca 4 para peek mostrador del elemento por salir")
        #hacemos la entrada del usuario
        opcion=int(input());
        
        if (opcion==1):
            if cola[ip-1]==0:
                print("La cola se encuentra vacía!")
            else:                
                print("\nEl valor tope de la cola es:")
                print(cola[ip-1])
                print("se encuentra en el indice")
                print(ip)
        
            
           
           #para el segundo peek, colocamos un ciclo for para que compare
           #el numero ingresado por el usuario con los elementos de la pila
           #una vez que haya la coincidencia, imprime el valor y su posicion
           #con la funcion .index
        if (opcion==2):
            if cola[ip-1]==0:
                print("La cola se encuentra vacía!")
            else:
                print("Introduzca el valor que desea buscar en la cola")
                vb=input();
                for Num in cola:
                    if (Num==vb):
                        print("\nValor encontrado en la cola")
                        print(vb)
                        print("\nSe encuentra en la posicion")
                        print(cola.index(Num))
                        opciones();
                                      
                    
                print("\nNo se encontro el valor en la cola")
            
        if (opcion==3):
                if cola[ip-1]==0:
                    print("La cola se encuentra vacía!")
                    print(cola)
                else:                
                    print("La cola completa es esta:")
                    print(cola)
            
            
            
        if (opcion==4):
            if cola[ip-1]==0:
                print("La cola se encuentra vacía!, no hay elemento por salir")
                print(cola)
            else:
                print("\nEl elemento que esta por salir de la pila es")
                print(cola[0])
           
    """
    
    
    
    
    
    
    

#el metodo push usa la variable ip, primero, comparamos el valor de ip con el limite de espacio de nuestra cola
#si la condicion se cumple, entonces procede a pedir al usuario un valor a insertar en la cola, lo mete en la posicion
#actual de ip, imprime la cola y aumenta el valor de ip en 1 para que la siguiente insercion sea en el siguiente espacio
def opciones():
    
    print("\nIntroduzca la opcion que desee")
    print("1:Crear la cola")    
    print("2:Metodo Push")
    print("3:Metodo Pop")
    #print("4:Metodos Peek")
    print("5:Para salir")
    e=int(input());
     #primero comparamos la opcion ingresada y en seguida, comparamos si la longitud del arreglo es de 5
    #osea, si existe el arreglo creado anteriormente por el metodo create, de ser asi
    #se muestra el mensaje de que ya se ha creado, de lo contrario, se ejecutara el metodo de creacion
    if (e==1):
        
        if len(cola)==5:
            print("Ya se ha creado una cola anteriormente!")
            opciones();
        
        else:
            metodocreate();
            opciones();
    #aplicamos la misma dinamica para todas las opciones, si la longitd del arreglo es 5
    #lo que quiere decir que ya se ha creado, se ejecuta el metodo que quiere el usuario, de no ser asi
    #se mostrara el mensaje de que no se ha creado la cola
    
    #al final de cada comparacion y sentencia else, despues de ejecutar el mensaje o metodos, mandamos a llamar
    #al metodo de opciones para usar recursividad y trabajar con la cola hasta que el usuario quiera salir
            
    if(e==2):
        
        if len(cola)==5:
                        
            metodopushjojo();
            opciones();
        else:
            print("No se ha creado una cola anteriormente!")            
            opciones();
    
    if (e==3):
        
        if len(cola)==5:                         
                                       
                metodopopjojo();
                
                opciones();
          
        
        else:
            print("No se ha creado una cola anteriormente")
            opciones();
        
        
    #if (e==4):
        #if len(cola)==5:
            #
            #metodopeekJOJO();
           # opciones();
            
        #else:
          #  print("No se ha creado una cola anteriormente!")
           # opciones();
             
                
                
    
    #if (e==5):
        #print("Que tenga buen dia:D")
       



#ejecutamos nuestro metodo de opciones para mostrar el menu y empezar la ejecucion de nuestro programa
opciones();

