#Crear una función que convierta grados Fahrenheit a grados Celsius

def fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Ejemplo de uso de la función

temperatura_fahrenheit = int(input("Digite una temperatura: "))
temperatura_celsius = fahrenheit_a_celsius(temperatura_fahrenheit)
print(temperatura_fahrenheit, "grados Fahrenheit son", temperatura_celsius, "grados Celsius.")
