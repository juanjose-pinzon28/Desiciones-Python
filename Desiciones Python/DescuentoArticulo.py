precio = int(input("Ingrese el precio de su articulo: "))
tipo = int(input("Ingrese el tipo de su articulo: "))

if tipo == 1:
    precio = precio -(precio*0.125)
    print("El descuento agregado es de el 12.5%, su valor con descuento es: ",precio)
else:
    if tipo == 2:
        precio= precio-(precio*0.083)
        print("El descuento agregado es de el 8.3%, su valor con descuento es: ",precio)
    else:
        if tipo == 3:
            precio= precio-(precio*0.032)
            print("El descuento agregado es de el 3.2%, su valor con descuento es: ",precio)
        
        
