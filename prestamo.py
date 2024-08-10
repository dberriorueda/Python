import sqlite3
import sys

def conectar():
    return sqlite3.connect('prestamos.db')

def crear_tablas():
    conn = conectar()
    cursor = conn.cursor()


    cursor.execute('''
CREATE TABLE IF NOT EXISTS clientes (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nombre TEXT NOT NULL,
                   telefono TEXT,
                   direccion TEXT
)
''')

    cursor.execute('''
CREATE TABLE IF NOT EXISTS prestamos (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   cliente_id INTEGER NOT NULL,
                   monto REAL NOT NULL,
                   interes REAL NOT NULL,
                   fecha_inicio TEXT NOT NULL,
                   fecha_vencimiento TEXT NOT NULL,
                   estado TEXT NOT NULL DEFAULT 'pendiente',
                   FOREIGN KEY (cliente_id) REFERENCES cliente(id)
                   )
                   ''')
    
    cursor.execute('CREATE INDEX IF NOT EXISTS isx_cliente_id ON prestamos(cliente_id)')

    conn.commit()
    conn.close()

    def agregar_cliente(nombre, telefono, direccion):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Clientes (nombre, telefono, direccion) VALUES (?, ?, ? )",
                   (nombre, telefono, direccion))
        
        conn.commit()
        conn.close()

    def agregar_prestamo(cliente_id, monto, interes, fecha_inicio, fecha_vencimiento):
        conn.conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO prestamos (cliente_id, monto, interes, fecha_inicio, fecha_vencimiento) Values (?, ?, ?, ?, ?)",
                    (cliente_id, monto, interes, fecha_inicio, fecha_vencimiento))
        
        conn.commit()
        conn.close()


    def ver_cliente():
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clientes")
        clientes = cursor.fetchall()
        conn.close()
        return clientes
    
    def ver_prestamo():
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM prestamos")
        prestamos = cursor.fetchall()
        conn.close()
        return prestamos
    
    def actuallizar_prestamo(id_prestamo, monto, interes, estado):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('''
        UPDATE prestamos
        SET monto = ?, interes = ?, estado = ? WHERE id = ?''', (monto, interes, estado, id_prestamo))

        conn.commit()
        conn.close()
        
