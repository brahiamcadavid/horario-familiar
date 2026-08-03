import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# Configuración de la página
st.set_page_config(page_title="Agenda Familiar Brahiam & Marcela", page_icon="📅", layout="wide")

st.title("📅 Centro de Control & Agenda Familiar")
st.write("Gestiona horarios, transporte automático, tiempo libre y aulas de la familia.")

# 1. Base de datos inicial
if 'agenda' not in st.session_state:
    st.session_state.agenda = [
        # Lunes
        {"Día": "Lunes", "Integrante": "Marcela", "Hora_Inicio_Num": 12.0, "Hora_Fin_Num": 16.0, "Hora_Inicio": "2026-08-03 12:00", "Hora_Fin": "2026-08-03 16:00", "Horario": "12:00 PM - 04:00 PM", "Actividad": "Seminario de Investigación / Empatía", "Lugar / Aula": "Aula 14-201 / 6-504"},
        {"Día": "Lunes", "Integrante": "Brahiam", "Hora_Inicio_Num": 18.0, "Hora_Fin_Num": 22.0, "Hora_Inicio": "2026-08-03 18:00", "Hora_Fin": "2026-08-03 22:00", "Horario": "06:00 PM - 10:00 PM", "Actividad": "Estadística General", "Lugar / Aula": "Colegio Alcaldía-5 (BELÉN)"},
        
        # Martes
        {"Día": "Martes", "Integrante": "Brahiam", "Hora_Inicio_Num": 18.0, "Hora_Fin_Num": 20.0, "Hora_Inicio": "2026-08-04 18:00", "Hora_Fin": "2026-08-04 20:00", "Horario": "06:00 PM - 08:00 PM", "Actividad": "Física de Campos y Lab.", "Lugar / Aula": "Aula M-106 (FRATERNIDAD)"},
        {"Día": "Martes", "Integrante": "Brahiam", "Hora_Inicio_Num": 20.0, "Hora_Fin_Num": 22.0, "Hora_Inicio": "2026-08-04 20:00", "Hora_Fin": "2026-08-04 22:00", "Horario": "08:00 PM - 10:00 PM", "Actividad": "Cálculo de Varias Var.", "Lugar / Aula": "Aula Cas-306 (CASTILLA)"},

        # Miércoles
        {"Día": "Miércoles", "Integrante": "Marcela", "Hora_Inicio_Num": 6.0, "Hora_Fin_Num": 14.0, "Hora_Inicio": "2026-08-05 06:00", "Hora_Fin": "2026-08-05 14:00", "Horario": "06:00 AM - 02:00 PM", "Actividad": "Taller de Diseño / Higiene", "Lugar / Aula": "Aula 14-201 / 13-304"},
        {"Día": "Miércoles", "Integrante": "Brahiam", "Hora_Inicio_Num": 14.0, "Hora_Fin_Num": 16.0, "Hora_Inicio": "2026-08-05 14:00", "Hora_Fin": "2026-08-05 16:00", "Horario": "02:00 PM - 04:00 PM", "Actividad": "Electrónica Digital", "Lugar / Aula": "Aula C-204 (ROBLEDO)"},
        {"Día": "Miércoles", "Integrante": "Brahiam", "Hora_Inicio_Num": 18.0, "Hora_Fin_Num": 20.0, "Hora_Inicio": "2026-08-05 18:00", "Hora_Fin": "2026-08-05 20:00", "Horario": "06:00 PM - 08:00 PM", "Actividad": "Física de Campos y Lab.", "Lugar / Aula": "Aula M-207 (FRATERNIDAD)"},

        # Jueves
        {"Día": "Jueves", "Integrante": "Brahiam", "Hora_Inicio_Num": 20.0, "Hora_Fin_Num": 22.0, "Hora_Inicio": "2026-08-06 20:00", "Hora_Fin": "2026-08-06 22:00", "Horario": "08:00 PM - 10:00 PM", "Actividad": "Cálculo de Varias Var.", "Lugar / Aula": "Aula Cas-306 (CASTILLA)"},

        # Viernes
        {"Día": "Viernes", "Integrante": "Marcela", "Hora_Inicio_Num": 10.0, "Hora_Fin_Num": 14.0, "Hora_Inicio": "2026-08-07 10:00", "Hora_Fin": "2026-08-07 14:00", "Horario": "10:00 AM - 02:00 PM", "Actividad": "Seminario Ética / Calidad", "Lugar / Aula": "Aula 13-303 / 8-502"},
        {"Día": "Viernes", "Integrante": "Brahiam", "Hora_Inicio_Num": 14.0, "Hora_Fin_Num": 16.0, "Hora_Inicio": "2026-08-07 14:00", "Hora_Fin": "2026-08-07 16:00", "Horario": "02:00 PM - 04:00 PM", "Actividad": "Electrónica Digital", "Lugar / Aula": "Aula G-307 (ROBLEDO)"},
        {"Día": "Viernes", "Integrante": "Brahiam", "Hora_Inicio_Num": 18.0, "Hora_Fin_Num": 20.0, "Hora_Inicio": "2026-08-07 18:00", "Hora_Fin": "2026-08-07 20:00", "Horario": "06:00 PM - 08:00 PM", "Actividad": "Física de Campos y Lab.", "Lugar / Aula": "Aula M-207 (FRATERNIDAD)"}
    ]

