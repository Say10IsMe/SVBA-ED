# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 18:12:38 2018

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
    

#en el metodo push, usamos los indices de front y rear
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
                    
                    
                    
                
                
    

    
#definimos nuestro metodo pop, el cual se encargará de sacar los elementos
#de nuestra cola
def metodopopjojo():
    #usaremos las variables de rear y front
    global rear
    global front
    
    #primero comparamos si el valor actual de rear es menor a 5, osea
    #que no se ha desbordado, entonces comparamos si en la actual posición
    #de front hay un 0, de ser así, entonces no hay elementos por salir
    #por consecuencia, la cola se encuentra vacia
    if front<5:
        if (cola[front]==0):
            print("La cola se encuentra vacia!") 
        #si no hay un 0, procedemos a hacer las siguientes comparaciones:
        #si el valor de front es menor a 5 (que no se ha desbordado)
        #imprimimos el valor que esta por salir (el valor que se encuentra
        #en la posicion de front), seguido, reemplazamos ese dato en esa
        #posicion con un 0 e incrementamos el valor de front en 1, ya que
        #la posición de front se moverá al siguiente elemento
        else:
            if front<5:
                print("El valor que sera borrado de la cola es el:")
                print(cola[front])
                cola[front]=0
                print(cola)
                front+=1
            #si el valor de front no es menor a 5, es decir, que es 5
            #verificamos si en la posición de rear se encuentra un 0
            #si se cumple la condición, entonces se sabe que se han eliminado
            #todos los elementos y por consecuencia la cola esta vacia
            else:
                if cola[rear]==0:
                    print("La cola se encuentra vacia!!!")
                #si es diferente de 0, reiniciamos el valor de front
                #ya que el flujo de datos ya dio la vuelta a la cola
                else:
                    #reiniciamos el valor de front, y entonces "vaceamos"
                    #el espacio de este, aumentamos su valor en 1 para que
                    #el front pase al siguiente elemento de la lista
                    front=0
                    print("El valor que sera borrado de la cola es el:")
                    print(cola[front])
                    cola[front]=0
                    print(cola)
                    front+=1
    #si la primera condicón no se cumple, entonces comparamos si en
    #rear se encuentra un 0, de ser así, se entiende que la cola
    #esta vacía
    else:
        if cola[rear]==0:
            print("La cola se encuentra vacia!!")
        #si no es así, entonces reiniciamos el valor de front y reiniciamos
        #el flujo de datos (porque el flujo ya dio la vuelta a la cola)
        else:
            #mostramos el valor que esta en front y lo reemplazamos
            #con un 0, es decir, un espacio vacio
            front=0
            print("El valor que sera borrado de la cola es el:")
            print(cola[front])
            cola[front]=0
            print(cola)
            front+=1





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
        
        #comparamos la entrada del usuario con las diferentes alternativas
        #y seguido, nos aseguramos de que la cola no esta vacía:
        if (opcion==1):
            #en esta condición, checamos si en la posición de front hay un
            #0, de ser así, se entiende que la cola esta vacía y entonces
            #no se puede ejecutar el peek
            if cola[front]==0:
                print("La cola se encuentra vacía!")
            #si no lo esta, simplemenete imprime el valor que esta en
            #la posición de rear, osea, el ultimo valor ingresado
            else:                
                print("\nEl valor tope de la cola es:")
                print(cola[rear])
                print("se encuentra en el indice")
                print(rear)
        
            
           
           #para el segundo peek, colocamos un ciclo for para que compare
           #el numero ingresado por el usuario con los elementos de la pila
           #una vez que haya la coincidencia, imprime el valor y su posicion
           #con la funcion .index
        if (opcion==2):
            if cola[front]==0:
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
                                      
                #si no se encuentra el valor, se imprime este mensaje
                print("\nNo se encontro el valor en la cola")
        
        #usamos la misma comparación para saber si la cola esta vacía
        if (opcion==3):
                if cola[front]==0:
                    print("La cola se encuentra vacía!")
                    print(cola)
                #si no lo esta, se imprime toda la cola
                else:                
                    print("La cola completa es esta:")
                    print(cola)
            
            
        #repetimos la condición para el menu y para saber si esta vacía
        if (opcion==4):
            if cola[front]==0:
                print("La cola se encuentra vacía!, no hay elemento por salir")
                print(cola)
            #si no lo está, se imprimirá el valor que se encuentra en
            #la posición de rear
            else:
                print("\nEl elemento que esta por salir de la cola es")
                print(cola[front])
           

    
    
    
    
    
    
    


#creamos nuestro metodo de opciones para el menu
def opciones():
    #le damos al usuario las siguientes opciones
    print("\nIntroduzca la opcion que desee")
    print("1:Crear la cola")
    print("2:Metodo Push")
    print("3:Metodo Pop")
    print("4:Metodos Peek")
    print("5:Para salir")
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
            opciones();
            
        else:
            print("No se ha creado una cola anteriormente!")
            opciones();
    
    if (e==3):
    #si el usuario eligió hacer un pop, lo primero es verificar si
    #la cola existe con la comparación de len(cola)==5, si es así,
    #entonce es posible ejecutar el metodo pop, pero si la longitud no es
    #5, se entiende que no se ha creado la cola, por lo tanto, no se puede
    #proseguir hasta que se haya creado la cola
        
        if len(cola)==5:                         
                                       
                metodopopjojo();
                
                opciones();
          
        
        else:
            print("No se ha creado una cola anteriormente")
            opciones();
    
    #repetimos la comparación para la entrada del usuario y para verificar
    #si la cola fue creada anteriormente
    if (e==4):
        if len(cola)==5:
            #de ser así, se ejecutan los peeks y se usa recursividad para
            #regresar al menu
            metodopeekJOJO();
            opciones();
            
        else:
            print("No se ha creado una cola anteriormente!")
            opciones();
             
                
                
    #solo en la opcion de salida no usamos recursividad, ya que no
    #tiene caso regresar al menu si es la salida
    if (e==5):
        print("Que tenga buen dia:D")
  



#ejecutamos el metodo de opciones para iniciar nuestro programa
opciones();