from services.database import obtener_conexion


# ----------------------------------------------------------------------
# AGREGAR PRODUCTO
# ----------------------------------------------------------------------
def agregar_producto():
    """Agrega un producto a la base de datos"""
    print("\n=== Agregar Producto ===")
    nombre = input("Nombre: ")
    descripcion = input("Descripción: ")
    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio: "))
    categoria = input("Categoría: ")

    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
        VALUES (?, ?, ?, ?, ?)
        """,
        (nombre, descripcion, cantidad, precio, categoria)
    )

    conn.commit()
    conn.close()
    print("Producto agregado exitosamente.")


# ----------------------------------------------------------------------
# MOSTRAR PRODUCTOS
# ----------------------------------------------------------------------
def mostrar_productos():
    """Muestra todos los productos"""
    print("\n=== Lista de Productos ===")

    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    conn.close()

    if not productos:
        print("No hay productos cargados.")
        return

    for p in productos:
        print(f"ID: {p[0]} | Nombre: {p[1]} | Descripción: {p[2]} | Cantidad: {p[3]} | Precio: {p[4]} | Categoría: {p[5]}")


# ----------------------------------------------------------------------
# BUSCAR PRODUCTO (por id, nombre o categoría)
# ----------------------------------------------------------------------
def buscar_producto():
    """Busca productos por ID, nombre o categoría"""
    print("\n=== Buscar Producto ===")
    print("1. Buscar por ID")
    print("2. Buscar por Nombre")
    print("3. Buscar por Categoría")

    opcion = input("Seleccione una opción: ")

    conn = obtener_conexion()
    cursor = conn.cursor()

    if opcion == "1":
        id_buscar = input("Ingrese ID: ")
        cursor.execute("SELECT * FROM productos WHERE id = ?", (id_buscar,))

    elif opcion == "2":
        nombre_buscar = input("Ingrese nombre (o parte): ")
        cursor.execute("SELECT * FROM productos WHERE nombre LIKE ?", ('%' + nombre_buscar + '%',))

    elif opcion == "3":
        categoria_buscar = input("Ingrese categoría: ")
        cursor.execute("SELECT * FROM productos WHERE categoria LIKE ?", ('%' + categoria_buscar + '%',))

    else:
        print("Opción inválida.")
        conn.close()
        return

    resultados = cursor.fetchall()
    conn.close()

    if resultados:
        for p in resultados:
            print(f"ID: {p[0]} | Nombre: {p[1]} | Descripción: {p[2]} | Cantidad: {p[3]} | Precio: {p[4]} | Categoría: {p[5]}")
    else:
        print("No se encontraron productos.")


# ----------------------------------------------------------------------
# EDITAR PRODUCTO
# ----------------------------------------------------------------------
def editar_producto():
    """Edita un producto existente por su ID"""
    print("\n=== Editar Producto ===")
    producto_id = input("Ingrese el ID del producto a editar: ")

    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM productos WHERE id = ?", (producto_id,))
    producto = cursor.fetchone()

    if not producto:
        print("Producto no encontrado.")
        conn.close()
        return

    print("Deje en blanco para no modificar el campo.")
    nuevo_nombre = input(f"Nombre ({producto[1]}): ") or producto[1]
    nueva_desc = input(f"Descripción ({producto[2]}): ") or producto[2]
    nueva_cantidad = input(f"Cantidad ({producto[3]}): ")
    nuevo_precio = input(f"Precio ({producto[4]}): ")
    nueva_categoria = input(f"Categoría ({producto[5]}): ") or producto[5]

    nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else producto[3]
    nuevo_precio = float(nuevo_precio) if nuevo_precio else producto[4]

    cursor.execute(
        """
        UPDATE productos
        SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria = ?
        WHERE id = ?
        """,
        (nuevo_nombre, nueva_desc, nueva_cantidad, nuevo_precio, nueva_categoria, producto_id)
    )

    conn.commit()
    conn.close()
    print("Producto actualizado exitosamente.")


# ----------------------------------------------------------------------
# ELIMINAR PRODUCTO
# ----------------------------------------------------------------------
def eliminar_producto():
    """Elimina un producto por ID"""
    print("\n=== Eliminar Producto ===")
    producto_id = input("Ingrese ID del producto: ")

    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM productos WHERE id = ?", (producto_id,))
    conn.commit()
    conn.close()

    print("Producto eliminado (si existía).")


# ----------------------------------------------------------------------
# REPORTE DE BAJO STOCK
# ----------------------------------------------------------------------
def reporte_bajo_stock():
    """Muestra productos con cantidad menor o igual a un límite dado por el usuario."""
    print("\n=== Reporte: Productos con Bajo Stock ===")
    limite = int(input("Mostrar productos con cantidad <= a: "))

    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (limite,))
    productos = cursor.fetchall()

    conn.close()

    if not productos:
        print("No hay productos con bajo stock.")
        return

    print("\nProductos con bajo stock:")
    for p in productos:
        print(f"ID: {p[0]} | Nombre: {p[1]} | Cantidad: {p[3]} | Categoría: {p[5]}")
