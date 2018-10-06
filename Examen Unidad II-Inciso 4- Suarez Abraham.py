# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 01:40:22 2018

@author: pc
"""
#declaramos nuestra variable indice junto con el arreglo que será nuestra
#cola para la caja
ip=0
colamercado=[]
#definimos nuestro metodo crear, en el cual declaramos como globales las
#variables de indice y el arreglo de cola
def metodocreate():
    global ip
    ip=0
    global colamercado
    # llenamos la cola con espacios vacios, imprimimos el mesaje de que
    #se ha abierto la caja con espacio para 5 clientes y la imprimimos
    colamercado=['Desocupado','Desocupado','Desocupado','Desocupado','Desocupado']
    print("Se ha abierto la caja con capacidad para 5 clientes!")
    print(colamercado)
    
    
#definimos el metodo push, en el cual usamos la variable de indice y despues
#comparamos si esta es menor al limite de clientes que entran en la cola
#pedimos el nombre del cliente y lo colocamos en la posición designada por
# la misma variable de indice, reemplazando el espacio vacio con un cliente
def metodopushjojo():
            global ip
            if ip<5:                                      
                print("Introduzca el nombre del cliente:")
                v=input()
                colamercado[ip]=v
                #cola.append(0)
                print(colamercado)
                ip+=1 
#en caso de que la variable alcance al indice, se desplegará este mensaje
#que indica que la cola esta en su maxima capacidad                             
            else:
                print("La fila se encuentra llena!")        

  
        
#definimos el metodo pop, que se encargará de "despachar" al cliente primero
#en la fila, usamos la variable de indice y aparte agregamos una mas, que se
#encargará de establacer cual cliente será despachado, es decir, el primer cliente
#que llego; el que siempre estará en la posición ultima del arreglo
def metodopopjojo():
    global ip
    ie=5 
#comparamos el espacio en la cola, y de ser "desocupado" se entiende que la cola
#esta vacia, por lo tanto, no hay clientes que despachar
    if colamercado[0]=='Desocupado':           
        print("La fila se encuentra vacia!,no hay clientes para despachar")
#de no ser así, imprimimos que el cliente en la ultima posición del arreglo
#(el primero en llegar) ha sido despachado, lo borramos del arreglo y
#agregamos un espacio "desocupado" al final de la cola, además restamos a
#la variable indice 1 para tener controlado el underflow
    else:
        print("El cliente que fue despachado fue:")
        print(colamercado[len(colamercado)-ie])
        del (colamercado[len(colamercado)-ie])
        colamercado.append('Desocupado')
        print(colamercado)
        ip-=1


def metodopeekJOJO():
        #aqui esta el menu con los diferentes tipos de peeks solicitados
        global ip
        global colamercado
        print("Ingrese la opcion que desee")
        print("Introduzca 1 para saber que cliente llego al final")
        print("Introduzca 2 para buscar un cliente en especifico")
        print("Introduzca 3 para mostrar toda la fila de clientes")
        print("Introduzca 4 para saber que cliente esta por salir")
        #hacemos la entrada del usuario
        opcion=int(input());
        
        #hacemos las comparaciones de la ingresión del usuario con todas
        #las opciones y se ejecuta la que pidio
        if (opcion==1):
            #hacemos la condición para el caso en el que la cola se
            #encuentra vacia, es decir, si la posición esta "desocupada" se
            #entiende que esta vacia
            if colamercado[ip-1]=='Desocupado':
                print("La fila de clientes esta vacía!")
                #de no ser asi, se imprime el cliente que llegó al final, es decir
                #el que esta en la posición ip-1 ya que la posición ip acualmente
                #se encuentra en un espacio desocupado, ya que se incrementa
                #despues de cada push
            else:
                print("\nEl ultimo cliente que llego fue:")
                print(colamercado[ip-1])
                print("Será atendido en la posición:")
                print(ip-1)
        
            
           
           #para el segundo peek, colocamos un ciclo for para que compare
           #el el cliente ingresado por el usuario con los elementos de la cola
           #una vez que haya la coincidencia, imprime el cliente y su posicion
           #con la funcion .index
        if (opcion==2):
            if colamercado[ip-1]=='Desocupado':
                print("La fila de clientes esta vacía!")
                
            else:
                print("Introduzca el nombre del cliente que quiere buscar")
                vb=input();
                for Num in colamercado:
                    if (Num==vb):
                        print("Cliente encontrado en la fila!")
                        print(vb)
                        print("Se encuentra en la posicion")
                        print(colamercado.index(Num))
                        opciones();
                  
                    #en caso de no hayar coincidencias, se despliega este mensaje
                    print("No se encontró al cliente en la fila")
                
        #este opcion simplemente despliega toda la fila, en caso de que este
        #vacia, avisa que lo esta y luego la imprime para verificar
        if (opcion==3):
                if colamercado[ip-1]=='Desocupado':
                    print("La fila esta vacia!")
                    print(colamercado)
                else:
                    print("La fila de clientes es esta!:")
                    print(colamercado)
            
            
        #esta opcion, luego de verificar que la pila no esta vacia, siempre
        #imprimirá el cliente en la posición inicial del arreglo, osea: el
        #primer cliente en llegar
        if (opcion==4):
            
            if colamercado[0]=='Desocupado':
                print("La fila de clientes esta vacía, no hay cliente por despachar")
            else:
                print("\nEl cliente que esta por ser despachado es:")
                print(colamercado[0])
           
    
    
    
    
    
    
    
    

#creamos nuestro menu con las opciones que se muestran a continuación:
def opciones():
    
    print("\nIntroduzca la opción que desee")
    print("1:Abrir caja con capacidad de 5 clientes")
    print("2:Agregar Cliente")
    print("3:Despachar cliente")
    print("4:Consultar estado de la fila")
    print("5:Para salir del programa")
    e=int(input())
    
#para acceder a las opciones, comparamos el numero que introdujo el usuario
#y entonces ejecutamos su opcion, pero antes, establecemos una condicion
#en la que se verifica si la cola ha sido creada, de no ser así, se desplegará
#el mensaje de que no se ha creado, y seguirá haciendolo hasta que antes
#se abrá la caja (se cree la cola con el metodo create), esto se repite
#en todos las opciones de la cola
    
#para evitar el uso de iteradores, despues de cada ejecucion de las sentencias
# if y else, usamos recursividad para volver a ejecutar el menu, esto se repite
#en todas las opciones disponibles menos en la opcion de salida
    if (e==1):
        
        if len(colamercado)==5:
            
            print("Ya se ha abierto la caja anteriormente!")
            opciones();
        
        else:
            metodocreate();
            opciones();
                
    if(e==2):
        
        if len(colamercado)==5:
                        
                         
            metodopushjojo();
              
            
        else:
            print("Aún no se ha abierto la caja! espere a las 8:00 am :3")
            
        opciones();
    
    if (e==3):
        
        if len(colamercado)==5:                         
                                       
                metodopopjojo();
                
                opciones();
          
        
        else:
            print("Aún no se ha abierto la caja! espere a las 8:00 am :3")
            opciones();
        
        
    if (e==4):
        if len(colamercado)==5:
            
            metodopeekJOJO();
            opciones();
            
        else:
            print("Aún no se ha abierto la caja! espere a las 8:00 am :3")
            opciones();
             
                
    if (e==5):
        print("Que tenga buen dia:D")
       


#por ultimo, ejecutamos el metodo de opciones para mostrar el menu al usuario:3
opciones();



