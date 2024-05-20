import streamlit as st
from database import crear_tabla, agregar_mensaje, mostrar_mensajes, eliminar_mensaje
from PIL import Image

st.set_page_config(page_title="Manu.py", page_icon="🐍", layout="wide")

# Crear la tabla en la base de datos si no existe
crear_tabla()

# Función para mostrar la página de inicio con información personal
def pagina_inicio():

   #introduccion

   with st.container():
      st.header("Este es mi portafolio")
      st.title("Hola mundo, soy Manu.py🐍")
      st.write("""¡Hola! Soy Manuel, un apasionado de la programación con sede en Santa Fe, Argentina. Me encanta trabajar en el backend 
               y he invertido tiempo en aprender diversas tecnologías para ampliar mis habilidades. He realizado cursos en PHP, SQL, Bootstrap y Python, 
               además de dominar los fundamentos de HTML, CSS y JavaScript.
               Mi fascinación por el desarrollo web me llevó a explorar diferentes lenguajes y frameworks. 
               Disfruto especialmente trabajando en el backend, donde puedo construir la lógica que hace que las aplicaciones cobren vida. 
               Estoy constantemente buscando oportunidades para mejorar y expandir mis conocimientos en el campo de la programación.
               """)
      st.write("Aquí mi repositorio de Github")
      st.write("[📂 >] (https://github.com/Manu-py)")
      st.write("##") 
      st.subheader("Sobre mi")
      st.write("En esta sección, me gustaría compartir un poco más sobre mí y mi trayectoria en la programación.")
      
   #sobre mi 

   with st.container():
      st.write("---")
      st.write("##")
      img_colum, text_colum = st.columns((1,2))
      with img_colum:
         image = Image.open("img/estudios.png")
         st.image(image, use_column_width=True)
      with text_colum:
         st.write ( '''

         **Experiencia Educativa**
         
         ***- Estudios:***
         Actualmente soy estudiante de programación y desarrollo web. He completado cursos en Python, así como en los fundamentos de HTML, CSS y JavaScript.
         '''
         )   
         
      with st.container():
         st.write("---")
         text_colum, img_colum = st.columns((2,1))
      with text_colum:
         st.write ( '''
         **Intereses y Habilidades**
         
         ***- Backend Development:*** Mi principal área de interés es el desarrollo backend, especialmente con Python.
         
         
         ***- Automatización:*** Disfruto automatizando procesos para hacerlos más eficientes y efectivos.
         
         ***- Desarrollo de Aplicaciones:*** Me gusta desarrollar aplicaciones funcionales y útiles utilizando Python y sus diferentes frameworks.'''
         )   
      with img_colum:
         image = Image.open("img/skil.png")
         st.image(image, use_column_width=True)

      with st.container():
         st.write("---")
      
         img_colum, text_colum = st.columns((1,2))
      with img_colum:
         image = Image.open("img/proyectos.png")
         st.image(image, use_column_width=True)
      
      with text_colum:
         st.write( '''
         **Proyectos Destacados**
         
         Aquí están algunos de los proyectos en los que he trabajado:
         
         ***- Generador de Imágenes con IA (Python):***
         
         Desarrollé un generador de imágenes utilizando Inteligencia Artificial (IA) y Python. Esta herramienta utiliza algoritmos de generación de imágenes para crear contenido visual de manera automatizada.
         
         ***- App de Facturación Personalizada (Python/Flask):***
         
         Desarrollé una aplicación web de facturación personalizada utilizando Python y Flask. Esta aplicación permite a los usuarios gestionar sus facturas de manera eficiente, adaptándose a sus necesidades específicas.
         
         ***- Automatización de Emails (Python):***
         
         Implementé un sistema de automatización de emails utilizando Python. Esta herramienta automatiza el envío de correos electrónicos, lo que ahorra tiempo y reduce errores en comunicaciones repetitivas.
         
         ***- Páginas Web Interactivas con Streamlit (Python):***
         
         Desarrollé páginas web interactivas utilizando Streamlit, una biblioteca de Python para la creación de aplicaciones web. Estas páginas web presentan información de manera atractiva y funcional.
         
         ***- IA Chatbot (Python):***
         
         Creé un chatbot utilizando Inteligencia Artificial (IA) y Python. Este chatbot es capaz de mantener conversaciones con usuarios y responder a sus preguntas de manera inteligente.
         '''
         )

   # contacto
   with st.container():
      st.write("---")
      st.write("##")
      st.subheader("Contacto")
      st.write("Para cualquier duda o consulta, puedes contactarme a través de los siguientes medios:")
      st.write("[💻 >] (https://github.com/)")
      st.write("[📂 >] (https://linkedin.com/in/)")
      st.write("O puedes completar el formulario seleccionando la opción aquí a la izquierda y será respondido a la brevedad")
      st.write("[↖↖↖↖]")

