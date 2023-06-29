from catalogo import *
import random as rn
import numpy as np


#############
def Grabar_libro(lista_libros):
    blib = libro()

    c = False
    while c == False:
        c = blib.selfCodigo(input("ingrese codigo de libro(AAA-123): "))

    blib.titulo = input("Ingrese titulo del libro: ")

    blib.autor = input("Ingrese nombre del autor: ")

    c = False
    while c == False:
        try:
            c = blib.selfPrecio(int(input("Ingrese Precio: ")))
        except BaseException as error:
            print(f"error {error}")

    blib.pais = input("ingrese pais de origen del libro: ")

    c = False
    while c == False:
        c = blib.selfFecha(input("Ingrese fecha del libro: "))

    blib.categoria = input("Ingrese la categoria del libro: ")

def buscar_libro(lista_libros):
    alib = libro
    input("ingrese codigo de libro")

############
lista_libros = np.array
ciclo = True
while ciclo:
    print("Libreria 'Mayor'")
    print("1) Grabar libro")
    print("2) Buscar libro")
    print("3) Imprimir informe")
    print("4) salir")
    op = int(input("Seleccione 1-4: "))
    try:
        match op:
            case 1:
                print("Grabar libro")
                Grabar_libro(lista_libros)
            case 2:
                print("Buscar libro")
                buscar_libro()
            case 3:
                print("Imprimir informe")
            case 4:
                print("Salir")
                ciclo = False
            case _:
                print("opcion invalida")
    except BaseException as error:
        print(f"error {error}")
