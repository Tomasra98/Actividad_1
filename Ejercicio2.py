#Escribir una función que calcule el área de un círculo dado su radio

import math

def area_circulo(radio):
    return math.pi * radio ** 2

radio = int(input("Ingrese radio del circulo: "))
area = area_circulo(radio)
print(f"El área del círculo con radio {radio} es {area:.2f}")