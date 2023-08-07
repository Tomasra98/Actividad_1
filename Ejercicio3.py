#Crear un programa que genere una lista de números aleatorios y los imprima en pantalla

import random

def generar_lista_aleatoria(longitud, minimo, maximo):
    lista = []
    for i in range(longitud):
        lista.append(random.randint(minimo, maximo))
    return lista

longitud = 8
minimo = 1
maximo = 50

numeros_aleatorios = generar_lista_aleatoria(longitud, minimo, maximo)
print(numeros_aleatorios)