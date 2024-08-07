import sqlite3
from datetime import datetime

def conectar():
    return sqlite3.connect('prestamos.db')

def agregar_cliente(nombre, telefono, direccion):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Clientes (n,ombre, telefono, direccion) VALUES (?, ?, ?, ?, ? )",
                   (cliente_id, monto,interes,fecha_inicio,fecha_vencimiento))
    
    conn.commit()
    conn.close()