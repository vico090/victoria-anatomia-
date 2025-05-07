"""
Aplicación de prueba básica para verificar si Streamlit funciona correctamente.
"""
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Aplicación de Prueba",
    page_icon="🧪",
    layout="wide"
)

# Título y descripción
st.title("Aplicación de Prueba")
st.markdown("""
Esta es una aplicación de prueba simple para verificar si Streamlit está funcionando correctamente.
""")

# Contenido básico
st.header("Componentes Básicos")

# Un texto
st.write("Esto es un texto simple")

# Un botón
if st.button("Haz clic aquí"):
    st.write("¡Botón presionado!")

# Un selectbox
option = st.selectbox(
    'Selecciona una opción:',
    ['Opción 1', 'Opción 2', 'Opción 3']
)
st.write('Seleccionaste:', option)

# Mostrar un mensaje de estado
st.success("¡La aplicación está funcionando correctamente!")