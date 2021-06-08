"""
STRING y mas!
"""
esto_es_una_string = "Hola"
esto_es_otra_string = "Mundo"

#Concatenar
print(esto_es_una_string +' '+ esto_es_otra_string)

#hola mundo
#MAYUS
print (esto_es_una_string.upper())
#minus
print (esto_es_una_string.lower())
#Primera Mayuscula
print (esto_es_una_string.capitalize())
#Poner mayuscula en cada palabra
print (esto_es_una_string.title())
#me dice la longitud
print(len(esto_es_una_string))
#buscar una caracter y muestra su ubicacion en indice
print(esto_es_una_string.find('l'))
#Imprimir solo la primera letra SLICE
print(esto_es_una_string[0:2]) # ho tu le dices que inicie en cero
print(esto_es_una_string[:2]) # ho asume que inicia en cero
print(esto_es_una_string[3:4]) # 
#Radar poner al reves una palabra
print(esto_es_una_string[::-1])

