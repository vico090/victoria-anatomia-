"""
Este módulo contiene los datos anatómicos del sistema respiratorio.
"""

# Información detallada sobre las estructuras del sistema respiratorio
# Basado en el documento "Sistema respiratorio - copia (3).pdf"

# Estructura principal del sistema respiratorio
RESPIRATORY_SYSTEM = {
    "name": "Sistema Respiratorio",
    "description": "El sistema respiratorio está formado por las estructuras que realizan el intercambio de gases entre la atmósfera y la sangre. El oxígeno (O2) es introducido dentro del cuerpo para su posterior distribución a los tejidos y el dióxido de carbono (CO2) producido por el metabolismo celular, es eliminado al exterior. Además interviene en la regulación del pH corporal, en la protección contra los agentes patógenos y las sustancias irritantes que son inhalados y en la vocalización."
}

# Tracto respiratorio superior
UPPER_TRACT = {
    "name": "Tracto Respiratorio Superior",
    "description": "Comprende las estructuras respiratorias ubicadas fuera del tórax.",
    "structures": [
        {
            "id": "nose",
            "name": "Nariz y Fosas Nasales",
            "description": "La nariz es la parte superior del sistema respiratorio y varía en tamaño y forma en diferentes personas. Se proyecta hacia adelante desde la cara. En el interior de la nariz se encuentra el tabique nasal que divide a la cavidad nasal en dos partes llamadas las fosas nasales. Las fosas nasales en su parte más exterior están recubiertas por piel que contiene vibrisas (pelos) que atrapan partículas suspendidas en el aire inspirado.",
            "function": "Filtra, calienta y humedece el aire inspirado. También contiene los receptores del olfato."
        },
        {
            "id": "sinuses",
            "name": "Senos Paranasales",
            "description": "Los senos paranasales son cavidades llenas de aire que se originan al introducirse la mucosa de la cavidad nasal en los huesos del cráneo contiguos. Incluyen los senos frontales, etmoidales, esfenoidales y maxilares.",
            "function": "Reducen el peso del cráneo, dan resonancia a la voz y producen moco que drena hacia las fosas nasales."
        },
        {
            "id": "mouth",
            "name": "Boca",
            "description": "La boca es la primera parte del tubo digestivo aunque también se emplea para respirar. Está tapizada por una membrana mucosa y limitada por las mejillas y los labios. El techo de la cavidad oral está formado por el paladar.",
            "function": "Vía alternativa para la respiración cuando las fosas nasales están bloqueadas."
        },
        {
            "id": "pharynx",
            "name": "Faringe",
            "description": "La faringe es un tubo que continúa a la boca y constituye el extremo superior común de los tubos respiratorio y digestivo. Se divide en 3 partes: nasofaringe, orofaringe y laringofaringe.",
            "function": "Paso de aire hacia las vías respiratorias inferiores y alimentos hacia el esófago."
        },
        {
            "id": "larynx",
            "name": "Laringe",
            "description": "Es un órgano especializado que se encarga de la fonación o emisión de sonidos con la ayuda de las cuerdas vocales. Está localizada entre la laringofaringe y la tráquea y es una parte esencial de las vías aéreas.",
            "function": "Producción de sonidos, evita el paso de sólidos y líquidos a las vías respiratorias inferiores."
        },
        {
            "id": "trachea",
            "name": "Tráquea",
            "description": "La tráquea es un tubo cilíndrico, semiflexible, de unos 10-12 cm de longitud y 2,5 cm de diámetro que se extiende desde la laringe hasta el mediastino, a nivel de la 5ª vértebra torácica, donde se divide en los bronquios principales derecho e izquierdo.",
            "function": "Conduce el aire desde la laringe hasta los bronquios."
        }
    ]
}

# Tracto respiratorio inferior
LOWER_TRACT = {
    "name": "Tracto Respiratorio Inferior",
    "description": "Comprende las estructuras respiratorias ubicadas dentro del tórax.",
    "structures": [
        {
            "id": "bronchi",
            "name": "Bronquios",
            "description": "Los bronquios son las ramificaciones de la tráquea que conducen el aire hacia los pulmones. El bronquio principal derecho es más vertical, más corto y más ancho que el izquierdo y se divide en 3 bronquios lobares que ventilan los 3 lóbulos del pulmón derecho. El bronquio principal izquierdo es más horizontal, más largo y más estrecho que el derecho y se divide en 2 bronquios lobares que ventilan los 2 lóbulos del pulmón izquierdo.",
            "function": "Conducir el aire desde la tráquea hasta los bronquiolos y alvéolos pulmonares."
        },
        {
            "id": "lungs",
            "name": "Pulmones",
            "description": "Los pulmones son los órganos esenciales de la respiración. Son ligeros, blandos, esponjosos y muy elásticos y están situados en la cavidad torácica a ambos lados del mediastino. Tienen forma de cono con una base inferior apoyada en el diafragma y un vértice o ápex redondeado que se extiende por encima de la primera costilla. El pulmón derecho está dividido en tres lóbulos (superior, medio e inferior) por dos cisuras (oblicua y horizontal) y el pulmón izquierdo en dos lóbulos (superior e inferior) por una cisura (oblicua).",
            "function": "Realizar el intercambio gaseoso: captación de oxígeno y eliminación de dióxido de carbono."
        },
        {
            "id": "respiratory_unit",
            "name": "Unidad Respiratoria",
            "description": "La unidad respiratoria está formada por un bronquiolo respiratorio, conductos alveolares, atrios, sacos alveolares y alvéolos. Es la unidad funcional del pulmón donde se realiza el intercambio gaseoso.",
            "function": "Intercambio de gases entre el aire y la sangre."
        }
    ]
}

