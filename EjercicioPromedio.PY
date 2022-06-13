'''Se solicita hacer un bucle y cuando el usuario finalice de cargar datos sacar el promedio total'''

i = 0
suma = 0
promedio = 0

numero = int(input("Ingrese un numero para comenzar el programa, para finalizar ingrese 0"))


while numero != 0:
    print("Se ingreso el numero: ", numero)

    suma = suma + numero
    i = i+1

    numero = int(input("Ingrese un numero para comenzar el programa, para finalizar ingrese 0"))

promedio = (suma/i)
print ("La suma total es: ", suma)
print ("Se divide por: " , i)
print ("El promedio de todos los numeros ingresados es:", promedio)
