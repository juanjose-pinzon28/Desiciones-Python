tanque = float(input("Ingrese cuantos litros tiene el tanque: "))

if tanque<250:
    print("Abra la llave")
else:
    if tanque>= 250 and tanque <=450:
        print("Mantenga la llave abierta ")
    else:
        print("Cierre la llave")
        
