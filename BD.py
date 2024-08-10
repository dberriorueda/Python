import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('prestamos.db')
cursor = conn.cursor()

# Crear tabla clientes
cursor.execute('''
CREATE TABLE IF NOT EXISTS Clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    telefono TEXT,
    direccion TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS prestamos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER NOT null,
    monto REAL NOT NULL,
    interes REAL NOT NULL,
    fecha_inicio text NOT null,
    fecha_vencimiento TEXT NOT NULL,
    estado TEXT NOT NULL DEFAULT 'pendiente',
    FOREIGN KEY (cliente_id) REFERENCES Clientes(id)
)
''')

#Crear indice en cliente_id para mejorar el rendimiento

cursor.execute('CREATE INDEX IF NOT EXISTS idx_cliente_id ON prestamos(cliente_id)')

conn.commit()
conn.close()