# Función para mostrar el formulario de contacto
def pagina_formulario():
   st.title("Formulario de Contacto")  # Título de la página

    # Formulario de contacto
   with st.form(key='formulario_contacto'):
      nombre = st.text_input("Nombre")  # Campo de entrada para el nombre
      email = st.text_input("Correo electrónico")  # Campo de entrada para el correo electrónico
      mensaje = st.text_area("Mensaje")  # Campo de entrada para el mensaje
      enviar = st.form_submit_button("Enviar")  # Botón de envío

        # Cuando el usuario envía el formulario
      if enviar:
            agregar_mensaje(nombre, email, mensaje)  # Guardar el mensaje en la base de datos
            st.success("¡Mensaje enviado con éxito!")  # Mostrar mensaje de éxito

# Función para mostrar la página de login del administrador
def pagina_admin_login():
    st.title("Iniciar sesión como administrador")  # Título de la página

    # Formulario de login
    username = st.text_input("Nombre de usuario")  # Campo de entrada para el nombre de usuario
    password = st.text_input("Contraseña", type="password")  # Campo de entrada para la contraseña
    if st.button("Iniciar sesión"):  # Botón de inicio de sesión
        if username == "admin" and password == "admin":
            st.session_state['admin_logged_in'] = True  # Guardar estado de sesión como administrador
            st.experimental_rerun()  # Recargar la página para reflejar el cambio de estado
        else:
            st.error("Credenciales incorrectas")  # Mostrar mensaje de error si las credenciales son incorrectas

# Función para mostrar los mensajes recibidos y permitir su eliminación
def mostrar_mensajes_admin():
    st.title("Mensajes Recibidos")  # Título de la página

    # Obtener y mostrar todos los mensajes de la base de datos
    mensajes = mostrar_mensajes()
    for mensaje in mensajes:
        st.write(f"ID: {mensaje[0]}")
        st.write(f"Nombre: {mensaje[1]}")
        st.write(f"Correo electrónico: {mensaje[2]}")
        st.write(f"Mensaje: {mensaje[3]}")
        
        # Botón para eliminar cada mensaje
        if st.button(f"Eliminar mensaje {mensaje[0]}", key=f"eliminar_{mensaje[0]}"):
            eliminar_mensaje(mensaje[0])  # Eliminar el mensaje de la base de datos
            st.success("¡Mensaje eliminado con éxito!")  # Mostrar mensaje de éxito
            st.experimental_rerun()  # Recargar la página para actualizar la lista de mensajes

# Lógica principal para controlar la navegación entre las páginas
def main():
    if 'admin_logged_in' not in st.session_state:
        st.session_state['admin_logged_in'] = False

    st.sidebar.title("Navegación")
    seleccion = st.sidebar.radio("Ir a", ["Inicio", "Formulario de Contacto", "Admin Login", "Administrar Mensajes"])

    if seleccion == "Inicio":
        pagina_inicio()
    elif seleccion == "Formulario de Contacto":
        pagina_formulario()
    elif seleccion == "Admin Login":
        pagina_admin_login()
    elif seleccion == "Administrar Mensajes":
        if st.session_state['admin_logged_in']:
            mostrar_mensajes_admin()
        else:
            st.error("Por favor, inicie sesión como administrador primero.")
            pagina_admin_login()

if __name__ == "__main__":
    main()     