lista = []
numero1 = 0
numero2 = 0
opcion = 0
aplicacion = true

def list():
    for i in lista
        imprimir(i)


def imprimir(resul):
    print(resul)


def guardar(resul):
    lista.append(resul)

def suma(var1,var2):
    resul = var1 + var2
    imprimir(resul)
    guardar(resul)

def resta(var1,var2):
    resul = var1 - var2
    imprimir(resul)
    guardar(resul)

def multiplicacion(var1,var2):
    resul = var1 * var2
    imprimir(resul)
    guardar(resul)

def division(var1,var2):
    resul = var1 / var2
    imprimir(resul)
    guardar(resul)
    

while(aplicacion):
    print("Calculadora")
    print("ingresar 1 Suma")
    print("ingresar 2 Resta")
    print("ingresar 3 Multiplicacion")
    print("ingresar 4 Division")
    print("ingresar 5 imprimir lista")
    print("ingresar 6 finalizar aplicacion")
    opcion = int(input("Elija una opcion: " )) 
    numero1 = int(input("ingrese un numero: "))
    numero2 = int(input("ingrese un numero: "))
    match opcion:
        case 1:
             suma(var1,var2)
        case 2:
             resta(var1,var2)
        case 3:
             multiplicacion(var1,var2)
        case 4:
             division(var1,var2)
        case 5:
            aplicacion = false
        case 6:
            aplicacion = false
        case _:
            print("La opcion ingresada no existe ")
