import sqlite3

# Función para conectar a la base de datos SQLite
def conectar_bd():
    conexion = sqlite3.connect('mensajes.db')
    return conexion

# Función para crear
def crear_tabla():
    conexion = conectar_bd()
    cursor = conexion.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS mensajes
                      (id INTEGER PRIMARY KEY, nombre TEXT, email TEXT, mensaje TEXT)''')
    conexion.commit()
    conexion.close()

# Función para insertar un mensaje en la base de datos
def insertar_mensaje(nombre, email, mensaje):
    conexion = conectar_bd()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO mensajes (nombre, email, mensaje) VALUES (?, ?, ?)", (nombre, email, mensaje))
    conexion.commit()
    conexion.close()

# Función para mostrar los mensajes almacenados en la base de datos
def mostrar_mensajes():
    conexion = conectar_bd()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM mensajes")
    mensajes = cursor.fetchall()
    conexion.close()
    return mensajes

def eliminar_mensaje(id_mensaje):
    # Función para eliminar un mensaje de la base de datos
    conexion = conectar_bd()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM mensajes WHERE id=?", (id_mensaje,))
    conexion.commit()
    conexion.close()
