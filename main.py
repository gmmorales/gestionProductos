#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Gustavo
Descripción: Sistema de gestión básica de productos
"""

# Sección de la funciones principales
def agregar_producto():
    '''Agrega un producto'''
    print("Has seleccionado: Agregar producto")

def mostrar_productos():
    '''Muestra los productos'''
    print("Has seleccionado: Mostrar productos")

def buscar_producto():
    '''Búsca un producto'''
    print("Has seleccionado: Buscar producto")

def eliminar_producto():
    '''Elimina un producto'''
    print("Has seleccionado: Eliminar producto")

def salir():
    '''Salgo de la app'''
    print("Saliendo del programa...")

def mostrar_menu():
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")


# Método main()

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ")


        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            salir()
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

if __name__ == "__main__":
    main()