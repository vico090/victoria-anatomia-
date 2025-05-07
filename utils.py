"""
Utilidades para la aplicación del sistema respiratorio.
"""
import streamlit as st

def create_anatomy_map():
    """
    Crea un mapa SVG interactivo del sistema respiratorio.
    """
    # SVG del sistema respiratorio con areas clickeables
    svg_code = """
    <svg width="600" height="800" viewBox="0 0 600 800" xmlns="http://www.w3.org/2000/svg">
        <!-- Nariz y fosas nasales -->
        <path id="nose" d="M300,100 Q320,120 320,140 Q320,160 300,170 Q280,160 280,140 Q280,120 300,100" 
              fill="#f2a2a2" stroke="#d35f5f" stroke-width="2"/>
        
        <!-- Boca -->
        <path id="mouth" d="M270,180 Q300,210 330,180" 
              fill="none" stroke="#d35f5f" stroke-width="2"/>
        
        <!-- Faringe -->
        <path id="pharynx" d="M300,170 L300,220 Q310,230 300,240 Q290,230 300,220" 
              fill="#f8c9c9" stroke="#d35f5f" stroke-width="2"/>
        
        <!-- Laringe -->
        <path id="larynx" d="M280,240 Q300,250 320,240 L320,270 Q300,280 280,270 Z" 
              fill="#eb8a8a" stroke="#d35f5f" stroke-width="2"/>
        
        <!-- Tráquea -->
        <path id="trachea" d="M290,270 L290,320 Q300,325 310,320 L310,270" 
              fill="#f8c9c9" stroke="#d35f5f" stroke-width="2"/>
        
        <!-- Bronquios principales -->
        <path id="bronchi" d="M290,320 Q270,340 250,350 M310,320 Q330,340 350,350" 
              fill="none" stroke="#d35f5f" stroke-width="3"/>
        
        <!-- Pulmón derecho (izquierdo en la imagen) -->
        <path id="lungs" d="M200,350 Q240,330 250,350 Q270,390 270,450 Q260,520 230,560 Q200,580 180,560 Q150,520 150,460 Q150,400 200,350 Z" 
              fill="#ffd9d9" stroke="#d35f5f" stroke-width="2"/>
        
        <!-- Pulmón izquierdo (derecho en la imagen) -->
        <path id="lungs" d="M400,350 Q360,330 350,350 Q330,390 330,450 Q340,520 370,560 Q400,580 420,560 Q450,520 450,460 Q450,400 400,350 Z" 
              fill="#ffd9d9" stroke="#d35f5f" stroke-width="2"/>
        
        <!-- Bronquios secundarios pulmón derecho -->
        <path id="bronchi" d="M250,350 Q240,360 230,380 M250,350 Q250,370 260,390 M250,350 Q230,370 220,410" 
              fill="none" stroke="#d35f5f" stroke-width="2"/>
        
        <!-- Bronquios secundarios pulmón izquierdo -->
        <path id="bronchi" d="M350,350 Q360,360 370,380 M350,350 Q350,370 340,390 M350,350 Q370,370 380,410" 
              fill="none" stroke="#d35f5f" stroke-width="2"/>
        
        <!-- Diafragma -->
        <path id="thoracic_wall" d="M150,520 Q200,560 300,570 Q400,560 450,520" 
              fill="none" stroke="#888888" stroke-width="3"/>
        
        <!-- Pleura (simplificada) -->
        <path id="pleura" d="M160,360 Q210,340 240,360 Q260,400 260,450 Q250,510 225,550 Q200,570 180,550 Q160,510 160,460 Q160,400 160,360 Z" 
              fill="none" stroke="#5555ff" stroke-width="1" stroke-dasharray="5,5"/>
        
        <path id="pleura" d="M440,360 Q390,340 360,360 Q340,400 340,450 Q350,510 375,550 Q400,570 420,550 Q440,510 440,460 Q440,400 440,360 Z" 
              fill="none" stroke="#5555ff" stroke-width="1" stroke-dasharray="5,5"/>
        
        <!-- Unidades respiratorias (simplificadas) -->
        <circle id="respiratory_unit" cx="230" cy="420" r="5" fill="#ff7777" stroke="#d35f5f"/>
        <circle id="respiratory_unit" cx="200" cy="450" r="5" fill="#ff7777" stroke="#d35f5f"/>
        <circle id="respiratory_unit" cx="210" cy="500" r="5" fill="#ff7777" stroke="#d35f5f"/>
        
        <circle id="respiratory_unit" cx="370" cy="420" r="5" fill="#ff7777" stroke="#d35f5f"/>
        <circle id="respiratory_unit" cx="400" cy="450" r="5" fill="#ff7777" stroke="#d35f5f"/>
        <circle id="respiratory_unit" cx="390" cy="500" r="5" fill="#ff7777" stroke="#d35f5f"/>
        
        <!-- Senos paranasales (simplificados) -->
        <path id="sinuses" d="M290,80 Q300,70 310,80 Q315,90 310,100 Q300,105 290,100 Q285,90 290,80 Z" 
              fill="#f8e9e9" stroke="#d35f5f" stroke-width="1"/>
        
        <!-- Etiquetas -->
        <text x="300" y="60" text-anchor="middle" font-size="12" fill="#333">Senos Paranasales</text>
        <text x="300" y="95" text-anchor="middle" font-size="12" fill="#333">Nariz</text>
        <text x="300" y="195" text-anchor="middle" font-size="12" fill="#333">Faringe</text>
        <text x="300" y="255" text-anchor="middle" font-size="12" fill="#333">Laringe</text>
        <text x="320" y="300" text-anchor="middle" font-size="12" fill="#333">Tráquea</text>
        <text x="250" y="330" text-anchor="middle" font-size="12" fill="#333">Bronquios</text>
        <text x="200" y="400" text-anchor="middle" font-size="12" fill="#333">Pulmón</text>
        <text x="400" y="400" text-anchor="middle" font-size="12" fill="#333">Pulmón</text>
        <text x="300" y="540" text-anchor="middle" font-size="12" fill="#333">Diafragma</text>
        <text x="350" y="560" text-anchor="start" font-size="10" fill="#5555ff">Pleura</text>
        <text x="225" cy="420" text-anchor="middle" font-size="9" fill="#333">Unidades</text>
        <text x="225" cy="430" text-anchor="middle" font-size="9" fill="#333">Respiratorias</text>
    </svg>
    """
    
    # Código JavaScript para hacer interactivo el SVG
    js = """
    <script>
    const parts = document.querySelectorAll('path, circle');
    parts.forEach(part => {
        part.style.cursor = 'pointer';
        part.addEventListener('click', function(e) {
            const partId = this.id;
            if (partId) {
                // Enviar el ID a Streamlit
                parent.postMessage({type: 'streamlit:setComponentValue', value: partId}, '*');
            }
        });
        
        part.addEventListener('mouseover', function() {
            this.setAttribute('stroke-width', parseInt(this.getAttribute('stroke-width')) + 2);
            this.style.fill = this.style.fill.replace(')', ', 0.7)').replace('rgb', 'rgba');
        });
        
        part.addEventListener('mouseout', function() {
            this.setAttribute('stroke-width', parseInt(this.getAttribute('stroke-width')) - 2);
            this.style.fill = this.style.fill.replace(', 0.7)', ')').replace('rgba', 'rgb');
        });
    });
    </script>
    """
    
    # Combinar SVG y JavaScript
    html_code = f"""
    <div style="width:100%; text-align:center;">
        {svg_code}
        {js}
    </div>
    """
    
    return html_code

