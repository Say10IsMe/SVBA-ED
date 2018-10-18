# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 06:11:54 2018

@author: pc
"""

#Creamos nuestro array al cual le ponemos el nombre de cola:
cola=[]

#definimos nuestro metodo de creación, en el cual declaramos como
#global la cola, la llenamos con 0 para establecer una dimensión
#y también declaramos como globales nuestros indices de frente y cola
def metodocreate():
    global cola
    cola=[0,0,0,0,0]
    global rear
    global front
    rear=-1
    front=0
    print("Se ha creado la cola circular con longitud de 5 espacios")
    print(cola)
    

def metodopushjojo():
            global front
            global rear
            
            #primero comparamos si en la posición actual de front
            #se encuentra un 0, de ser así, se entiende que no se
            #han introducido elementos en la cola, por lo que se procede
            #a capturar el primer valor para la cola y ponerlo en
            #la posición de rear, que primero se incrementa en 1
            if front==5:
                front=0
            if cola[front]==0:       
                print("Introduzca un valor para la cola")
                v=input();
                #Usaremos la siguiente comparación para evitar el
                #overflow en el indice rear
                if rear==5:
                    rear=-1
                    rear+=1
                    cola[rear]=v
                    print(cola)
                else:
                    rear+=1
                    if rear==5:
                        rear=0                        
                        cola[rear]=v
                        print(cola)
                    else:
                        cola[rear]=v
                        print(cola)
            #Si en la posicion de front, no se encuentra un 0 (que quiere
            #decir que ya se inserto el primer elemento), pasamos
            # a la siguiente comparación, en la cual verificamos si el
            #valor del indice de rear es menor a 4, lo que quiere decir que
            #aun no se desborda del limite de nuestro arreglo
            else:
                #de ser así, verificamos si la posición de rear+1 es igual
                #a la posición del front, lo que quiere decir que la cola
                #se encuentra llena ya que el flujo de datos dio la vuelta
                #hasta llegar de nuevo al front
                if rear<4:                    
                    if rear+1==front:
                        print("La cola se encuentra llena!")                        
                    #si la condición no se cumple, se entiende que todavía
                    #podemos seguir almacenando elementos hasta que
                    #el valor de rear ya no sea menor a 4
                    else:
                        print("Introduzca un valor para la cola")
                        v=input();
                        rear+=1
                        cola[rear]=v
                        print(cola)
                #una vez que el valor de rear ya no es menor que 4
                #es decir, que alcanzó el valor de 5, comparamos si
                #en la posición de front-1 se encuentre un 0 (esto sucederá
                #si antes se realizó un pop en la estructura, lo que quiere
                #decir que se dejó un 0 en la posición de front-1) lo que
                #significa que hay espacio disponible para un elemento
                else:
                    #entonces, igualamos el valor de rear a -1 y pedimos
                    #el dato para almacenar, incrementamos el valor
                    #de rear en 1 y almacenamos el dato en la posición
                    #de rear actual es decir, 0, y entonces empieza de nuevo
                    #el orden de las condiciones que nos han conducido aquí
                    if cola[front-1]==0:
                        rear=-1
                        print("Introduzca un valor para la cola")
                        v=input();
                        rear+=1
                        cola[rear]=v
                        print(cola)
                    #si en la posición de front-1 no hay un 0 (es decir, hay
                    #un valor) entonces se entiende que no hay espacio para
                    #meter mas elementos, por lo que se dice que la cola
                    #esta llena
                    else:
                        print("La cola se encuentra llena!!")
                    
                    
                    
                
                
    

#creamos nuestro metodo de opciones para el menu
def opciones():
    #le damos al usuario las siguientes opciones
    print("\nIntroduzca la opcion que desee")
    print("1:Crear la cola")
    print("2:Metodo Push")
    """
    print("3:Metodo Pop")
    print("4:Metodos Peek")
    print("5:Para salir")
    """
    #capturamos la entrada del usuario y la comparamos con las
    #distintas alternativas
    e=int(input())
    
    #si el usuarui decidio crear la cola, se compara si la longitud del
    #arreglo es igual a 5, osea, que existe; de ser así, se le despliega
    #el mensaje de que la cola ya fue creada
    if (e==1):
        
        if len(cola)==5:
            print("Ya se ha creado una cola anteriormente!")
            opciones();
        
        #si no, entonces ejecuta el metodo de crear cola y usamos
        #recursividad para regresar al menu de opciones
        else:
            metodocreate();
            opciones();
    #usamos la misma comparación para el resto de metodos, si
    #la longitud del arreglo cola es igual a 5 (si ya se creó) entonces
    #en el caso del push, procedemos a ejecutar dicho metodo, de no ser
    #así, le desplegamos al usuario de que no se ha creado la cola
    #anteriormente, por lo que debe crearla antes
    if(e==2):
        
        if len(cola)==5:
                        
                         
            metodopushjojo();
              
            
        else:
            print("No se ha creado una cola anteriormente!")
            
        opciones();
    """
    if (e==3):
        
        if len(cola)==5:                         
                                       
                metodopopjojo();
                
                opciones();
          
        
        else:
            print("No se ha creado una cola anteriormente")
            opciones();
        
  
    if (e==4):
        if len(cola)==5:
            
            metodopeekJOJO();
            opciones();
            
        else:
            print("No se ha creado una cola anteriormente!")
            opciones();
             
                
                
    """
    #solo en la opcion de salida no usamos recursividad, ya que no
    #tiene caso regresar al menu si es la salida
    if (e==5):
        print("Que tenga buen dia:D")
  



#ejecutamos el metodo de opciones para iniciar nuestro programa
opciones();