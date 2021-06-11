# Programa que verifica si una palabra es palindromo

palabra = input("Ingrese una palabra para verificar si es palindromo: ")

print(palabra)
print(palabra[::-1])

if (palabra == palabra[::-1]):
    print("Palindromo")
else:
    print("No es Palindromo")
