# Manual de Operación
## Sistema de Gestión Básica de Productos

**Autor:** Gustavo  
**Descripción:** Prototipo para agregar, mostrar, buscar y eliminar productos.

---

## Objetivo
Permitir la gestión básica de productos: agregar, mostrar, buscar y eliminar productos en una lista.

---

## Requisitos
- Python 3 instalado
- Ejecutar el archivo `.py` en consola o terminal

---

## Instrucciones de Uso

### Ejecutar el programa
```bash
python3 nombre_del_archivo.py
```

### Menú principal
```
===== MENÚ PRINCIPAL =====
1. Agregar producto
2. Mostrar productos
3. Buscar producto
4. Eliminar producto
5. Salir
```

### Opciones disponibles

#### 1. Agregar producto
- Solicita ingresar:
    - Nombre (no vacío)
    - Categoría (no vacío)
    - Precio (entero positivo)
- Muestra confirmación del producto agregado.

#### 2. Mostrar productos
- Lista todos los productos registrados con su nombre, categoría y precio.
- Si no hay productos, muestra un mensaje informativo.

#### 3. Buscar producto
- Solicita ingresar el **nombre o parte del nombre** del producto.
- Muestra todos los productos que coincidan (no sensible a mayúsculas).
- Si no encuentra coincidencias, informa al usuario.

#### 4. Eliminar producto
- Muestra la lista numerada de productos.
- Solicita ingresar el número del producto que se desea eliminar.
- Confirma la eliminación del producto seleccionado.
- Si la lista está vacía, informa que no hay productos para eliminar.

#### 5. Salir
- Finaliza el programa.

---

## Notas importantes
- Todos los campos son **requeridos**; no se permiten valores vacíos en nombre o categoría.
- El precio debe ser un **número entero mayor o igual a cero**.
- La búsqueda de productos permite coincidencias parciales y no distingue mayúsculas de minúsculas.

---

## Demo de flujo de ejecución
```
1. Agregar producto: "Coca Cola", categoría "Bebidas", precio 1500
2. Agregar producto: "Pepsi", categoría "Bebidas", precio 1400
3. Mostrar productos → lista con Coca Cola y Pepsi
4. Buscar producto: "coca" → encuentra Coca Cola
5. Eliminar producto: selecciona Coca Cola → eliminado
6. Mostrar productos → lista con Pepsi
7. Salir
```