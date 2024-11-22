def saludo():
    print("Hola bienvenido")
    print("Saludos desde python")

print("Esto es una funcion")
saludo()

def suma(a,b):
    resultado = a + b
    print("La suma es: " + str(resultado))

suma(8,4)

def datos(nom, ap, am):
    print("tu nombre es: {} {} {}".format(nom, ap, am))

datos("Juan", "Navarro", "Quintero")

def suma2(*args):
    resultado = 0
    for n in args:
        resultado += n
    return resultado

print("La suma total es: {}".format(suma2(5,9,15)))