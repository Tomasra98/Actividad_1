#Crear un programa que calcule la suma de los números en una lista dada

def suma_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

# Leer la lista desde la entrada del usuario

linea = input("Ingresa los números separados por espacios: ")
partes = linea.split()
mi_lista = [int(parte) for parte in partes]

# Calcular la suma

resultado = suma_lista(mi_lista)
print(f"La suma de los números de la lista es {resultado}")
