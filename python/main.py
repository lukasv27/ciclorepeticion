#solicitar cantidad de pasajes
#crear ciclo de repeticion 'for'
#solicitar precio de pasajes
#validar con try except
#romper bucle con break
#mostrar info total de pasajes

totalingresos = 0
banderacantidad = True
banderaprecio = True
while banderacantidad:
    try:
       cantidad =int(input("ingrese cantidad de pasajes\n"))
       for x in range (cantidad):
        try:    
          precio = int(input(f"ingrese precio para pasajes n°{x+1} \n"))
          totalingresos = totalingresos + precio
          
        except:
            print(" precio no exite")
        
    except:
     print("opcion no valida")
                
    print (f"para los {cantidad}  pasajes, el valor a pagar es: ${totalingresos}\n")
    