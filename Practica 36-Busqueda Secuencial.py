#tenemos un arreglo con las siguientes letras:
arreglo1=['N',"u","n","c","a",'m',"e","r","e","n","d","i","r","e"]

#definimos nuestro metodo de busqueda secuencial, que recibe un puntero
#y el dato a buscar en el arreglo
def busquedasecuencial(i,dato):
    #primero comparamos si el puntero es menor a la longitud del arreglo
    if (i<len(arreglo1)):
     #de ser así (que significa que aun no llegamos al ultimo elemento)
     #comparamos entonces el dato a buscar con el elemento almacenado
     #en la posicion de i en el arreglo:
        if (dato==arreglo1[i]):
            #de ser iguales, hemos encontrado el dato
            #en el arreglo
            print ("Dato encontrado")
            print ("En la posicion")
            print(i)
        #si no son iguales, movemos el puntero a la siguiente posicion
        #del arreglo y usamos recursividad para volver a llamar al metodo
        #hasta encontrarlo o no encontrarlo
        else:
            i+=1
            busquedasecuencial(i,dato);
    #una vez que el puntero ya no es menor que la longitud del arreglo
    #es decir, que se encuentra en la ultima posición del mismo
    #entonces imprimimos el siguiente mensaje:            
    else:
        print("No se encontro el elemento deseado en la busqueda")
        
        
#creamos nuestro puntero i con el valor inicial de 0
i=0
#pedimos la entrada del dato que el usuario desea buscar en el arreglo
print("Introduzca un dato que desea buscar en el arreglo")
dato=input()
#lo campturamos, imprimimos el arreglo y luego ejecutamos
#nuestro metodo de busqueda
print(arreglo1)
busquedasecuencial(i,dato);
