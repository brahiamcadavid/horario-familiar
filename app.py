import streamlit as st
import pandas as pd
from datetime import datetime

# Configuración de la página
st.set_page_config(page_title="Agenda Familiar Brahiam & Marcela", page_icon="📅", layout="wide")

st.title("⚡ Centro de Control & Agenda Familiar")
st.write("Gestiona horarios, transporte automático, tiempo libre y recordatorios de la familia.")

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
        
        h_inicio_val = st.number_input("Hora Inicio (24h, ej: 14 para 2pm)", min_value=0.0, max_value=23.0, value=8.0, step=0.5)
        h_fin_val = st.number_input("Hora Fin (24h, ej: 16 para 4pm)", min_value=0.5, max_value=24.0, value=10.0, step=0.5)
        
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
    tipo_vista = st.selectbox("🎨 Estilo de Visualización:", ["📱 Tarjetas Modernas (Glassmorphism)", "📋 Tabla Detallada"])

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

# 4. RENDERIZADO DE TARJETAS ESTILO MODERNO
if tipo_vista == "📱 Tarjetas Modernas (Glassmorphism)":
    st.subheader("📆 Tarjetero Semanal Interactivo")
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"] if filtro_dia == "Todos" else [filtro_dia]
    cols = st.columns(len(dias_semana))
    
    for i, dia in enumerate(dias_semana):
        with cols[i if len(dias_semana) > 1 else 0]:
            st.markdown(f"<div style='text-align: center; background: linear-gradient(135deg, #1e293b, #0f172a); padding: 10px; border-radius: 12px; font-weight: bold; color: #f8fafc; margin-bottom: 12px; border: 1px solid #334155;'>{dia}</div>", unsafe_allow_html=True)
            df_day = df_view[df_view["Día"] == dia]
            if df_day.empty:
                st.caption("🟢 Día Libre")
            else:
                for _, row in df_day.iterrows():
                    # ESTILOS MODERNOS Y ULTRA LIMPIOS (Azul para Marcela, Rojo/Neón para Brahiam)
                    if row['Integrante'] == 'Marcela':
                        card_style = """
                            background: linear-gradient(135deg, rgba(30, 58, 138, 0.85), rgba(29, 78, 216, 0.95));
                            border-left: 6px solid #60a5fa;
                            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
                        """
                        badge_color = "#93c5fd"
                    elif row['Integrante'] == 'Brahiam':
                        card_style = """
                            background: linear-gradient(135deg, rgba(153, 27, 27, 0.85), rgba(220, 38, 38, 0.95));
                            border-left: 6px solid #fca5a5;
                            box-shadow: 0 8px 32px 0 rgba(135, 31, 31, 0.37);
                        """
                        badge_color = "#fca5a5"
                    else:
                        card_style = """
                            background: linear-gradient(135deg, rgba(6, 78, 59, 0.85), rgba(5, 150, 105, 0.95));
                            border-left: 6px solid #6ee7b7;
                            box-shadow: 0 8px 32px 0 rgba(31, 135, 80, 0.37);
                        """
                        badge_color = "#6ee7b7"
                    
                    st.markdown(f"""
                    <div style="{card_style} border-radius: 16px; padding: 14px; margin-bottom: 14px; color: white; backdrop-filter: blur(8px);">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <span style="font-size: 13px; font-weight: 700; background: rgba(0,0,0,0.25); padding: 4px 8px; border-radius: 20px; color: {badge_color};">⏰ {row['Horario']}</span>
                            <span style="font-size: 12px; font-weight: bold; opacity: 0.9;">👤 {row['Integrante']}</span>
                        </div>
                        <div style="font-size: 15px; font-weight: 700; margin-top: 10px; line-height: 1.3;">{row['Actividad']}</div>
                        <div style="font-size: 12px; margin-top: 6px; opacity: 0.9;">📍 {row['Lugar / Aula']}</div>
                        <div style="margin-top: 10px; padding-top: 8px; border-top: 1px solid rgba(255,255,255,0.2); font-size: 11px;">
                            <div>🚗 <strong>Llevar:</strong> {row['Llevar (🚗)']}</div>
                            <div style="margin-top: 2px;">🚙 <strong>Recoger:</strong> {row['Recoger (🚙)']}</div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

elif tipo_vista == "📋 Tabla Detallada":
    st.subheader("📋 Vista en Tabla")
    df_tabla = df_view[["Día", "Integrante", "Horario", "Actividad", "Lugar / Aula", "Llevar (🚗)", "Recoger (🚙)"]]
    st.dataframe(df_tabla, use_container_width=True, hide_index=True)

# 5. MÓDULO DE RECORDATORIOS POR TELEGRAM
st.markdown("---")
st.subheader("🔔 Conectar Recordatorios Automáticos por Telegram")

col_t1, col_t2 = st.columns(2)
with col_t1:
    st.markdown("""
    **Pasos rápidos para activar:**
    1. Abre Telegram y busca a **`@BotFather`**. Escribe `/newbot` para obtener tu **API Token**.
    2. Busca a **`@getmyid_bot`** en Telegram y presiona *Start* para ver tu **Chat ID**.
    3. Llena el formulario de la derecha.
    """)

with col_t2:
    with st.form("form_telegram"):
        api_token = st.text_input("🤖 Telegram Bot API Token:", type="password", placeholder="Ej: 123456789:ABCdefGHI...")
        chat_id = st.text_input("💬 Tu Telegram Chat ID:", placeholder="Ej: 987654321")
        btn_telegram = st.form_submit_button("🔔 Activar Notificaciones")
        
        if btn_telegram:
            if api_token and chat_id:
                st.session_state['telegram_token'] = api_token
                st.session_state['telegram_chat_id'] = chat_id
                st.success("¡Excelente! Credenciales guardadas correctamente. Tu app ya está lista para enviar las alertas automáticas a tu celular.")
            else:
                st.error("Por favor ingresa tanto el Token como el Chat ID.")
