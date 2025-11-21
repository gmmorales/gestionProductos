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

# Crear tabla productos si no existe
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


def editar_producto():
    """Edita un producto existente por su ID"""
    print("\n=== Editar producto ===")

    # Mostrar todos los productos antes de editar
    mostrar_productos()

    # Seleccionar ID
    while True:
        try:
            id_prod = int(input("\nIngrese el ID del producto que desea editar: "))
            break
        except ValueError:
            print("❌ Error: Ingrese un número válido.")

    conn = obtener_conexion()
    cursor = conn.cursor()

    # Buscar producto
    cursor.execute("""
        SELECT id, nombre, descripcion, cantidad, precio, categoria 
        FROM productos 
        WHERE id = ?
    """, (id_prod,))
    producto = cursor.fetchone()

    if not producto:
        print("❌ No existe un producto con ese ID.")
        conn.close()
        return

    # Datos actuales
    id_actual, nombre_act, desc_act, cant_act, precio_act, cat_act = producto

    print("\n=== Datos actuales del producto ===")
    print(f"Nombre: {nombre_act}")
    print(f"Descripción: {desc_act}")
    print(f"Cantidad: {cant_act}")
    print(f"Precio: {precio_act}")
    print(f"Categoría: {cat_act}")

    print("\nPresiona ENTER para mantener el valor actual.")

    # Nuevo nombre
    nuevo_nombre = input(f"Nuevo nombre ({nombre_act}): ").strip()
    if not nuevo_nombre:
        nuevo_nombre = nombre_act

    # Nueva descripción
    nueva_desc = input(f"Nueva descripción ({desc_act}): ").strip()
    if not nueva_desc:
        nueva_desc = desc_act

    # Nueva categoría
    nueva_cat = input(f"Nueva categoría ({cat_act}): ").strip()
    if not nueva_cat:
        nueva_cat = cat_act

    # Nueva cantidad
    while True:
        nueva_cant = input(f"Nueva cantidad ({cant_act}): ").strip()
        if not nueva_cant:
            nueva_cant = cant_act
            break
        try:
            nueva_cant = int(nueva_cant)
            break
        except ValueError:
            print("❌ Error: Ingrese un número válido.")

    # Nuevo precio
    while True:
        nuevo_precio = input(f"Nuevo precio ({precio_act}): ").strip()
        if not nuevo_precio:
            nuevo_precio = precio_act
            break
        try:
            nuevo_precio = float(nuevo_precio)
            break
        except ValueError:
            print("❌ Error: Ingrese un precio válido.")

    # Actualizar en la base
    cursor.execute("""
        UPDATE productos
        SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria = ?
        WHERE id = ?
    """, (nuevo_nombre, nueva_desc, nueva_cant, nuevo_precio, nueva_cat, id_prod))

    conn.commit()
    conn.close()

    print(f"\n✅ Producto ID {id_prod} actualizado correctamente.")


def buscar_producto():
    """Busca productos por ID, nombre o categoría"""
    print("\n=== Buscar producto ===")
    print("Puede buscar por:")
    print("1. ID")
    print("2. Nombre")
    print("3. Categoría")

    opcion = input("Seleccione una opción (1-3): ").strip()

    conn = obtener_conexion()
    cursor = conn.cursor()

    # ============================
    # Buscar por ID
    # ============================
    if opcion == "1":
        try:
            id_buscar = int(input("Ingrese el ID a buscar: "))
        except ValueError:
            print("❌ Debe ingresar un número válido.")
            conn.close()
            return

        cursor.execute("""
            SELECT id, nombre, descripcion, cantidad, precio, categoria
            FROM productos
            WHERE id = ?
        """, (id_buscar,))

        resultado = cursor.fetchone()
        conn.close()

        if resultado:
            id_, nombre, desc, cant, precio, cat = resultado
            print("\n=== Resultado ===")
            print(f"ID: {id_} | Nombre: {nombre} | Descripción: {desc} | Cantidad: {cant} | Precio: {precio} | Categoría: {cat}")
        else:
            print("❌ No se encontró un producto con ese ID.")

    # ============================
    # Buscar por Nombre
    # ============================
    elif opcion == "2":
        nombre_buscar = input("Ingrese el nombre o parte del nombre: ").strip().lower()

        cursor.execute("""
            SELECT id, nombre, descripcion, cantidad, precio, categoria
            FROM productos
            WHERE LOWER(nombre) LIKE ?
        """, ('%' + nombre_buscar + '%',))

        resultados = cursor.fetchall()
        conn.close()

        if resultados:
            print("\n=== Resultados ===")
            for p in resultados:
                id_, nombre, desc, cant, precio, cat = p
                print(f"{id_}. Nombre: {nombre} | Desc: {desc} | Cantidad: {cant} | Precio: ${precio} | Categoría: {cat}")
        else:
            print("❌ No se encontraron productos que coincidan con el nombre.")

    # ============================
    # Buscar por Categoría
    # ============================
    elif opcion == "3":
        categoria_buscar = input("Ingrese la categoría: ").strip().lower()

        cursor.execute("""
            SELECT id, nombre, descripcion, cantidad, precio, categoria
            FROM productos
            WHERE LOWER(categoria) = ?
        """, (categoria_buscar,))

        resultados = cursor.fetchall()
        conn.close()

        if resultados:
            print("\n=== Resultados ===")
            for p in resultados:
                id_, nombre, desc, cant, precio, cat = p
                print(f"{id_}. Nombre: {nombre} | Desc: {desc} | Cantidad: {cant} | Precio: ${precio} | Categoría: {cat}")
        else:
            print("❌ No se encontraron productos en esa categoría.")

    else:
        print("❌ Opción no válida.")
        conn.close()


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


def reporte_bajo_stock():
    """Muestra productos con cantidad menor o igual a un límite dado por el usuario."""
    print("\n=== Reporte de productos con bajo stock ===")

    # Pedir límite
    while True:
        try:
            limite = int(input("Ingrese el límite de cantidad: "))
            if limite < 0:
                print("❌ El límite no puede ser negativo.")
            else:
                break
        except ValueError:
            print("❌ Debe ingresar un número entero válido.")

    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, nombre, descripcion, cantidad, precio, categoria
        FROM productos
        WHERE cantidad <= ?
        ORDER BY cantidad ASC
    """, (limite,))

    resultados = cursor.fetchall()
    conn.close()

    # Mostrar reporte
    if not resultados:
        print(f"\nNo hay productos con cantidad menor o igual a {limite}.")
        return

    print(f"\nProductos con cantidad <= {limite}:")
    print("-" * 60)

    for p in resultados:
        id_, nombre, desc, cant, precio, cat = p
        print(
            f"ID: {id_} | Nombre: {nombre} | Cantidad: {cant} | "
            f"Precio: ${precio} | Categoría: {cat}"
        )

    print("-" * 60)
    print(f"Total de productos encontrados: {len(resultados)}")


def salir():
    """Salir de la app"""
    print("Saliendo del programa...")


def mostrar_menu():
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Editar producto")
    print("5. Eliminar producto")
    print("6. Reporte de bajo stock")
    print("7. Salir")


# ============================
# MÉTODO MAIN()
# ============================
def main():
    inicializar_bd()  # Crear la tabla si no existe

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-7): ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            editar_producto()
        elif opcion == "5":
            eliminar_producto()
        elif opcion == "6":
            reporte_bajo_stock()
        elif opcion == "7":
            salir()
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

if __name__ == "__main__":
    main()
