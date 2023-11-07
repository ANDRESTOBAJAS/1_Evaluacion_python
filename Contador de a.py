def contador_aes():
  #leemos una palabra 
  palabra=input("Dime una palabra: ")
  #inicializamos la variable que almacenara el numero 3
  numeroaes=0
  #recorremos la palabra y buscamos las letras a
  for cont in range(0,len(palabra)): 
    if palabra[cont]== "A" or palabra[cont]=="a":
      numeroaes=numeroaes+1  
  #mostramos el numero de aes contadas
  print("La palabra "+palabra+" tiene "+str(numeroaes)+" a ")

contador_aes()

#Update
def contador_aes():
    # Leemos una palabra
    palabra = input("Dime una palabra: ")
    
    # Inicializamos la variable que almacenará el número de 'a's
    numero_aes = 0
    
    # Convertimos la palabra a minúsculas para contar ambas 'A' y 'a'
    palabra = palabra.lower()
    
    # Recorremos la palabra y buscamos las letras 'a'
    for letra in palabra:
        if letra == 'a':
            numero_aes += 1
    
    # Mostramos el número de 'a's contadas
    print(f"La palabra '{palabra}' tiene {numero_aes} 'a's.")

contador_aes()
  
