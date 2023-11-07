def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

while True:
    print("Operaciones disponibles:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Salir")
    
    opcion = input("Elija una opción (1/2/3): ")
    
    if opcion == "3":
        print("¡Hasta luego!")
        break
    
    if opcion not in ["1", "2"]:
        print("Opción no válida. Por favor, elija 1 para sumar o 2 para restar.")
        continue
    
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    
    if opcion == "1":
        resultado = suma(num1, num2)
        print(f"La suma de {num1} y {num2} es: {resultado}")
    elif opcion == "2":
        resultado = resta(num1, num2)
        print(f"La resta de {num1} y {num2} es: {resultado}")
