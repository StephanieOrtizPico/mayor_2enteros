# Programa para verificar cual de dos números enteros es el mayor

# input
x = int(input ("Digite el primer número: "))
y = int(input ("Digite el segundo número: "))

# processing 
if x == y:
    # output
    print("Los números son iguales...")
else:
    if x > y:
        mayor = x
    else:
        mayor = y
# output
print("El número mayor entre " +str(x)+ " y " +str(y)+ " es " +str(mayor))
