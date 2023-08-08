#Crear un programa que genere una lista de números pares entre 1 y 100

numeros_pares = []
for i in range(1, 101):
    if i % 2 == 0:
        numeros_pares.append(i)
print(numeros_pares)