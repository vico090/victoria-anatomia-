"""
Aplicación simplificada para depurar problemas con pestañas y contenido mínimo.
"""
import streamlit as st
import quiz
from respiratory_system_data import QUIZ_QUESTIONS

# Configuración de la página
st.set_page_config(
    page_title="Debug App - Sistema Respiratorio",
    page_icon="🫁",
    layout="wide"
)

# Título y descripción
st.title("Depuración: Sistema Respiratorio")
st.markdown("Esta es una versión simplificada para depurar problemas")

# Mostrar dos botones simples
btn1 = st.button("Botón de prueba 1")
btn2 = st.button("Botón de prueba 2")

if btn1:
    st.write("Botón 1 presionado")
if btn2:
    st.write("Botón 2 presionado")

# Crear pestañas de forma sencilla
try:
    st.write("Creando pestañas...")
    tab1, tab2, tab3 = st.tabs(["Pestaña 1", "Pestaña 2", "Pestaña 3"])
    
    with tab1:
        st.header("Pestaña 1 - Anatomía Básica")
        st.write("Esta es la primera pestaña funcionando correctamente")
        # En lugar de una imagen externa, usamos un texto descriptivo
        st.info("Aquí se mostraría una imagen del sistema respiratorio si estuviera disponible")
    
    with tab2:
        st.header("Pestaña 2 - Información General")
        st.write("Esta es la segunda pestaña funcionando correctamente")
        
        # Un expander simple para probar
        with st.expander("Información sobre el sistema respiratorio"):
            st.write("El sistema respiratorio está formado por las estructuras que realizan el intercambio de gases entre la atmósfera y la sangre.")
    
    with tab3:
        st.header("Pestaña 3 - Quiz Básico")
        st.write("Esta es la tercera pestaña funcionando correctamente")
        
        # Intentar mostrar el quiz de forma simplificada
        if st.button("Cargar Quiz Simple"):
            st.write("Preguntas disponibles:")
            for i, q in enumerate(QUIZ_QUESTIONS[:3]):
                st.write(f"{i+1}. {q['question']}")
except Exception as e:
    st.error(f"Error al crear las pestañas: {e}")
    # Mostrar información detallada del error para depuración
    import traceback
    st.code(traceback.format_exc())

# Barra lateral con opciones
st.sidebar.title("Barra lateral")
st.sidebar.write("Contenido de prueba para la barra lateral")

# Información sobre el estado de la aplicación
st.sidebar.markdown("---")
st.sidebar.subheader("Información de depuración")
st.sidebar.write("Versión: Debug 1.0")
st.sidebar.write(f"Variables de sesión: {list(st.session_state.keys())}")