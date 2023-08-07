#Escribir un programa que determine si un número dado es par o impar

def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

numero = int(input("Ingrese un número bro: "))
if es_par(numero):
    print(f"{numero} es un número par")
else:
    print(f"{numero} es un número impar")