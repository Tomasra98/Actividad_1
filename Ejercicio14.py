#Escribir una función que calcule la media aritmética de una lista de números

lista = []
tamaño = int(input("Digite el tamaño de la lista: "))
for i in range(0, tamaño):
    valores = int(input("Escriba un número: "))
    lista.append(valores)

def media_aritmetica(list):
    suma = 0
    for i in range(0, len(list)):
        suma += list[i]
    return suma/len(list)

print("La media aritmetica de la lista es: ", int(media_aritmetica(lista)))