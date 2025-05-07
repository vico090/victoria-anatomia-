"""
Módulo para el modo quiz de la aplicación del sistema respiratorio.
"""
import streamlit as st
import random

def initialize_quiz_state():
    """Inicializa el estado del quiz si aún no existe."""
    if 'quiz_questions' not in st.session_state:
        st.session_state.quiz_questions = []
    if 'current_question_index' not in st.session_state:
        st.session_state.current_question_index = 0
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'quiz_finished' not in st.session_state:
        st.session_state.quiz_finished = False
    if 'answered_current' not in st.session_state:
        st.session_state.answered_current = False

def reset_quiz(questions):
    """Reinicia el quiz con las preguntas dadas."""
    st.session_state.quiz_questions = questions.copy()
    random.shuffle(st.session_state.quiz_questions)
    st.session_state.current_question_index = 0
    st.session_state.score = 0
    st.session_state.quiz_finished = False
    st.session_state.answered_current = False

def next_question():
    """Avanza a la siguiente pregunta."""
    st.session_state.current_question_index += 1
    st.session_state.answered_current = False
    if st.session_state.current_question_index >= len(st.session_state.quiz_questions):
        st.session_state.quiz_finished = True

def check_answer(selected_option, correct_answer):
    """Verifica si la respuesta seleccionada es correcta."""
    st.session_state.answered_current = True
    if selected_option == correct_answer:
        st.session_state.score += 1
        return True
    return False

def display_quiz(questions):
    """Muestra la interfaz del quiz."""
    initialize_quiz_state()
    
    if len(st.session_state.quiz_questions) == 0:
        reset_quiz(questions)
    
    if st.session_state.quiz_finished:
        st.success(f"¡Quiz completado! Tu puntuación: {st.session_state.score}/{len(st.session_state.quiz_questions)}")
        
        # Mostrar mensajes según la puntuación
        percentage = (st.session_state.score / len(st.session_state.quiz_questions)) * 100
        if percentage >= 90:
            st.balloons()
            st.write("¡Excelente! Tienes un gran conocimiento del sistema respiratorio.")
        elif percentage >= 70:
            st.write("¡Muy bien! Tienes un buen conocimiento del sistema respiratorio.")
        elif percentage >= 50:
            st.write("Bien. Tienes un conocimiento básico del sistema respiratorio.")
        else:
            st.write("Te recomendamos repasar más sobre el sistema respiratorio.")
        
        # Botón para reiniciar el quiz
        if st.button("Reiniciar Quiz"):
            reset_quiz(questions)
            st.rerun()
    else:
        # Mostrar pregunta actual
        question_data = st.session_state.quiz_questions[st.session_state.current_question_index]
        
        # Mostrar número de pregunta y puntuación actual
        st.write(f"Pregunta {st.session_state.current_question_index + 1} de {len(st.session_state.quiz_questions)}")
        st.write(f"Puntuación actual: {st.session_state.score}")
        
        st.subheader(question_data["question"])
        
        # Mostrar opciones
        if not st.session_state.answered_current:
            for option in question_data["options"]:
                if st.button(option, key=f"option_{option}"):
                    is_correct = check_answer(option, question_data["answer"])
                    if is_correct:
                        st.success("¡Correcto!")
                    else:
                        st.error(f"Incorrecto. La respuesta correcta es: {question_data['answer']}")
                    st.button("Siguiente pregunta", key="next", on_click=next_question)
        else:
            # Mostrar opciones deshabilitadas después de responder
            for option in question_data["options"]:
                if option == question_data["answer"]:
                    st.success(option)
                elif option == st.session_state.selected_option:
                    st.error(option)
                else:
                    st.write(option)
            
            # Botón para pasar a la siguiente pregunta
            st.button("Siguiente pregunta", key="next", on_click=next_question)