def find_structure_by_id(structure_id, data):
    """
    Busca una estructura por su ID en los datos del sistema respiratorio.
    
    Args:
        structure_id: ID de la estructura a buscar
        data: Diccionario con los datos del sistema respiratorio
    
    Returns:
        Diccionario con los datos de la estructura o None si no se encuentra
    """
    # Buscar en el tracto respiratorio superior
    for structure in data["upper_tract"]["structures"]:
        if structure["id"] == structure_id:
            return structure
    
    # Buscar en el tracto respiratorio inferior
    for structure in data["lower_tract"]["structures"]:
        if structure["id"] == structure_id:
            return structure
    
    # Buscar en las estructuras accesorias
    for structure in data["accessory_structures"]["structures"]:
        if structure["id"] == structure_id:
            return structure
    
    # Si es el mediastino
    if structure_id == "mediastinum":
        return data["mediastinum"]
    
    return None

def display_structure_info(structure):
    """
    Muestra la información de una estructura del sistema respiratorio.
    
    Args:
        structure: Diccionario con los datos de la estructura
    """
    if structure:
        st.subheader(structure["name"])
        st.write(structure["description"])
        
        if "function" in structure:
            st.markdown("**Función:**")
            st.write(structure["function"])
    else:
        st.warning("Selecciona una parte del sistema respiratorio para ver información detallada.")

def get_all_structures(data):
    """
    Obtiene todas las estructuras del sistema respiratorio.
    
    Args:
        data: Diccionario con los datos del sistema respiratorio
    
    Returns:
        Lista de diccionarios con todas las estructuras
    """
    structures = []
    
    # Añadir estructuras del tracto respiratorio superior
    structures.extend(data["upper_tract"]["structures"])
    
    # Añadir estructuras del tracto respiratorio inferior
    structures.extend(data["lower_tract"]["structures"])
    
    # Añadir estructuras accesorias
    structures.extend(data["accessory_structures"]["structures"])
    
    # Añadir el mediastino
    structures.append(data["mediastinum"])
    
    return structures
