#Crear un programa que pida al usuario ingresar una cadena de texto y determine si es un palíndromo o no

texto = input("Ingresa una cadena de texto: ")
texto = texto.replace(" ", "") # Elimina los espacios en blanco
texto = texto.lower() # Convierte el texto a minúsculas

if texto == texto[::-1]:
    print("La cadena es un palíndromo")
else:
    print("La cadena no es un palíndromo")
