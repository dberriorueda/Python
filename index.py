import sqlite3
from datetime import datetime

def conectar():
    return sqlite3.connect('prestamos.db')

def agregar_cliente(nombre, telefono, direccion):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Clientes (nombre, telefono, direccion) VALUES (?, ?, ? )",
                   (nombre, telefono, direccion))
    
    conn.commit()
    conn.close()
    
def agregar_prestamo(cliente_id, monto, interes, fecha_inicio, fecha_vencimiento):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO prestamos (cliente_id, monto, interes, fecha_inicio, fecha_vencimiento) Values (?, ?, ?, ?, ?)",
                    (cliente_id, monto, interes, fecha_inicio, fecha_vencimiento))   
    
    conn.commit()
    conn.close()

    #Ejemplo de agregar  un cliente
    agregar_cliente("Carlos Granados", "3235098018", "Calle medellin")
    agregar_prestamo(1, 1000000, 10, "2024-08-10", "2025-08-10")