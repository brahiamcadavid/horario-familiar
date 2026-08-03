import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Agenda Familiar Brahiam", page_icon="📅", layout="wide")

st.title("📅 Centro de Control & Agenda Familiar")
st.write("Gestiona horarios, transporte y actividades de toda la familia.")

# 1. Base de datos inicial (Estado de la sesión)
if 'agenda' not in st.session_state:
    st.session_state.agenda = [
        # Lunes
        {"Día": "Lunes", "Integrante": "Esposa", "Horario": "12:00 PM - 04:00 PM", "Actividad / Sede": "Seminario de Investigación / Empatía", "Llevar (🚗)": "🟢 SÍ (12:00 PM)", "Recoger (🚙)": "🟢 SÍ (04:00 PM)"},
        {"Día": "Lunes", "Integrante": "Brahiam", "Horario": "06:00 PM - 09:59 PM", "Actividad / Sede": "Estadística General (Belén)", "Llevar (🚗)": "N/A", "Recoger (🚙)": "N/A"},
        
        # Martes
        {"Día": "Martes", "Integrante": "Brahiam", "Horario": "06:00 PM - 07:59 PM", "Actividad / Sede": "Física de Campos (Fraternidad)", "Llevar (🚗)": "N/A", "Recoger (🚙)": "N/A"},
        {"Día": "Martes", "Integrante": "Brahiam", "Horario": "08:00 PM - 09:59 PM", "Actividad / Sede": "Cálculo Varias Var. (Castilla)", "Llevar (🚗)": "N/A", "Recoger (🚙)": "N/A"},

        # Miércoles
        {"Día": "Miércoles", "Integrante": "Esposa", "Horario": "06:00 AM - 02:00 PM", "Actividad / Sede": "Taller de Diseño / Higiene", "Llevar (🚗)": "🟢 SÍ (06:00 AM)", "Recoger (🚙)": "🔴 NO (Clase 2:00 PM)"},
        {"Día": "Miércoles", "Integrante": "Brahiam", "Horario": "02:00 PM - 03:59 PM", "Actividad / Sede": "Electrónica Digital (Robledo)", "Llevar (🚗)": "N/A", "Recoger (🚙)": "N/A"},
        {"Día": "Miércoles", "Integrante": "Brahiam", "Horario": "06:00 PM - 07:59 PM", "Actividad / Sede": "Física de Campos (Fraternidad)", "Llevar (🚗)": "N/A", "Recoger (🚙)": "N/A"},

        # Jueves
        {"Día": "Jueves", "Integrante": "Brahiam", "Horario": "08:00 PM - 09:59 PM", "Actividad / Sede": "Cálculo Varias Var. (Castilla)", "Llevar (🚗)": "N/A", "Recoger (🚙)": "N/A"},

        # Viernes
        {"Día": "Viernes", "Integrante": "Esposa", "Horario": "10:00 AM - 02:00 PM", "Actividad / Sede": "Seminario Ética / Calidad", "Llevar (🚗)": "🟢 SÍ (10:00 AM)", "Recoger (🚙)": "🔴 NO (Clase 2:00 PM)"},
        {"Día": "Viernes", "Integrante": "Brahiam", "Horario": "02:00 PM - 03:59 PM", "Actividad / Sede": "Electrónica Digital (Robledo)", "Llevar (🚗)": "N/A", "Recoger (🚙)": "N/A"},
        {"Día": "Viernes", "Integrante": "Brahiam", "Horario": "06:00 PM - 07:59 PM", "Actividad / Sede": "Física de Campos (Fraternidad)", "Llevar (🚗)": "N/A", "Recoger (🚙)": "N/A"}
    ]

# 2. Panel Lateral: Agregar nueva actividad
with st.sidebar:
    st.header("➕ Agregar Nueva Actividad")
    with st.form("form_nueva_actividad"):
        nuevo_integrante = st.selectbox("Integrante", ["Brahiam", "Esposa", "Hijo 1", "Hijo 2", "Familia"])
        nuevo_dia = st.selectbox("Día", ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"])
        nueva_actividad = st.text_input("Actividad / Materia / Evento")
        nuevo_horario = st.text_input("Horario (ej: 08:00 AM - 12:00 PM)")
        llevar = st.selectbox("¿Requiere LLEVAR?", ["N/A", "🟢 SÍ", "🔴 NO"])
        recoger = st.selectbox("¿Requiere RECOGER?", ["N/A", "🟢 SÍ", "🔴 NO"])
        
        btn_guardar = st.form_submit_button("Guardar en Agenda")
        
        if btn_guardar and nueva_actividad:
            nueva_entry = {
                "Día": nuevo_dia,
                "Integrante": nuevo_integrante,
                "Horario": nuevo_horario,
                "Actividad / Sede": nueva_actividad,
                "Llevar (🚗)": llevar,
                "Recoger (🚙)": recoger
            }
            st.session_state.agenda.append(nueva_entry)
            st.success(f"¡Actividad agregada para {nuevo_integrante}!")

# 3. Filtros Principales
col1, col2 = st.columns(2)

with col1:
    # Lista de integrantes dinámicos
    integrantes_disponibles = ["Todos"] + list(set([x["Integrante"] for x in st.session_state.agenda]))
    filtro_persona = st.selectbox("👤 Filtrar por Integrante:", integrantes_disponibles)

with col2:
    filtro_dia = st.selectbox("📅 Filtrar por Día:", ["Todos", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"])

# Convertir a DataFrame
df = pd.DataFrame(st.session_state.agenda)

# Aplicar Filtros
if filtro_persona != "Todos":
    df = df[df["Integrante"] == filtro_persona]

if filtro_dia != "Todos":
    df = df[df["Día"] == filtro_dia]

# Estilos de color según la persona
def colorear_filas(val):
    if "Esposa" in str(val):
        return 'background-color: #d0e1fd; color: #082a63; font-weight: bold;'
    elif "Brahiam" in str(val):
        return 'background-color: #fdd0d0; color: #630808; font-weight: bold;'
    elif "Hijo" in str(val):
        return 'background-color: #d0fdd7; color: #086317; font-weight: bold;'
    return ''

# Mostrar la tabla formateada
st.subheader("📋 Vista de Horarios y Tareas")
if not df.empty:
    st.dataframe(df.style.map(colorear_filas, subset=['Integrante']), use_container_width=True, hide_index=True)
else:
    st.warning("No hay actividades registradas para los filtros seleccionados.")

# 4. Sección de Recordatorios
st.markdown("---")
st.subheader("🔔 Recordatorios Automáticos")
st.info("💡 **Sugerencia de Recordatorios:** Para recibir alarmas sonoras en el celular, te recomiendo exportar los eventos a tu Google Calendar personal. Próximamente podremos conectar un Bot automático de Telegram que les envíe un mensaje al celular 30 minutos antes de cada trayecto de transporte.")
