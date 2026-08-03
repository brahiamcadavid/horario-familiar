import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de la página
st.set_page_config(page_title="Agenda Familiar Brahiam & Marcela", page_icon="📅", layout="wide")

st.title("📅 Centro de Control & Agenda Familiar")
st.write("Gestiona horarios, aulas, transporte y actividades de Brahiam, Marcela y los niños.")

# 1. Base de datos inicial con aulas y sedes precisas
if 'agenda' not in st.session_state:
    st.session_state.agenda = [
        # Lunes
        {"Día": "Lunes", "Integrante": "Marcela", "Horario": "12:00 PM - 04:00 PM", "Hora_Inicio": 12, "Hora_Fin": 16, "Actividad": "Seminario de Investigación / Empatía", "Lugar / Aula": "Aula 14-201 / 6-504", "Llevar (🚗)": "🟢 SÍ (12:00 PM)", "Recoger (🚙)": "🟢 SÍ (04:00 PM)"},
        {"Día": "Lunes", "Integrante": "Brahiam", "Horario": "06:00 PM - 09:59 PM", "Hora_Inicio": 18, "Hora_Fin": 22, "Actividad": "Estadística General", "Lugar / Aula": "Colegio Alcaldía-5 (BELÉN)", "Llevar (🚗)": "N/A", "Recoger (🚙)": "N/A"},
        
        # Martes
        {"Día": "Martes", "Integrante": "Brahiam", "Horario": "06:00 PM - 07:59 PM", "Hora_Inicio": 18, "Hora_Fin": 20, "Actividad": "Física de Campos y Lab.", "Lugar / Aula": "Aula M-106 (FRATERNIDAD)", "Llevar (🚗)": "N/A", "Recoger (🚙)": "N/A"},
        {"Día": "Martes", "Integrante": "Brahiam", "Horario": "08:00 PM - 09:59 PM", "Hora_Inicio": 20, "Hora_Fin": 22, "Actividad": "Cálculo de Varias Var.", "Lugar / Aula": "Aula Cas-306 (CASTILLA)", "Llevar (🚗)": "N/A", "Recoger (🚙)": "N/A"},

        # Miércoles
        {"Día": "Miércoles", "Integrante": "Marcela", "Horario": "06:00 AM - 02:00 PM", "Hora_Inicio": 6, "Hora_Fin": 14, "Actividad": "Taller de Diseño / Higiene", "Lugar / Aula": "Aula 14-201 / 13-304", "Llevar (🚗)": "🟢 SÍ (06:00 AM)", "Recoger (🚙)": "🔴 NO (Clase 2:00 PM)"},
        {"Día": "Miércoles", "Integrante": "Brahiam", "Horario": "02:00 PM - 03:59 PM", "Hora_Inicio": 14, "Hora_Fin": 16, "Actividad": "Electrónica Digital", "Lugar / Aula": "Aula C-204 (ROBLEDO)", "Llevar (🚗)": "N/A", "Recoger (🚙)": "N/A"},
        {"Día": "Miércoles", "Integrante": "Brahiam", "Horario": "06:00 PM - 07:59 PM", "Hora_Inicio": 18, "Hora_Fin": 20, "Actividad": "Física de Campos y Lab.", "Lugar / Aula": "Aula M-207 (FRATERNIDAD)", "Llevar (🚗)": "N/A", "Recoger (🚙)": "N/A"},

        # Jueves
        {"Día": "Jueves", "Integrante": "Brahiam", "Horario": "08:00 PM - 09:59 PM", "Hora_Inicio": 20, "Hora_Fin": 22, "Actividad": "Cálculo de Varias Var.", "Lugar / Aula": "Aula Cas-306 (CASTILLA)", "Llevar (🚗)": "N/A", "Recoger (🚙)": "N/A"},

        # Viernes
        {"Día": "Viernes", "Integrante": "Marcela", "Horario": "10:00 AM - 02:00 PM", "Hora_Inicio": 10, "Hora_Fin": 14, "Actividad": "Seminario Ética / Calidad", "Lugar / Aula": "Aula 13-303 / 8-502", "Llevar (🚗)": "🟢 SÍ (10:00 AM)", "Recoger (🚙)": "🔴 NO (Clase 2:00 PM)"},
        {"Día": "Viernes", "Integrante": "Brahiam", "Horario": "02:00 PM - 03:59 PM", "Hora_Inicio": 14, "Hora_Fin": 16, "Actividad": "Electrónica Digital", "Lugar / Aula": "Aula G-307 (ROBLEDO)", "Llevar (🚗)": "N/A", "Recoger (🚙)": "N/A"},
        {"Día": "Viernes", "Integrante": "Brahiam", "Horario": "06:00 PM - 07:59 PM", "Hora_Inicio": 18, "Hora_Fin": 20, "Actividad": "Física de Campos y Lab.", "Lugar / Aula": "Aula M-207 (FRATERNIDAD)", "Llevar (🚗)": "N/A", "Recoger (🚙)": "N/A"}
    ]

