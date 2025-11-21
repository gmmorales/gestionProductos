"""
Autor: Gustavo
Descripción: Sistema de gestión básica de productos con SQLite
"""
from utils.menu import mostrar_menu
from services.productos_service import (
    agregar_producto,
    mostrar_productos,
    buscar_producto,
    editar_producto,
    eliminar_producto,
    reporte_bajo_stock,
)
from services.database import inicializar_db


def main():
    inicializar_db()  # Crea la DB y tabla si no existen

    while True:
        opcion = mostrar_menu()

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
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()
