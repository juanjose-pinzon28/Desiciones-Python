nota = float(input("Ingrese la nota definitiva: "))

if nota < 3.0:
    print("Su nota es insuficiente")
else:
    if nota <= 3.5:
        print("Su nota es aceptable")
    else:
        if nota <= 4.0:
            print("Su nota es sobresaliente")
        else:
            print("Su nota es excelente")
