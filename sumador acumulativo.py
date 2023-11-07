#este programa 
def suma():
  num_final=input("dime hasta que numero quieres que sume: ")
  suma_acumulada=0
  for cont in range(1,int(num_final)+1):
    #print("esta vez cont= "+str(cont))
    suma_acumulada=suma_acumulada+cont
  print("suma acumulada = "+str(suma_acumulada))
  
suma()
