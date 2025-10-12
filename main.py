#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Gustavo
Descripción: Sistema de gestión básica de productos
"""
# Variables globales
productos = []

# Sección de la funciones principales
def agregar_producto():
    '''Agrega un producto'''
    print("\n=== Agregar producto ===")

    # Validar nombre
    while True:
        nombre = input("Ingrese el nombre del producto: ").strip()
        if nombre:
            break
        print("❌ El nombre no puede estar vacío.")

    # Validar categoría
    while True:
        categoria = input("Ingrese la categoría: ").strip()
        if categoria:
            break
        print("❌ La categoría no puede estar vacía.")

    # Validar precio (entero positivo)
    while True:
        try:
            precio = int(input("Ingrese el precio: "))
            if precio < 0:
                print("❌ El precio no puede ser negativo.")
            else:
                break
        except ValueError:
            print("❌ Error: Debe ingresar un número entero para el precio.")

    # Guardar el producto en la lista
    producto = [nombre, categoria, precio]
    productos.append(producto)
    print(f"✅ Producto '{nombre}' agregado correctamente.")

def mostrar_productos():
    '''Muestra los productos'''
    print("\n=== Lista de productos ===")
    if not productos:
        print("No hay productos registrados.")
        return

    for i, producto in enumerate(productos, start=1):
        nombre, categoria, precio = producto
        print(f"{i}. Nombre: {nombre} | Categoría: {categoria} | Precio: ${precio}")

def buscar_producto():
    '''Búsca un producto'''
    print("Has seleccionado: Buscar producto")

def eliminar_producto():
    '''Elimina un producto'''
    print("\n=== Eliminar producto ===")

    # Verificar si hay productos cargados
    if not productos:
        print("No hay productos para eliminar.")
        return

    # Mostrar los productos disponibles
    for i, producto in enumerate(productos, start=1):
        nombre, categoria, precio = producto
        print(f"{i}. Nombre: {nombre} | Categoría: {categoria} | Precio: ${precio}")

    # Pedir el número del producto a eliminar
    while True:
        try:
            indice = int(input("Ingrese el número del producto que desea eliminar: "))
            if 1 <= indice <= len(productos):
                producto_eliminado = productos.pop(indice - 1)
                print(f"✅ Producto '{producto_eliminado[0]}' eliminado correctamente.")
                break
            else:
                print(f"❌ Debe ingresar un número entre 1 y {len(productos)}.")
        except ValueError:
            print("❌ Error: Ingrese un número válido.")

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