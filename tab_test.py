"""
Prueba simple de pestañas en Streamlit
"""
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Prueba de pestañas",
    page_icon="🧪",
    layout="wide"
)

# Título y descripción
st.title("Prueba simple de pestañas")
st.markdown("Esta aplicación prueba la funcionalidad básica de pestañas en Streamlit.")

# Crear pestañas simples
try:
    # Crear pestañas con nombres descriptivos
    tab1, tab2, tab3 = st.tabs(["Primera Pestaña", "Segunda Pestaña", "Tercera Pestaña"])
    
    # Contenido de la primera pestaña
    with tab1:
        st.header("Contenido de la primera pestaña")
        st.write("Esta es la primera pestaña.")
        st.button("Botón en pestaña 1")
    
    # Contenido de la segunda pestaña
    with tab2:
        st.header("Contenido de la segunda pestaña")
        st.write("Esta es la segunda pestaña.")
        st.slider("Slider en pestaña 2", 0, 100, 50)
    
    # Contenido de la tercera pestaña
    with tab3:
        st.header("Contenido de la tercera pestaña")
        st.write("Esta es la tercera pestaña.")
        options = ["Opción 1", "Opción 2", "Opción 3"]
        st.selectbox("Selector en pestaña 3", options)
    
except Exception as e:
    st.error(f"Error al crear las pestañas: {e}")
    import traceback
    st.code(traceback.format_exc())

# Pie de página
st.markdown("---")
st.write("Prueba de pestañas en Streamlit")