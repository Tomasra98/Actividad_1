#Escribir un programa que encuentre el número más grande y el más pequeño en una lista dada

# Primero leemos la lista desde la entrada del usuario

linea = input("Ingresa los números separados por espacios: ")
partes = linea.split()
mi_lista = [int(parte) for parte in partes]

def max_min_lista(lista):
    maximo = max(lista)
    minimo = min(lista)
    return maximo, minimo

maximo, minimo = max_min_lista(mi_lista)
print(f"El número más grande en la lista es {maximo}")
print(f"El número más pequeño en la lista es {minimo}")