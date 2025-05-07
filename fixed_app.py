"""
Aplicación educativa interactiva para identificar y aprender sobre la anatomía del sistema respiratorio,
versión simplificada y optimizada.
"""
import streamlit as st
from respiratory_system_data import RESPIRATORY_SYSTEM_DATA, QUIZ_QUESTIONS

# Configuración de la página
st.set_page_config(
    page_title="Sistema Respiratorio - Anatomía",
    page_icon="🫁",
    layout="wide"
)

# Título y descripción
st.title("Sistema Respiratorio: Anatomía Interactiva")
st.markdown("""
Esta aplicación te permite explorar en detalle la anatomía del sistema respiratorio. 
Conoce la estructura y función de cada componente para comprender mejor este sistema vital.
""")

# Inicializar estados de la sesión
if 'quiz_questions' not in st.session_state:
    st.session_state.quiz_questions = QUIZ_QUESTIONS.copy()
if 'current_question_index' not in st.session_state:
    st.session_state.current_question_index = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'quiz_finished' not in st.session_state:
    st.session_state.quiz_finished = False
if 'answered_current' not in st.session_state:
    st.session_state.answered_current = False
if 'selected_structure' not in st.session_state:
    st.session_state.selected_structure = None

# Crear pestañas
tab1, tab2, tab3 = st.tabs(["Atlas Anatómico", "Detalles Estructurales", "Quiz de Anatomía"])

# Pestaña 1: Atlas Anatómico
with tab1:
    st.header("Atlas Anatómico del Sistema Respiratorio")
    
    # Introducción breve
    st.markdown("""
    El sistema respiratorio es fundamental para el intercambio de gases entre el organismo y el ambiente.
    Está dividido en tracto respiratorio superior e inferior, cada uno con estructuras especializadas.
    """)
    
    # Columnas para mejor organización
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Tracto superior - detalles visuales
        st.markdown("## Tracto Respiratorio Superior")
        
        # Lista de estructuras con descripciones breves
        for structure in RESPIRATORY_SYSTEM_DATA["upper_tract"]["structures"]:
            with st.expander(f"🔍 {structure['name']}"):
                st.markdown(f"**Descripción:** {structure['description']}")
                if "function" in structure:
                    st.markdown(f"**Función:** {structure['function']}")
        
        # Tracto inferior - detalles visuales
        st.markdown("## Tracto Respiratorio Inferior")
        
        # Lista de estructuras con descripciones breves
        for structure in RESPIRATORY_SYSTEM_DATA["lower_tract"]["structures"]:
            with st.expander(f"🔍 {structure['name']}"):
                st.markdown(f"**Descripción:** {structure['description']}")
                if "function" in structure:
                    st.markdown(f"**Función:** {structure['function']}")
    
    with col2:
        # Panel informativo para destacar datos anatómicos clave
        st.markdown("### Datos Anatómicos Clave")
        st.info("""
        **Tráquea:** Tubo de 10-12 cm de longitud que conecta la laringe con los bronquios
        
        **Pulmones:** El derecho tiene 3 lóbulos, el izquierdo tiene 2 lóbulos
        
        **Intercambio Gaseoso:** Ocurre en los alvéolos pulmonares
        """)
        
        # Añadir selector de estructuras para exploración
        st.markdown("### Explorar Estructura")
        all_structures = []
        for section in ["upper_tract", "lower_tract", "accessory_structures"]:
            if section in RESPIRATORY_SYSTEM_DATA:
                all_structures.extend(RESPIRATORY_SYSTEM_DATA[section]["structures"])
        
        structure_names = [s["name"] for s in all_structures]
        selected_name = st.selectbox("Selecciona una estructura:", structure_names)
        
        # Mostrar detalles de la estructura seleccionada
        for structure in all_structures:
            if structure["name"] == selected_name:
                st.markdown(f"#### {structure['name']}")
                st.markdown(structure["description"])
                if "function" in structure:
                    st.markdown("**Función Anatómica:**")
                    st.markdown(structure["function"])
                break

