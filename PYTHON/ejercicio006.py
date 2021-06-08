#ingrese un numero y elija si es par o impar
numero = int(input("Ingrese un número: "))
if numero == 0 : #si el numero es igual a cero
    print ("Es Cero")
elif numero % 2 == 0 : #caso contrario si el numero mod 2 es cero
    print ("El número es Par")
else: #caso contrario
    print ("El número es Impar")

