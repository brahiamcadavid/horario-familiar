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
            
            clases_b_dia = df_brahiam[df_brahiam['Día'] == dia]
            
            # Evaluar Llevar
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
                
            # Evaluar Recoger
            ocupado_recoger = False
            for _, c_b in clases_b_dia.iterrows():
                if c_b['Hora_Inicio_Num'] <= h_fin_pasajero <= c_b['Hora_Fin_Num']:
                    ocupado_recoger = True
                    break
            
            if ocupado_recoger:
                recoger_list.append("🔴 NO (Brahiam inicia/está en clase)")
            else:
                h_str_fin = datetime.strptime(f"{int(h_fin_pasajero)}:00", "%H:%M").strftime("%I:%M %p")
                recoger_list.append(f"🟢 SÍ ({h_str_fin})")
                
    df_total['Llevar (🚗)'] = llevar_list
    df_total['Recoger (🚙)'] = recoger_list
    return df_total

# 3. Formulario Lateral
with st.sidebar:
    st.header("➕ Agregar Actividad")
    with st.form("form_nueva_actividad"):
        nuevo_integrante = st.selectbox("Integrante", ["Brahiam", "Marcela", "Hijo 1", "Hijo 2", "Familia"])
        nuevo_dia = st.selectbox("Día", ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"])
        nueva_actividad = st.text_input("Actividad / Materia")
        nuevo_lugar = st.text_input("Aula / Sede")
        
        h_inicio_val = st.number_input("Hora Inicio (24h, ej: 14 p.m.)", min_value=0.0, max_value=23.0, value=8.0, step=0.5)
        h_fin_val = st.number_input("Hora Fin (24h, ej: 16 p.m.)", min_value=0.5, max_value=24.0, value=10.0, step=0.5)
        
        btn_guardar = st.form_submit_button("Guardar Actividad")
        
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
            st.success(f"¡Guardado para {nuevo_integrante}!")

# Procesar datos
df_base = pd.DataFrame(st.session_state.agenda)
df_procesado = calcular_transporte_automatico(df_base)

# Filtros visuales
col1, col2, col3 = st.columns(3)
with col1:
    integrantes_disponibles = list(set([x["Integrante"] for x in st.session_state.agenda]))
    filtro_persona = st.selectbox("👤 Integrante:", ["Todos"] + integrantes_disponibles)
with col2:
    filtro_dia = st.selectbox("📅 Día de la semana:", ["Todos", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"])
with col3:
    tipo_vista = st.selectbox("🎨 Estilo de Visualización:", ["🎴 Tarjetas por Día (Recomendado)", "📊 Cronograma de Barras (Plotly)", "📋 Tabla Detallada"])

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
    m2.metric("🌴 Tiempo Libre Estimado (Lun-Vie 16h/día)", f"{libres:.1f} hrs")

# 4. RENDERIZADO DE VISTAS CON DISEÑO Y COLORES

if tipo_vista == "🎴 Tarjetas por Día (Recomendado)":
    st.subheader("📆 Tarjetero Semanal por Integrante")
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"] if filtro_dia == "Todos" else [filtro_dia]
    cols = st.columns(len(dias_semana))
    
    for i, dia in enumerate(dias_semana):
        with cols[i if len(dias_semana) > 1 else 0]:
            st.markdown(f"<h4 style='text-align: center; background-color: #1e1e1e; padding: 8px; border-radius: 8px; color: white;'>{dia}</h4>", unsafe_allow_html=True)
            df_day = df_view[df_view["Día"] == dia]
            if df_day.empty:
                st.caption("🟢 Libre")
            else:
                for _, row in df_day.iterrows():
                    # Definición de colores distintivos
                    if row['Integrante'] == 'Marcela':
                        bg_color = "#1e3a8a" # Azul oscuro
                        border_color = "#3b82f6" # Azul brillante
                    elif row['Integrante'] == 'Brahiam':
                        bg_color = "#831843" # Rojo / Rosado oscuro
                        border_color = "#ec4899" # Rosa brillante
                    else:
                        bg_color = "#064e3b" # Verde oscuro
                        border_color = "#10b981" # Verde brillante
                    
                    st.markdown(f"""
                    <div style="background-color: {bg_color}; border: 2px solid {border_color}; border-radius: 12px; padding: 12px; margin-bottom: 12px; color: white; box-shadow: 2px 2px 8px rgba(0,0,0,0.3);">
                        <div style="font-size: 14px; font-weight: bold; color: #f3f4f6;">⏰ {row['Horario']}</div>
                        <div style="font-size: 16px; font-weight: bold; margin-top: 4px;">👤 {row['Integrante']}</div>
                        <div style="font-size: 14px; margin-top: 4px;">📖 <em>{row['Actividad']}</em></div>
                        <div style="font-size: 12px; margin-top: 4px; color: #d1d5db;">📍 {row['Lugar / Aula']}</div>
                        <hr style="margin: 8px 0; border-color: {border_color}; opacity: 0.5;">
                        <div style="font-size: 11px;">🚗 <strong>Llevar:</strong> {row['Llevar (🚗)']}</div>
                        <div style="font-size: 11px;">🚙 <strong>Recoger:</strong> {row['Recoger (🚙)']}</div>
                    </div>
                    """, unsafe_allow_html=True)

elif tipo_vista == "📊 Cronograma de Barras (Plotly)":
    st.subheader("📊 Cronograma Visual (Plotly)")
    if not df_view.empty:
        fig = px.timeline(
            df_view, 
            x_start="Inicio_dt", 
            x_end="Fin_dt", 
            y="Día", 
            color="Integrante",
            hover_data=["Actividad", "Lugar / Aula", "Horario", "Llevar (🚗)", "Recoger (🚙)"],
            title="Distribución del Tiempo",
            color_discrete_map={"Brahiam": "#ec4899", "Marcela": "#3b82f6", "Hijo 1": "#10b981"}
        )
        fig.update_yaxes(autorange="reversed")
        st.plotly_chart(fig, use_container_width=True)

elif tipo_vista == "📋 Tabla Detallada":
    st.subheader("📋 Vista en Tabla")
    def colorear_filas(val):
        if "Marcela" in str(val):
            return 'background-color: #d0e1fd; color: #082a63; font-weight: bold;'
        elif "Brahiam" in str(val):
            return 'background-color: #fdd0d0; color: #630808; font-weight: bold;'
        elif "Hijo" in str(val):
            return 'background-color: #d0fdd7; color: #086317; font-weight: bold;'
        return ''
        
    df_tabla = df_view[["Día", "Integrante", "Horario", "Actividad", "Lugar / Aula", "Llevar (🚗)", "Recoger (🚙)"]]
    st.dataframe(df_tabla.style.map(colorear_filas, subset=['Integrante']), use_container_width=True, hide_index=True)
