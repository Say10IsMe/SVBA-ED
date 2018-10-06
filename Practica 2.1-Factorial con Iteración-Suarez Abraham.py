
#pedimos la ingresión de un numero para calcular su factorial
num = int(input("Ingresa un numero: "))
#establecemos la variable factorial como 1
factorial = 1
#iniciamos in ciclo for con rango determinado por el numero que el usuario
#ingresó
for i in range(num):
    #se muestra en pantalla la multiplicación del factorial por el numero ingresado
    #y se re-asigna a la variable factorial el resultado de dicha multiplicación
    #entonces, se resta al numero ingresado del usuario una unidad
    print (factorial, " * " , num)
    factorial = factorial * num
    num = num - 1 
#se imprime entonces el valor del factorial hasta que el ciclo for cumpla todas
    #sus iteraciones
print (factorial)
    
    