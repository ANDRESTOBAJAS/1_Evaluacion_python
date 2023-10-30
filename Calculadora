def mostrarMenu():
    print("***********************************")
    print("*        SUPERCALCULADORA         *")
    print("***********************************")
    print("ELIJA UNA DE LAS SIGUIENTES OPCIONES:")
    print("1. SUMAR")
    print("2. RESTAR")
    print("3. MULTIPLICAR")
    print("4. DIVIDIR")
    print("____________________________________")
    respuesta = input("ELIJA (1, 2, 3 o 4): ")
    return respuesta

def sumarNumeros(num1, num2):
    respuesta = num1 + num2
    return respuesta

def restarNumeros(num1, num2):
    respuesta = num1 - num2
    return respuesta

def multiplicarNumeros(num1, num2):
    respuesta = num1 * num2
    return respuesta

def dividirNumeros(num1, num2):
    if num2 != 0:
        respuesta = num1 / num2
        return respuesta
    else:
        print("No es posible dividir por cero.")
        return None

def calculadora():
    num1 = float(input("Numero 1: "))
    num2 = float(input("Numero 2: "))

    opcion = mostrarMenu()

    if opcion == '1':
        respuesta = sumarNumeros(num1, num2)
    elif opcion == '2':
        respuesta = restarNumeros(num1, num2)
    elif opcion == '3':
        respuesta = multiplicarNumeros(num1, num2)
    elif opcion == '4':
        respuesta = dividirNumeros(num1, num2)
    else:
        print("Opción no válida")
        return

    if respuesta is not None:
        print("Resultado =", respuesta)

calculadora()
