
#definimos el metodo numeros naturales el cual recibe un parametro y regresa
#uno al mismo tiempo
def numerosnaturales(x):
    #la condicion de detencion para la recursividad es esta, cuando x alcance
    #el valor tope, se detendra, en esta caso es 101 ya que el numero maximo
    #que queremos es 100
    if x<101:
        #imprime el valor inicial y enseguida lo incrementa, despues envia
        #el nuevo valor al mismo metodo y asi sucesivamente hasta que se
        #cumpla la condición
        print(x)
        x=x+1
        return numerosnaturales(x)

print(numerosnaturales(1))

