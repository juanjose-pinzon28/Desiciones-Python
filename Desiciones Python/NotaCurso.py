n1 = float(input("Ingrese la primera nota: "))
n2 = float(input("Ingrese la segunda nota: "))
n3 = float(input("Ingrese la tercera nota: "))
n4 = float(input("Ingrese la cuarta nota: "))
n5 = float(input("Ingrese la quinta nota: "))

notaDefinitiva = (n1+n2+n3+n4+n5)/5

if notaDefinitiva>=3.5:
    print("Usted paso el curso con:",notaDefinitiva)
else:
    print("Usted no paso el curso")
