# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 06:07:18 2018

@author: pc
"""


ip=0
cola=[]
def metodocreate():
    global ip
    ip=0
    global cola
    cola=[0,0,0,0,0]
    print("Se ha creado la cola con longitud de 5 espacios")
    print(cola)
    
    

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

  
        
"""
def metodopopjojo():
    global ip
    ie=5 
    if ip==0:           
        print("La cola se encuentra vacia!")
    else:
        print("El valor que sera borrado de la cola es el:")
        print(cola[len(cola)-ie])
        del (cola[len(cola)-ie])
        cola.append(0)
        print(cola)
        ip-=1


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
    
    
    
    
    
    
    


def opciones():
    
    print("\nIntroduzca la opcion que desee")
    print("1:Crear la cola")    
    print("2:Metodo Push")
    #print("3:Metodo Pop")
    #print("4:Metodos Peek")
    print("5:Para salir")
    e=int(input());
    
    if (e==1):
        
        if len(cola)==5:
            print("Ya se ha creado una cola anteriormente!")
            opciones();
        
        else:
            metodocreate();
            opciones();
            
    if(e==2):
        
        if len(cola)==5:
                        
            metodopushjojo();
            opciones();
        else:
            print("No se ha creado una cola anteriormente!")            
            opciones();
    
#    if (e==3):
        
        #if len(cola)==5:                         
                                       
                #metodopopjojo();
                
                #opciones();
          
        
        #else:
            #print("No se ha creado una cola anteriormente")
            #opciones();
        
        
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
       




opciones();



