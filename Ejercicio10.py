#Escribir una función que calcule el factorial de un número dado

n = int(input("Escriba un número cualquiera: "))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(n))