# Estructuras accesorias
ACCESSORY_STRUCTURES = {
    "name": "Estructuras Accesorias",
    "description": "Estructuras que ayudan en el proceso respiratorio.",
    "structures": [
        {
            "id": "pleura",
            "name": "Pleuras",
            "description": "Las pleuras son membranas serosas que recubren los pulmones y la cavidad torácica. Cada pulmón está recubierto por la pleura visceral y la pared de la cavidad torácica está recubierta por la pleura parietal. Entre ambas pleuras existe un espacio virtual llamado cavidad pleural que contiene una pequeña cantidad de líquido pleural que actúa como lubricante.",
            "function": "Facilitar el deslizamiento de los pulmones durante los movimientos respiratorios y mantener los pulmones adheridos a la pared torácica."
        },
        {
            "id": "thoracic_wall",
            "name": "Pared Torácica",
            "description": "La pared torácica está formada por la caja torácica ósea (constituida por las costillas, el esternón y las vértebras torácicas), las articulaciones entre estos huesos, y los músculos que recubren el esqueleto óseo y rellenan los espacios intercostales.",
            "function": "Proteger los órganos torácicos y participar en los movimientos respiratorios."
        }
    ]
}

# Mediastino
MEDIASTINUM = {
    "name": "Mediastino",
    "description": "El mediastino es la región de la cavidad torácica situada entre los dos pulmones. Contiene el corazón y los grandes vasos, la tráquea, el esófago, el timo, ganglios linfáticos y nervios.",
    "function": "Alojar y proteger órganos vitales como el corazón, grandes vasos sanguíneos y otras estructuras."
}

# Todos los datos del sistema respiratorio
RESPIRATORY_SYSTEM_DATA = {
    "system": RESPIRATORY_SYSTEM,
    "upper_tract": UPPER_TRACT,
    "lower_tract": LOWER_TRACT,
    "accessory_structures": ACCESSORY_STRUCTURES,
    "mediastinum": MEDIASTINUM
}

# Preguntas para el modo quiz
QUIZ_QUESTIONS = [
    {
        "question": "¿Qué estructura divide la cavidad nasal en dos partes?",
        "options": ["Cornetes nasales", "Tabique nasal", "Meatos", "Coanas"],
        "answer": "Tabique nasal"
    },
    {
        "question": "¿Cuántos lóbulos tiene el pulmón derecho?",
        "options": ["1", "2", "3", "4"],
        "answer": "3"
    },
    {
        "question": "¿Qué estructura conecta la faringe con los bronquios?",
        "options": ["Laringe", "Tráquea", "Esófago", "Epiglotis"],
        "answer": "Tráquea"
    },
    {
        "question": "¿Cuántas partes se distinguen en la faringe?",
        "options": ["1", "2", "3", "4"],
        "answer": "3"
    },
    {
        "question": "Los senos paranasales se encuentran en los siguientes huesos EXCEPTO:",
        "options": ["Frontal", "Etmoides", "Temporal", "Maxilar"],
        "answer": "Temporal"
    },
    {
        "question": "¿Qué estructura separa la cavidad torácica de la abdominal?",
        "options": ["Pleura", "Pericardio", "Diafragma", "Mediastino"],
        "answer": "Diafragma"
    },
    {
        "question": "La unidad funcional del pulmón donde se realiza el intercambio gaseoso es:",
        "options": ["Bronquio", "Bronquiolo", "Unidad respiratoria", "Alvéolo"],
        "answer": "Unidad respiratoria"
    },
    {
        "question": "¿Qué membranas recubren los pulmones?",
        "options": ["Pleuras", "Pericardio", "Peritoneo", "Meninges"],
        "answer": "Pleuras"
    },
    {
        "question": "¿Cuál de las siguientes NO es una función del sistema respiratorio?",
        "options": ["Intercambio de gases", "Regulación del pH", "Digestión de alimentos", "Fonación"],
        "answer": "Digestión de alimentos"
    },
    {
        "question": "¿Qué estructura se encarga de la producción de sonidos?",
        "options": ["Faringe", "Laringe", "Tráquea", "Epiglotis"],
        "answer": "Laringe"
    }
]
