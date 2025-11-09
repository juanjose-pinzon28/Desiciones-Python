precio = int(input("Ingrese el precio de su articulo: "))
tipo = input("Ingrese el tipo de su articulo: ")

if tipo == 'textil':
    print("Su articulo no tiene descuento, el valor de su articulo es:",precio)
else:
    if tipo == 'electrodomestico':
        precio = precio-(precio*0.037)
        print("Su articulo tiene el 3.7% de descuento, el valor de su articulo es:",precio)
    else:
        if tipo == 'cocina':
            precio = precio-(precio*0.042)
            print("El valor de su articulo tiene el 4.2% de descuento, el valor de su articulo es:",precio)
        else:
            if tipo == 'videojuego':
                precio = precio-(precio*0.078)
                print("EL valor de su articulo tiene el 7.8% de descuento, el valor de su articulo es:",precio)
