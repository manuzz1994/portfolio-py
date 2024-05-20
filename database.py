import sqlite3

# Función para conectar a la base de datos
def conectar_bd():
    return sqlite3.connect('mensajes.db')

# Función para crear la tabla de mensajes si no existe
def crear_tabla():
    conexion = conectar_bd()
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS mensajes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            email TEXT NOT NULL,
            mensaje TEXT NOT NULL
        )
    ''')
    conexion.commit()
    conexion.close()

# Función para agregar un mensaje a la base de datos
def agregar_mensaje(nombre, email, mensaje):
    conexion = conectar_bd()
    cursor = conexion.cursor()
    cursor.execute('INSERT INTO mensajes (nombre, email, mensaje) VALUES (?, ?, ?)', (nombre, email, mensaje))
    conexion.commit()
    conexion.close()

# Función para obtener todos los mensajes de la base de datos
def mostrar_mensajes():
    conexion = conectar_bd()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM mensajes')
    mensajes = cursor.fetchall()
    conexion.close()
    return mensajes

# Función para eliminar un mensaje de la base de datos
def eliminar_mensaje(id_mensaje):
    conexion = conectar_bd()
    cursor = conexion.cursor()
    cursor.execute('DELETE FROM mensajes WHERE id = ?', (id_mensaje,))
    conexion.commit()
    conexion.close()
