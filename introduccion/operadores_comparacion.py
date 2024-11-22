#Operadores

a = 8
b = 10
c = 10

print("Son iguales " + str(a == b))
print("a es menor que b " + str(a < b))
print("a es mayor que b " + str(a > b))
print("a es menor o es igual a b " + str(a <= b))
print("a es mayor o es igual a b " + str(a >= b))
print("a es diferente que b " + str(a != b))

#Comparacion y
print("Si a es menor que b y a es menor que c: " + str(a < b and a < c))

#Comparando o
print("Si a es menor que b o a es menor que c: " + str(a < b and a < c))

if(a > b):
    print("El mayor es a: " + str(a))
elif(a == b):
    print("ambos son iguales " + str(a))
else:
    print("El mayor es: " + str(b))