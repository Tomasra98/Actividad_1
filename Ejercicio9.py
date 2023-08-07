#Crear un programa que genere una matriz de números y la imprima en pantalla

import random

def generar_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(random.randint(1, 100))
        matriz.append(fila)
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

matriz = generar_matriz(7, 8)
imprimir_matriz(matriz)