# 2. MOTOR DE CÁLCULO DE TRANSPORTE AUTOMÁTICO
def calcular_transporte_automatico(df_total):
    df_brahiam = df_total[df_total['Integrante'] == 'Brahiam']
    
    llevar_list = []
    recoger_list = []
    
    for idx, row in df_total.iterrows():
        if row['Integrante'] == 'Brahiam':
            llevar_list.append("N/A")
            recoger_list.append("N/A")
        else:
            dia = row['Día']
            h_inicio_pasajero = row['Hora_Inicio_Num']
            h_fin_pasajero = row['Hora_Fin_Num']
            
            # Obtener clases de Brahiam ese mismo día
            clases_b_dia = df_brahiam[df_brahiam['Día'] == dia]
            
            # --- EVALUAR LLEVAR ---
            # Brahiam está ocupado a la hora de entrada si la hora cae dentro de alguna de sus clases
            ocupado_llevar = False
            for _, c_b in clases_b_dia.iterrows():
                if c_b['Hora_Inicio_Num'] <= h_inicio_pasajero < c_b['Hora_Fin_Num']:
                    ocupado_llevar = True
                    break
            
            if ocupado_llevar:
                llevar_list.append("🔴 NO (Brahiam en clase)")
            else:
                h_str = datetime.strptime(f"{int(h_inicio_pasajero)}:00", "%H:%M").strftime("%I:%M %p")
                llevar_list.append(f"🟢 SÍ ({h_str})")
                
            # --- EVALUAR RECOGER ---
            # Regla estricta: Si sale justo a la hora que Brahiam ENTRA a clase o mientras Brahiam está en clase, NO se puede.
            ocupado_recoger = False
            for _, c_b in clases_b_dia.iterrows():
                if c_b['Hora_Inicio_Num'] <= h_fin_pasajero <= c_b['Hora_Fin_Num']:
                    ocupado_recoger = True
                    break
            
            if ocupado_recoger:
                recoger_list.append("🔴 NO (Cruza con inicio/clase de Brahiam)")
            else:
                h_str_fin = datetime.strptime(f"{int(h_fin_pasajero)}:00", "%H:%M").strftime("%I:%M %p")
                recoger_list.append(f"🟢 SÍ ({h_str_fin})")
                
    df_total['Llevar (🚗)'] = llevar_list
    df_total['Recoger (🚙)'] = recoger_list
    return df_total

