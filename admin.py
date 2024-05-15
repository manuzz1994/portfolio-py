import streamlit as st
from database import mostrar_mensajes, crear_tabla, eliminar_mensaje

def login_admin():
    # Función para iniciar sesión como administrador
    st.title("Iniciar sesión como administrador")

    username = st.text_input("Nombre de usuario")
    password = st.text_input("Contraseña", type="password")
    enviar = st.button("Iniciar sesión")  # botón para enviar las credenciales
    if enviar: # Solo verificamos las credenciales si se presiona el botón 
        if username == "admin" and password == "admin":
            return True
        else:
            st.error("Credenciales incorrectas")
            return False

def mostrar_mensajes_admin():
    # Función para mostrar los mensajes recibidos por los usuarios
    st.title("Mensajes Recibidos")
    mensajes = mostrar_mensajes()
    for mensaje in mensajes:
        st.write(f"Nombre: {mensaje[1]}")
        st.write(f"Correo electrónico: {mensaje[2]}")
        st.write(f"Mensaje: {mensaje[3]}")
       
        # Botón para eliminar el mensaje
        if st.button(f"Eliminar mensaje {mensaje[0]}"):  # Utilizamos el ID del mensaje en el texto del botón
            eliminar_mensaje(mensaje[0])  # Pasar el ID del mensaje a la función eliminar_mensaje()
            st.success("¡Mensaje eliminado con éxito!")
    # Refrescar la app después de eliminar el mensaje
            st.experimental_rerun()
        st.write("------")
def main():
    crear_tabla()
    # Verificar si el usuario es un administrador
    if login_admin():
        # Mostrar los mensajes almacenados
        mostrar_mensajes_admin()

if __name__ == "__main__":
    main()
