a= float(input("Ingrese el valor de a: "))
b= float(input("Ingrese el valor de b: "))
c= float(input("Ingrese el valor de c: "))
import math

discriminante= b**2 - 4*(a*c)

x1= (-b + math.sqrt(discriminante))/(2*a)
x2= (-b - math.sqrt(discriminante))/(2*a)

if discriminante>0 and a!=0:
    print("Su ecuacion cuadratica tiene solucion y es:", x1 , x2)
else:
    print("Su ecuacion Cuadratica no tiene solucion")
