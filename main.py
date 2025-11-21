#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Gustavo
Descripción: Sistema de gestión básica de productos con SQLite
"""

import sqlite3

# ================================
# FUNCIÓN DE CONEXIÓN A LA BASE
# ================================
def obtener_conexion():
    """Devuelve una conexión a la base de datos SQLite."""
    return sqlite3.connect("inventario.db")

# Crear tabla si no existe
def inicializar_bd():
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL,
            categoria TEXT
        )
    """)
    conn.commit()
    conn.close()

# ============================================
# SECCIÓN DE FUNCIONES PRINCIPALES
# ============================================

def agregar_producto():
    """Agrega un producto a la base de datos"""
    print("\n=== Agregar producto ===")

    # Validar nombre
    while True:
        nombre = input("Ingrese el nombre del producto: ").strip()
        if nombre:
            break
        print("❌ El nombre no puede estar vacío.")

    descripcion = input("Ingrese la descripción (opcional): ").strip()

    # Validar categoría
    while True:
        categoria = input("Ingrese la categoría: ").strip()
        if categoria:
            break
        print("❌ La categoría no puede estar vacía.")

    # Validar cantidad
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad: "))
            if cantidad < 0:
                print("❌ La cantidad no puede ser negativa.")
            else:
                break
        except ValueError:
            print("❌ Error: Debe ingresar un número entero para la cantidad.")

    # Validar precio
    while True:
        try:
            precio = float(input("Ingrese el precio: "))
            if precio < 0:
                print("❌ El precio no puede ser negativo.")
            else:
                break
        except ValueError:
            print("❌ Error: Debe ingresar un número para el precio.")

    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria) VALUES (?, ?, ?, ?, ?)",
        (nombre, descripcion, cantidad, precio, categoria)
    )

    conn.commit()
    conn.close()

    print(f"✅ Producto '{nombre}' agregado correctamente.")


def mostrar_productos():
    """Muestra todos los productos"""
    print("\n=== Lista de productos ===")

    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, descripcion, cantidad, precio, categoria FROM productos")
    productos = cursor.fetchall()
    conn.close()

    if not productos:
        print("No hay productos registrados.")
        return

    for p in productos:
        id_, nombre, descripcion, cantidad, precio, categoria = p
        print(f"{id_}. Nombre: {nombre} | Desc: {descripcion} | Cantidad: {cantidad} | Precio: ${precio} | Categoría: {categoria}")


def buscar_producto():
    """Busca productos por nombre"""
    print("\n=== Buscar producto ===")

    busqueda = input("Ingrese el nombre del producto a buscar: ").strip().lower()

    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, nombre, descripcion, cantidad, precio, categoria
        FROM productos
        WHERE LOWER(nombre) LIKE ?
    """, ('%' + busqueda + '%',))

    resultados = cursor.fetchall()
    conn.close()

    if resultados:
        print(f"\nSe encontraron {len(resultados)} resultado(s):")
        for p in resultados:
            id_, nombre, descripcion, cantidad, precio, categoria = p
            print(f"{id_}. Nombre: {nombre} | Desc: {descripcion} | Cantidad: {cantidad} | Precio: ${precio} | Categoría: {categoria}")
    else:
        print("❌ No se encontraron productos que coincidan con la búsqueda.")


def eliminar_producto():
    """Elimina un producto por ID"""
    print("\n=== Eliminar producto ===")

    mostrar_productos()

    while True:
        try:
            id_prod = int(input("Ingrese el ID del producto a eliminar: "))
            break
        except ValueError:
            print("❌ Error: Ingrese un número válido.")

    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute("SELECT nombre FROM productos WHERE id = ?", (id_prod,))
    producto = cursor.fetchone()

    if not producto:
        print("❌ No existe un producto con ese ID.")
        conn.close()
        return

    cursor.execute("DELETE FROM productos WHERE id = ?", (id_prod,))
    conn.commit()
    conn.close()

    print(f"✅ Producto '{producto[0]}' eliminado correctamente.")


def salir():
    """Salir de la app"""
    print("Saliendo del programa...")


def mostrar_menu():
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")


# ============================
# MÉTODO MAIN()
# ============================
def main():
    inicializar_bd()  # Crear la tabla si no existe

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
