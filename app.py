import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Horario Familiar", page_icon="📅", layout="wide")

st.title("📅 Horario Unificado y Logística de Transporte")
st.write("Visualización integrada de clases y logística de transporte de Brahiam y Esposa.")

# Datos de los horarios
datos = [
    # Lunes
    {"Día": "Lunes", "Persona": "Esposa (Azul)", "Horario": "12:00 PM - 04:00 PM", "Materia / Sede": "Seminario de Investigación / Empatía", "Llevar (🚗)": "🟢 SÍ (12:00 PM)", "Recoger (🚙)": "🟢 SÍ (04:00 PM)"},
    {"Día": "Lunes", "Persona": "Brahiam (Rojo)", "Horario": "06:00 PM - 09:59 PM", "Materia / Sede": "Estadística General (Belén)", "Llevar (🚗)": "N/A", "Recoger (🚙)": "N/A"},
    
    # Martes
    {"Día": "Martes", "Persona": "Esposa (Azul)", "Horario": "LIBRE", "Materia / Sede": "Día Libre", "Llevar (🚗)": "—", "Recoger (🚙)": "—"},
    {"Día": "Martes", "Persona": "Brahiam (Rojo)", "Horario": "06:00 PM - 07:59 PM", "Materia / Sede": "Física de Campos (Fraternidad)", "Llevar (🚗)": "N/A", "Recoger (🚙)": "N/A"},
    {"Día": "Martes", "Persona": "Brahiam (Rojo)", "Horario": "08:00 PM - 09:59 PM", "Materia / Sede": "Cálculo Varias Var. (Castilla)", "Llevar (🚗)": "N/A", "Recoger (🚙)": "N/A"},

    # Miércoles
    {"Día": "Miércoles", "Persona": "Esposa (Azul)", "Horario": "06:00 AM - 02:00 PM", "Materia / Sede": "Taller de Diseño / Higiene", "Llevar (🚗)": "🟢 SÍ (06:00 AM)", "Recoger (🚙)": "🔴 NO (Clase 2:00 PM)"},
    {"Día": "Miércoles", "Persona": "Brahiam (Rojo)", "Horario": "02:00 PM - 03:59 PM", "Materia / Sede": "Electrónica Digital (Robledo)", "Llevar (🚗)": "N/A", "Recoger (🚙)": "N/A"},
    {"Día": "Miércoles", "Persona": "Brahiam (Rojo)", "Horario": "06:00 PM - 07:59 PM", "Materia / Sede": "Física de Campos (Fraternidad)", "Llevar (🚗)": "N/A", "Recoger (🚙)": "N/A"},

    # Jueves
    {"Día": "Jueves", "Persona": "Esposa (Azul)", "Horario": "LIBRE", "Materia / Sede": "Día Libre", "Llevar (🚗)": "—", "Recoger (🚙)": "—"},
    {"Día": "Jueves", "Persona": "Brahiam (Rojo)", "Horario": "08:00 PM - 09:59 PM", "Materia / Sede": "Cálculo Varias Var. (Castilla)", "Llevar (🚗)": "N/A", "Recoger (🚙)": "N/A"},

    # Viernes
    {"Día": "Viernes", "Persona": "Esposa (Azul)", "Horario": "10:00 AM - 02:00 PM", "Materia / Sede": "Seminario Ética / Calidad", "Llevar (🚗)": "🟢 SÍ (10:00 AM)", "Recoger (🚙)": "🔴 NO (Clase 2:00 PM)"},
    {"Día": "Viernes", "Persona": "Brahiam (Rojo)", "Horario": "02:00 PM - 03:59 PM", "Materia / Sede": "Electrónica Digital (Robledo)", "Llevar (🚗)": "N/A", "Recoger (🚙)": "N/A"},
    {"Día": "Viernes", "Persona": "Brahiam (Rojo)", "Horario": "06:00 PM - 07:59 PM", "Materia / Sede": "Física de Campos (Fraternidad)", "Llevar (🚗)": "N/A", "Recoger (🚙)": "N/A"}
]

df = pd.DataFrame(datos)

# Filtro por día
dia_seleccionado = st.radio("Selecciona un día para ver detalle:", ["Todos", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes"], horizontal=True)

if dia_seleccionado != "Todos":
    df_mostrar = df[df["Día"] == dia_seleccionado]
else:
    df_mostrar = df

# Aplicar estilos de color a la tabla
def colorear_filas(val):
    if "Esposa" in str(val):
        return 'background-color: #d0e1fd; color: #082a63; font-weight: bold;'
    elif "Brahiam" in str(val):
        return 'background-color: #fdd0d0; color: #630808; font-weight: bold;'
    return ''

st.dataframe(df_mostrar.style.map(colorear_filas, subset=['Persona']), use_container_width=True, hide_index=True)

st.info("💡 **Recordatorio de transporte:** Los días Miércoles y Viernes a las 2:00 PM Brahiam inicia clase en Robledo, por lo que su esposa debe retornar por su cuenta.")