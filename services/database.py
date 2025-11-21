import sqlite3
from pathlib import Path


DB_PATH = Path(__file__).resolve().parents[1] / "inventario.db"


def obtener_conexion():
    """Devuelve una conexión a la base de datos SQLite."""
    # Usamos detect_types=0 por compatibilidad simple
    return sqlite3.connect(str(DB_PATH))


def inicializar_db():
    """Crea la tabla productos si no existe."""
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
