import streamlit as st

st.title("Aplicación simple de prueba")

st.write("Esta es una aplicación muy básica para probar Streamlit")

# Crear un botón
if st.button("Haz clic aquí"):
    st.write("¡Has hecho clic en el botón!")

# Crear un slider
valor = st.slider("Selecciona un valor", 0, 100, 50)
st.write(f"Has seleccionado: {valor}")