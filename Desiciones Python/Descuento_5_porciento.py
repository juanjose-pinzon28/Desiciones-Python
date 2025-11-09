val = float(input("Ingrese el valor de su articulo: "))

if val>150000:
    descuento = val - (val*0.05)
    print("El valor de su articulo es superior a 150.000 pesos, entonces su valor final con el 5% es de: ",descuento)
else:
    print("El valor de su articulo no es superior a 150.000 pesos, entonces se valor final sin descuento es de: ",val)
    
