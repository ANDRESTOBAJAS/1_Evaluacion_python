#Haz un programa que lea un numero y te duvukeva la suma de sus cifras, tratando el numero como un numero natural.
#Ejemplo:
#Si leemos 123 la suma de sus cifras es 6.
#Si leemos 5 la suma de sus cifras es 5.

numero = int(input("Ingrese un número: "))

suma_cifras = 0

while numero > 0:
    cifra = numero % 10
    suma_cifras += cifra
    numero //= 10

print("La suma de las cifras es:", suma_cifras)
