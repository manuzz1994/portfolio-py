import streamlit as st
from database import insertar_mensaje, mostrar_mensajes, crear_tabla
from PIL import Image

st.set_page_config(page_title="Manu.py", page_icon="🐍", layout="wide")

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
    st.write("O puedes completar el formulario y será respondido a la brevedad")
    
def mostrar_form():
      # creando formulario.
      with st.form(key='formulario_contacto'):
         # Campo de entrada para el nombre
         nombre = st.text_input("Nombre")

         # Campo de entrada para el correo electrónico
         email = st.text_input("Correo electrónico")

         # Campo de entrada para el mensaje
         mensaje = st.text_area("Mensaje")

         # Botón de enviar dentro del formulario
         enviar = st.form_submit_button("Enviar")
   # Cuando se hace clic en el botón de enviar
         if enviar:
               if nombre.strip() == "" or email.strip() == "" or mensaje.strip() == "": #validar campos
                  st.error("Por favor, completa todos los campos.")
               else:
                  #Se agrega mensaje en BD
                  insertar_mensaje(nombre, email, mensaje)
                  st.success("¡Mensaje enviado con éxito!")
def main():
   #llamar funcion para mostrar el formulario
   mostrar_form()
   
if __name__ == "__main__":
   main()                  