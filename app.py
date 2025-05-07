"""
Aplicación educativa interactiva para identificar y aprender sobre la anatomía del sistema respiratorio.
"""
import streamlit as st
import streamlit.components.v1 as components
from respiratory_system_data import RESPIRATORY_SYSTEM_DATA, QUIZ_QUESTIONS
from utils import create_anatomy_map, find_structure_by_id, display_structure_info, get_all_structures
from quiz import display_quiz, initialize_quiz_state

# Configuración de la página
st.set_page_config(
    page_title="Sistema Respiratorio - Anatomía Interactiva",
    page_icon="🫁",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Título y descripción
st.title("Sistema Respiratorio: Anatomía Interactiva")
st.markdown("""
Esta aplicación te permite explorar la anatomía del sistema respiratorio de forma interactiva. 
Puedes seleccionar diferentes estructuras para aprender más sobre ellas y poner a prueba tus conocimientos con un quiz.
""")

# Inicializar el estado de la sesión si no existe
if 'selected_structure_id' not in st.session_state:
    st.session_state.selected_structure_id = None

# Inicializar el estado del quiz
initialize_quiz_state()

# Envolvemos cada sección en un bloque try-except para manejar posibles errores
try:
    # Pestañas para navegación
    tab1, tab2, tab3 = st.tabs(["Explorar Anatomía", "Estructuras del Sistema Respiratorio", "Quiz"])

    # Pestaña 1: Explorador Anatómico
    try:
        with tab1:
            st.header("Explorador Anatómico Interactivo")
            st.markdown("""
            Selecciona cualquier parte del sistema respiratorio en la imagen para obtener información detallada.
            Puedes hacer clic en las diferentes estructuras para aprender más sobre ellas.
            """)
            
            # Dividir la pantalla en dos columnas
            col1, col2 = st.columns([3, 2])
            
            with col1:
                try:
                    # Mostrar el mapa anatómico interactivo
                    svg_html = create_anatomy_map()
                    selected_part = components.html(svg_html, height=600, scrolling=False)
                    
                    # Actualizar la estructura seleccionada si se ha hecho clic en el SVG
                    if selected_part and selected_part != st.session_state.selected_structure_id:
                        st.session_state.selected_structure_id = selected_part
                        st.rerun()
                except Exception as e:
                    st.error(f"Error al cargar el mapa anatómico: {e}")
                    st.info("No se pudo cargar el mapa interactivo. Por favor, intenta recargar la página.")
            
            with col2:
                # Mostrar información de la estructura seleccionada
                st.subheader("Información")
                
                if st.session_state.selected_structure_id:
                    try:
                        selected_structure = find_structure_by_id(st.session_state.selected_structure_id, RESPIRATORY_SYSTEM_DATA)
                        display_structure_info(selected_structure)
                    except Exception as e:
                        st.error(f"Error al mostrar información de la estructura: {e}")
                else:
                    st.info("Selecciona una parte del sistema respiratorio en la imagen para ver información detallada.")
    except Exception as e:
        st.error(f"Error en la pestaña Explorador Anatómico: {e}")

    # Pestaña 2: Estructuras del Sistema Respiratorio
    try:
        with tab2:
            st.header("Estructuras del Sistema Respiratorio")
            
            # Mostrar información general del sistema respiratorio
            st.subheader(RESPIRATORY_SYSTEM_DATA["system"]["name"])
            st.write(RESPIRATORY_SYSTEM_DATA["system"]["description"])
            
            # Dividir en secciones principales
            st.markdown("## Tracto Respiratorio Superior")
            st.write(RESPIRATORY_SYSTEM_DATA["upper_tract"]["description"])
            
            # Mostrar estructuras del tracto respiratorio superior con expanders
            for structure in RESPIRATORY_SYSTEM_DATA["upper_tract"]["structures"]:
                with st.expander(structure["name"]):
                    st.write(structure["description"])
                    if "function" in structure:
                        st.markdown("**Función:**")
                        st.write(structure["function"])
            
            st.markdown("## Tracto Respiratorio Inferior")
            st.write(RESPIRATORY_SYSTEM_DATA["lower_tract"]["description"])
            
            # Mostrar estructuras del tracto respiratorio inferior con expanders
            for structure in RESPIRATORY_SYSTEM_DATA["lower_tract"]["structures"]:
                with st.expander(structure["name"]):
                    st.write(structure["description"])
                    if "function" in structure:
                        st.markdown("**Función:**")
                        st.write(structure["function"])
            
            st.markdown("## Estructuras Accesorias")
            st.write(RESPIRATORY_SYSTEM_DATA["accessory_structures"]["description"])
            
            # Mostrar estructuras accesorias con expanders
            for structure in RESPIRATORY_SYSTEM_DATA["accessory_structures"]["structures"]:
                with st.expander(structure["name"]):
                    st.write(structure["description"])
                    if "function" in structure:
                        st.markdown("**Función:**")
                        st.write(structure["function"])
            
            st.markdown("## Mediastino")
            with st.expander(RESPIRATORY_SYSTEM_DATA["mediastinum"]["name"]):
                st.write(RESPIRATORY_SYSTEM_DATA["mediastinum"]["description"])
                if "function" in RESPIRATORY_SYSTEM_DATA["mediastinum"]:
                    st.markdown("**Función:**")
                    st.write(RESPIRATORY_SYSTEM_DATA["mediastinum"]["function"])
    except Exception as e:
        st.error(f"Error en la pestaña Estructuras del Sistema Respiratorio: {e}")

    # Pestaña 3: Quiz
    try:
        with tab3:
            st.header("Quiz: Pon a prueba tus conocimientos")
            st.markdown("""
            Este quiz te permitirá evaluar tu conocimiento sobre la anatomía del sistema respiratorio.
            Selecciona la respuesta correcta para cada pregunta.
            """)
            
            # Mostrar el quiz
            display_quiz(QUIZ_QUESTIONS)
    except Exception as e:
        st.error(f"Error en la pestaña Quiz: {e}")

    # Barra lateral con opciones
    try:
        st.sidebar.title("Navegación")
        st.sidebar.markdown("## Opciones")

        # Selector de estructuras en la barra lateral
        all_structures = get_all_structures(RESPIRATORY_SYSTEM_DATA)
        structure_names = [structure["name"] for structure in all_structures]
        selected_name = st.sidebar.selectbox("Seleccionar estructura:", structure_names)

        # Encontrar la estructura seleccionada y mostrarla
        for structure in all_structures:
            if structure["name"] == selected_name:
                # Actualizar el estado de la sesión
                st.session_state.selected_structure = structure
                
                # Mostrar información en la barra lateral
                st.sidebar.markdown("### " + structure["name"])
                st.sidebar.write(structure["description"])
                if "function" in structure:
                    st.sidebar.markdown("**Función:**")
                    st.sidebar.write(structure["function"])
                break

        # Información de la aplicación
        st.sidebar.markdown("---")
        st.sidebar.markdown("""
        ### Acerca de esta aplicación

        Esta aplicación educativa interactiva permite explorar la anatomía del sistema respiratorio 
        de manera visual e intuitiva.

        Desarrollada con fines educativos para el estudio de la anatomía humana.
        """)
    except Exception as e:
        st.sidebar.error(f"Error en la barra lateral: {e}")

except Exception as e:
    st.error(f"Error general en la aplicación: {e}")
    st.write("Por favor, recarga la página para intentar de nuevo.")
    import traceback
    st.code(traceback.format_exc())

# Pie de página
st.markdown("---")
st.markdown("Desarrollado con ❤️ para educación médica")
