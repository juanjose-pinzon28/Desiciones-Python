genero = input("Ingrese el genero del aspirante (hombre/mujer): ")
estatura = float(input("Ingrese la estatura del aspirante: "))
edad = int(input("Ingrese la edad del aspirante: "))
estadoCivil = input("Ingrese el estado civil del aspirante (soltero/casado): ")

if estadoCivil == "soltero":
    if genero == "mujer":
        if (estatura>1.60) and (edad>=20) and (edad<=25):
            print("La aspirante es apta para ingresar al ejercito")
        else:
            print("La aspirante no es apta para ingresar al ejercito")
    else:
        if genero == "hombre":
            if (estatura > 1.65) and (edad>=18) and (edad<=24):
                print("El aspirante es apto para ingresar al ejercito")
            else:
                print("El aspirante no es apto para ingresar al ejercito")
else:
    print("El aspirante debe ser soltero para ingresar al ejercito")