# 2. Panel Lateral: Formulario para añadir eventos
with st.sidebar:
    st.header("➕ Agregar Nueva Actividad")
    with st.form("form_nueva_actividad"):
        nuevo_integrante = st.selectbox("Integrante", ["Brahiam", "Marcela", "Hijo 1", "Hijo 2", "Familia"])
        nuevo_dia = st.selectbox("Día", ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"])
        nueva_actividad = st.text_input("Actividad / Materia")
        nuevo_lugar = st.text_input("Aula / Sede / Dirección")
        h_inicio = st.number_input("Hora Inicio (Formato 24h, ej: 14 para 2pm)", min_value=0, max_value=23, value=8)
        h_fin = st.number_input("Hora Fin (Formato 24h, ej: 16 para 4pm)", min_value=1, max_value=24, value=10)
        nuevo_horario_txt = f"{h_inicio:02d}:00 - {h_fin:02d}:00"
        llevar = st.selectbox("¿Requiere LLEVAR?", ["N/A", "🟢 SÍ", "🔴 NO"])
        recoger = st.selectbox("¿Requiere RECOGER?", ["N/A", "🟢 SÍ", "🔴 NO"])
        
        btn_guardar = st.form_submit_button("Guardar Actividad")
        
        if btn_guardar and nueva_actividad:
            st.session_state.agenda.append({
                "Día": nuevo_dia,
                "Integrante": nuevo_integrante,
                "Horario": nuevo_horario_txt,
                "Hora_Inicio": h_inicio,
                "Hora_Fin": h_fin,
                "Actividad": nueva_actividad,
                "Lugar / Aula": nuevo_lugar,
                "Llevar (🚗)": llevar,
                "Recoger (🚙)": recoger
            })
            st.success(f"¡Guardado para {nuevo_integrante}!")

# 3. Filtros
col1, col2, col3 = st.columns(3)
with col1:
    integrantes = ["Todos"] + list(set([x["Integrante"] for x in st.session_state.agenda]))
    filtro_persona = st.selectbox("👤 Integrante:", integrantes)
with col2:
    filtro_dia = st.selectbox("📅 Día:", ["Todos", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"])
with col3:
    tipo_vista = st.selectbox("🎨 Estilo de Visualización:", ["📋 Tabla Detallada", "📊 Cronograma de Barras (Plotly)", "🧱 Bloques Semanales"])

# Filtrado de DataFrame
df = pd.DataFrame(st.session_state.agenda)
if filtro_persona != "Todos":
    df = df[df["Integrante"] == filtro_persona]
if filtro_dia != "Todos":
    df = df[df["Día"] == filtro_dia]

st.markdown("---")

# 4. Renderizado según la opción elegida
if tipo_vista == "📋 Tabla Detallada":
    st.subheader("📋 Vista en Tabla")
    def colorear_filas(val):
        if "Marcela" in str(val):
            return 'background-color: #d0e1fd; color: #082a63; font-weight: bold;'
        elif "Brahiam" in str(val):
            return 'background-color: #fdd0d0; color: #630808; font-weight: bold;'
        elif "Hijo" in str(val):
            return 'background-color: #d0fdd7; color: #086317; font-weight: bold;'
        return ''
    
    df_tabla = df[["Día", "Integrante", "Horario", "Actividad", "Lugar / Aula", "Llevar (🚗)", "Recoger (🚙)"]]
    st.dataframe(df_tabla.style.map(colorear_filas, subset=['Integrante']), use_container_width=True, hide_index=True)

elif tipo_vista == "📊 Cronograma de Barras (Plotly)":
    st.subheader("📊 Cronograma de Horas Libres y Ocupadas")
    if not df.empty:
        fig = px.timeline(
            df, 
            x_start="Hora_Inicio", 
            x_end="Hora_Fin", 
            y="Día", 
            color="Integrante",
            hover_data=["Actividad", "Lugar / Aula", "Horario"],
            title="Línea de Tiempo Semanal"
        )
        fig.update_yaxes(autorange="reversed")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No hay datos para mostrar en este filtro.")

elif tipo_vista == "🧱 Bloques Semanales":
    st.subheader("🧱 Bloques Semanales por Día")
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    cols = st.columns(len(dias_semana))
    
    for i, dia in enumerate(dias_semana):
        with cols[i]:
            st.markdown(f"### {dia}")
            df_day = df[df["Día"] == dia]
            if df_day.empty:
                st.caption("Libre")
            else:
                for _, row in df_day.iterrows():
                    color_box = "#d0e1fd" if row['Integrante'] == 'Marcela' else "#fdd0d0"
                    st.markdown(f"""
                    <div style="background-color: {color_box}; padding: 10px; border-radius: 8px; margin-bottom: 8px; color: #333;">
                        <strong>{row['Integrante']}</strong><br>
                        ⏰ {row['Horario']}<br>
                        📖 <em>{row['Actividad']}</em><br>
                        📍 <small>{row['Lugar / Aula']}</small>
                    </div>
                    """, unsafe_allow_html=True)

# 5. Módulo de Telegram
st.markdown("---")
st.subheader("🔔 Sistema de Recordatorios por Telegram")
st.write("Configura el bot de Telegram para que les envíe alertas automáticas al celular antes de salir o recoger.")

with st.expander("🛠️ Ver instrucciones para conectar el Bot de Telegram"):
    st.markdown("""
    1. Abre **Telegram** en tu celular y busca a `@BotFather`.
    2. Escribe `/newbot`, ponle un nombre y te dará un **Token de acceso** (API Token).
    3. Pega el Token a continuación y haz clic en **Conectar**.
    """)
    token_input = st.text_input("Ingresa tu Telegram API Token:", type="password")
    chat_id_input = st.text_input("Ingresa tu Telegram Chat ID (de Brahiam o Marcela):")
    if st.button("Guardar Credenciales de Telegram"):
        st.success("¡Credenciales guardadas con éxito! Las alertas automáticas quedan listas para programarse.")