# 3. Formulario Lateral
with st.sidebar:
    st.header("➕ Agregar Nueva Actividad")
    with st.form("form_nueva_actividad"):
        nuevo_integrante = st.selectbox("Integrante", ["Brahiam", "Marcela", "Hijo 1", "Hijo 2", "Familia"])
        nuevo_dia = st.selectbox("Día", ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"])
        nueva_actividad = st.text_input("Actividad / Materia")
        nuevo_lugar = st.text_input("Aula / Sede")
        
        h_inicio_val = st.number_input("Hora Inicio (24h, ej: 14 para 2pm)", min_value=0.0, max_value=23.0, value=8.0, step=0.5)
        h_fin_val = st.number_input("Hora Fin (24h, ej: 16 para 4pm)", min_value=0.5, max_value=24.0, value=10.0, step=0.5)
        
        btn_guardar = st.form_submit_button("Guardar y Recalcular")
        
        if btn_guardar and nueva_actividad:
            dias_dict = {"Lunes": "2026-08-03", "Martes": "2026-08-04", "Miércoles": "2026-08-05", "Jueves": "2026-08-06", "Viernes": "2026-08-07", "Sábado": "2026-08-08", "Domingo": "2026-08-09"}
            fecha_str = dias_dict.get(nuevo_dia, "2026-08-03")
            
            h_in_dt = datetime.strptime(f"{int(h_inicio_val):02d}:{int((h_inicio_val%1)*60):02d}", "%H:%M")
            h_fi_dt = datetime.strptime(f"{int(h_fin_val):02d}:{int((h_fin_val%1)*60):02d}", "%H:%M")
            
            st.session_state.agenda.append({
                "Día": nuevo_dia,
                "Integrante": nuevo_integrante,
                "Hora_Inicio_Num": h_inicio_val,
                "Hora_Fin_Num": h_fin_val,
                "Hora_Inicio": f"{fecha_str} {h_in_dt.strftime('%H:%M')}",
                "Hora_Fin": f"{fecha_str} {h_fi_dt.strftime('%H:%M')}",
                "Horario": f"{h_in_dt.strftime('%I:%M %p')} - {h_fi_dt.strftime('%I:%M %p')}",
                "Actividad": nueva_actividad,
                "Lugar / Aula": nuevo_lugar
            })
            st.success(f"¡Guardado para {nuevo_integrante}! Se han recalculado los cruces de transporte.")

# 4. Sección de Selección de Cruce Automático
st.markdown("### 🔀 Selector de Cruce y Logística Automática")
integrantes_disponibles = list(set([x["Integrante"] for x in st.session_state.agenda]))

col_c1, col_c2 = st.columns(2)
with col_c1:
    persona_cruce = st.selectbox("Selecciona la persona a cruzar con los horarios de Brahiam:", [p for p in integrantes_disponibles if p != "Brahiam"] + ["Todas"])

# Ejecutar el cálculo sobre la base de datos
df_base = pd.DataFrame(st.session_state.agenda)
df_procesado = calcular_transporte_automatico(df_base)

# Filtros visuales
col1, col2, col3 = st.columns(3)
with col1:
    filtro_persona = st.selectbox("👤 Ver en pantalla a:", ["Todos"] + integrantes_disponibles)
with col2:
    filtro_dia = st.selectbox("📅 Día de la semana:", ["Todos", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"])
with col3:
    tipo_vista = st.selectbox("🎨 Estilo de Visualización:", ["📊 Cronograma de Barras (Plotly)", "📆 Google Calendar Style", "📋 Tabla con Cálculo de Transporte"])

# Aplicar filtros
df_view = df_procesado.copy()
if filtro_persona != "Todos":
    df_view = df_view[df_view["Integrante"] == filtro_persona]
if filtro_dia != "Todos":
    df_view = df_view[df_view["Día"] == filtro_dia]

# Métricas de tiempo
if not df_view.empty:
    df_view['Inicio_dt'] = pd.to_datetime(df_view['Hora_Inicio'])
    df_view['Fin_dt'] = pd.to_datetime(df_view['Hora_Fin'])
    df_view['Horas_Invertidas'] = (df_view['Fin_dt'] - df_view['Inicio_dt']).dt.total_seconds() / 3600

st.markdown("---")

if not df_view.empty and filtro_persona != "Todos":
    total_horas = df_view['Horas_Invertidas'].sum()
    libres = 112 - total_horas
    m1, m2 = st.columns(2)
    m1.metric("📚 Horas en Estudio / Actividad", f"{total_horas:.1f} hrs")
    m2.metric("🌴 Tiempo Libre Restante (Lun-Vie 16h/día)", f"{libres:.1f} hrs")

# 5. RENDERIZADO DE VISTAS
if tipo_vista == "📊 Cronograma de Barras (Plotly)":
    st.subheader("📊 Cronograma de Horas Ocupadas y Cruces")
    if not df_view.empty:
        fig = px.timeline(
            df_view, 
            x_start="Inicio_dt", 
            x_end="Fin_dt", 
            y="Día", 
            color="Integrante",
            hover_data=["Actividad", "Lugar / Aula", "Horario", "Llevar (🚗)", "Recoger (🚙)"],
            title="Línea de Tiempo Semanal y Distribución de Horas",
            color_discrete_map={"Brahiam": "#ef553b", "Marcela": "#636efa", "Hijo 1": "#00cc96"}
        )
        fig.update_yaxes(autorange="reversed")
        fig.update_layout(xaxis_title="Hora del Día", yaxis_title="Día de la Semana")
        st.plotly_chart(fig, use_container_width=True)

elif tipo_vista == "📆 Google Calendar Style":
    st.subheader("📆 Rejilla Semanal por Días")
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    cols = st.columns(5)
    
    for i, dia in enumerate(dias_semana):
        with cols[i]:
            st.markdown(f"<h4 style='text-align: center; background-color: #262730; padding: 5px; border-radius: 5px;'>{dia}</h4>", unsafe_allow_html=True)
            df_day = df_view[df_view["Día"] == dia]
            if df_day.empty:
                st.caption("🟢 Día Libre")
            else:
                for _, row in df_day.iterrows():
                    color_bg = "#1e3a8a" if row['Integrante'] == 'Marcela' else "#831843"
                    st.markdown(f"""
                    <div style="background-color: {color_bg}; border-left: 5px solid #00d2ff; padding: 8px; border-radius: 5px; margin-bottom: 8px; color: white;">
                        <span style="font-size: 11px; font-weight: bold;">{row['Horario']}</span><br>
                        <strong>{row['Integrante']}</strong><br>
                        <span>{row['Actividad']}</span><br>
                        <small>📍 {row['Lugar / Aula']}</small><br>
                        <small>🚗 Llevar: {row['Llevar (🚗)']}</small><br>
                        <small>🚙 Recoger: {row['Recoger (🚙)']}</small>
                    </div>
                    """, unsafe_allow_html=True)

elif tipo_vista == "📋 Tabla con Cálculo de Transporte":
    st.subheader("📋 Tabla con Resultados del Cruce Automático")
    df_tabla = df_view[["Día", "Integrante", "Horario", "Actividad", "Lugar / Aula", "Llevar (🚗)", "Recoger (🚙)"]]
    st.dataframe(df_tabla, use_container_width=True, hide_index=True)
