import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('prestamos.db')
cursor = conn.cursor()

# Crear tabla clientes
cursor.execute('''
CREATE TABLE IF NOT EXISTS Clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    telefono TEXT.
    direccion TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS prestamos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER NOT null,
    monto REAL NOT NULL,
    interes REAL NOT NULL,
    fecha_inicio text not null,
    fecha_vencimiento TEXT NOT NULL,
    estado TEXT NOT NULL DEFAULT 'pendiente',
    FOREING KEY (cliente_id) REFERENCES Clientes(id)
)
''')

conn.commit()
conn.close()
