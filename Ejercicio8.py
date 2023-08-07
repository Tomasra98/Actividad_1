#Crear una función que invierta el orden de los elementos en una lista dada

#Se lee la lista desde la entrada del usuario

linea = input("Ingresa los números separados por espacios: ")
partes = linea.split()
mi_lista = [int(parte) for parte in partes]

def invertir_lista(lista):
    return lista[::-1]

# La notación lista[::-1] significa “tomar todos los elementos de la lista, desde el principio hasta el final, en pasos de -1”. Esto produce una nueva lista con los elementos en orden inverso.

lista_invertida = invertir_lista(mi_lista)
print(f"La lista invertida es: {lista_invertida}")