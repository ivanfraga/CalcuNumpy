import numpy
import sys

Fila1 = 0
Fila2 = 0
Columna1 = 0
Columna2 = 0

print(" ===============================================================")

print("|       BIENVENIDO AL SISTEMA DE MULTIPLICACIÓN DE MATRICES    |")
print(" ===============================================================")

while True:

    try:
        Fila1 = int(input('\n\n*Ingrese las filas de la primera matriz :'))
        break

    except ValueError:
        print("\n\n***************\n\n")
        print("Error, el sistema solo admite numeros  ")
        print("\n\n***************\n\n")

while True:
    try:
        Columna1 = int(input('*Ingrese las colunmas de la primera matriz:'))
        break
    except ValueError:
        print("\n\n***************\n\n")
        print("Error, el sistema solo admite numeros  ")
        print("\n\n***************\n\n")
while True:
    try:
        Fila2 = int(input('*Ingrese las filas de la segunda matriz:'))
        break
    except ValueError:
        print("\n\n***************\n\n")
        print("Error, el sistema solo admite numeros  ")
        print("\n\n***************\n\n")
while True:
    try:
        Columna2 = int(input('*Ingrese las colunmas de la segunda matriz:'));
        break
    except ValueError:
        print("\n\n***************\n\n")
        print("Error, el sistema solo admite numeros  ")
        print("\n\n***************\n\n")

# Verificacion de entrada d valores del tamaño de las matrices

while Columna1 != Fila2:
    print("\n[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]][[[[[[[[[[[[[[[[[[[[\n")
    print(
        "Datos inconrrectos , o el tamaño de las matrices son diferentes \n  Por favor vuelve a ingresarlos!!!!!!!!!\n")
    print(" \n[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]\n")

    while True:

        try:
            Fila1 = int(input('-Ingrese las filas de la primera matriz :'))
            break

        except ValueError:
            print("\n\n***************\n\n")
            print("Error, el sistema solo admite numeros  ")
            print("\n\n***************\n\n")

    while True:
        try:
            Columna1 = int(input('-Ingrese las colunmas de la primera matriz:'))
            break
        except ValueError:
            print("\n\n***************\n\n")
            print("Error, el sistema solo admite numeros  ")
            print("\n\n***************\n\n")
    while True:
        try:
            Fila2 = int(input('-Ingrese las filas de la segunda matriz:'))
            break
        except ValueError:
            print("\n\n***************\n\n")
            print("Error, el sistema solo admite numeros  ")
            print("\n\n***************\n\n")
    while True:
        try:
            Columna2 = int(input('-Ingrese las colunmas de la segunda matriz:'));
            break
        except ValueError:
            print("\n\n***************\n\n")
            print("Error, el sistema solo admite numeros  ")
            print("\n\n***************\n\n")

print("\n\nIngreso correctamente el tamaño de las matrices:")

matriz1 = numpy.zeros((Fila1, Columna1))
matriz2 = numpy.zeros((Fila2, Columna2))
matrizr = numpy.zeros((Fila1, Columna2))

print("Introduzca los valores de la 1 matriz")
for r in range(0, Fila1):
    for c in range(0, Columna1):
        while True:
            try:
                matriz1[r, c] = (input("Elemento a [" + str(r + 1) + "," + str(c + 1) + "] : "))
                break
            except ValueError:
                print("\n\n***************\n\n")
                print("Error, el sistema solo admite numeros  ")
                print("\n\n***************\n\n")

print("\nIntroduzca los valores de la 2 matriz")
for r in range(0, Fila2):
    for c in range(0, Columna2):
        while True:
            try:
                matriz2[r, c] = input("Elemento a [" + str(r + 1) + "," + str(c + 1) + "] : ")
                break
            except ValueError:
                print("\n\n***************\n\n")
                print("Error, el sistema solo admite numeros  ")
                print("\n\n***************\n\n")

# procedimiento de la multiplicacion
for r in range(0, Fila1):
    for c in range(0, Columna2):
        for k in range(0, Fila1):
            matrizr[r, c] += matriz1[r, k] * matriz2[k, c]
print("\n\n El resultado es : \n")
print(matrizr)