# Pestaña 2: Detalles Estructurales
with tab2:
    st.header("Detalles Estructurales")
    
    # Información general
    st.subheader("Anatomía General")
    st.write(RESPIRATORY_SYSTEM_DATA["system"]["description"])
    
    # Organización por secciones principales
    st.markdown("## 1. Tracto Respiratorio Superior")
    st.write(RESPIRATORY_SYSTEM_DATA["upper_tract"]["description"])
    
    # Tabla de estructuras anatómicas
    upper_data = []
    for structure in RESPIRATORY_SYSTEM_DATA["upper_tract"]["structures"]:
        upper_data.append([structure["name"], structure.get("function", "No especificada")])
    
    st.table({"Estructura": [row[0] for row in upper_data], 
             "Función": [row[1] for row in upper_data]})
    
    # Sección para el tracto inferior
    st.markdown("## 2. Tracto Respiratorio Inferior")
    st.write(RESPIRATORY_SYSTEM_DATA["lower_tract"]["description"])
    
    lower_data = []
    for structure in RESPIRATORY_SYSTEM_DATA["lower_tract"]["structures"]:
        lower_data.append([structure["name"], structure.get("function", "No especificada")])
    
    st.table({"Estructura": [row[0] for row in lower_data],
             "Función": [row[1] for row in lower_data]})

# Pestaña 3: Quiz de Anatomía
with tab3:
    st.header("Quiz de Anatomía")
    st.markdown("""
    Pon a prueba tus conocimientos sobre la anatomía del sistema respiratorio.
    """)
    
    # Mostrar el quiz
    current_q = st.session_state.current_question_index
    
    # Si el quiz no ha terminado
    if not st.session_state.quiz_finished and current_q < len(st.session_state.quiz_questions):
        # Obtener la pregunta actual
        question = st.session_state.quiz_questions[current_q]
        
        # Mostrar la pregunta
        st.subheader(f"Pregunta {current_q + 1}/{len(st.session_state.quiz_questions)}")
        st.info(question["question"])
        
        # Mostrar opciones
        st.markdown("**Selecciona la respuesta correcta:**")
        
        # Mostrar las opciones
        for i, option in enumerate(question["options"]):
            if st.button(option, key=f"option_{i}"):
                if option == question["answer"]:
                    st.success("¡Correcto!")
                    st.session_state.score += 1
                else:
                    st.error(f"Incorrecto. La respuesta correcta es: {question['answer']}")
                st.session_state.answered_current = True
        
        # Botón para siguiente pregunta
        if st.session_state.answered_current:
            if st.button("Siguiente pregunta"):
                st.session_state.current_question_index += 1
                st.session_state.answered_current = False
                if st.session_state.current_question_index >= len(st.session_state.quiz_questions):
                    st.session_state.quiz_finished = True
                st.rerun()
    else:
        # Quiz terminado - mostrar resultados
        st.success(f"Quiz completado. Tu puntuación: {st.session_state.score}/{len(st.session_state.quiz_questions)}")
        
        # Botón para reiniciar
        if st.button("Reiniciar Quiz"):
            st.session_state.current_question_index = 0
            st.session_state.score = 0
            st.session_state.quiz_finished = False
            st.rerun()

# Barra lateral
st.sidebar.title("Guía Anatómica")

# Selector de regiones anatómicas
st.sidebar.markdown("## Regiones Anatómicas")
region = st.sidebar.radio("Selecciona una región:", 
                         ["Tracto Superior", "Tracto Inferior", "Estructuras Accesorias"])

# Mostrar información según la región seleccionada
if region == "Tracto Superior":
    st.sidebar.markdown("### Tracto Respiratorio Superior")
    st.sidebar.markdown(RESPIRATORY_SYSTEM_DATA["upper_tract"]["description"])
elif region == "Tracto Inferior":
    st.sidebar.markdown("### Tracto Respiratorio Inferior")
    st.sidebar.markdown(RESPIRATORY_SYSTEM_DATA["lower_tract"]["description"])
else:
    st.sidebar.markdown("### Estructuras Accesorias")
    st.sidebar.markdown(RESPIRATORY_SYSTEM_DATA["accessory_structures"]["description"])

# Información sobre la aplicación
st.sidebar.markdown("---")
st.sidebar.markdown("""
### Acerca de esta aplicación

Esta aplicación educativa interactiva permite explorar la anatomía del sistema respiratorio 
de manera visual y detallada.
""")

# Pie de página
st.markdown("---")
st.markdown("Desarrollado con ❤️ para educación médica y anatómica")