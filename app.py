import streamlit as st
import pandas as pd
from datetime import datetime
from zoneinfo import ZoneInfo  # Nativo de Python (Sin requerir librerías externas)

# Configuración de la página
st.set_page_config(page_title="Agenda Familiar Brahiam & Marcela", page_icon="📅", layout="wide")

# 1. RELOJ Y FECHA EN TIEMPO REAL
ahora = datetime.now(ZoneInfo("America/Bogota"))
dias_espanol = {"Monday": "Lunes", "Tuesday": "Martes", "Wednesday": "Miércoles", "Thursday": "Jueves", "Friday": "Viernes", "Saturday": "Sábado", "Sunday": "Domingo"}
dia_hoy_nombre = dias_espanol.get(ahora.strftime('%A'), ahora.strftime('%A'))
fecha_actual_str = f"🕒 **Hoy es:** {dia_hoy_nombre}, {ahora.strftime('%d/%m/%Y')} — **Hora:** {ahora.strftime('%I:%M %p')}"

# Banner de Encabezado
st.title("⚡ Centro de Control & Agenda Familiar")
st.info(fecha_actual_str)

# 2. Cargar credenciales desde Secrets si existen
secret_token = st.secrets.get("TELEGRAM_TOKEN", "")
secret_id_brahiam = st.secrets.get("CHAT_ID_BRAHIAM", "")
secret_id_marcela = st.secrets.get("CHAT_ID_MARCELA", "")

# 3. Base de datos inicial en session_state (Protegidas)
if 'agenda' not in st.session_state:
    st.session_state.agenda = [
        # Lunes
        {"id": 1, "tipo": "fija", "Día": "Lunes", "Integrante": "Marcela", "Hora_Inicio_Num": 12.0, "Hora_Fin_Num": 16.0, "Hora_Inicio": "2026-08-03 12:00", "Hora_Fin": "2026-08-03 16:00", "Horario": "12:00 PM - 04:00 PM", "Actividad": "Seminario de Investigación / Empatía", "Lugar / Aula": "Aula 14-201 / 6-504"},
        {"id": 2, "tipo": "fija", "Día": "Lunes", "Integrante": "Brahiam", "Hora_Inicio_Num": 18.0, "Hora_Fin_Num": 22.0, "Hora_Inicio": "2026-08-03 18:00", "Hora_Fin": "2026-08-03 22:00", "Horario": "06:00 PM - 10:00 PM", "Actividad": "Estadística General", "Lugar / Aula": "Colegio Alcaldía-5 (BELÉN)"},
        
        # Martes
        {"id": 3, "tipo": "fija", "Día": "Martes", "Integrante": "Brahiam", "Hora_Inicio_Num": 18.0, "Hora_Fin_Num": 20.0, "Hora_Inicio": "2026-08-04 18:00", "Hora_Fin": "2026-08-04 20:00", "Horario": "06:00 PM - 08:00 PM", "Actividad": "Física de Campos y Lab.", "Lugar / Aula": "Aula M-106 (FRATERNIDAD)"},
        {"id": 4, "tipo": "fija", "Día": "Martes", "Integrante": "Brahiam", "Hora_Inicio_Num": 20.0, "Hora_Fin_Num": 22.0, "Hora_Inicio": "2026-08-04 20:00", "Hora_Fin": "2026-08-04 22:00", "Horario": "08:00 PM - 10:00 PM", "Actividad": "Cálculo de Varias Var.", "Lugar / Aula": "Aula Cas-306 (CASTILLA)"},

        # Miércoles
        {"id": 5, "tipo": "fija", "Día": "Miércoles", "Integrante": "Marcela", "Hora_Inicio_Num": 6.0, "Hora_Fin_Num": 14.0, "Hora_Inicio": "2026-08-05 06:00", "Hora_Fin": "2026-08-05 14:00", "Horario": "06:00 AM - 02:00 PM", "Actividad": "Taller de Diseño / Higiene", "Lugar / Aula": "Aula 14-201 / 13-304"},
        {"id": 6, "tipo": "fija", "Día": "Miércoles", "Integrante": "Brahiam", "Hora_Inicio_Num": 14.0, "Hora_Fin_Num": 16.0, "Hora_Inicio": "2026-08-05 14:00", "Hora_Fin": "2026-08-05 16:00", "Horario": "02:00 PM - 04:00 PM", "Actividad": "Electrónica Digital", "Lugar / Aula": "Aula C-204 (ROBLEDO)"},
        {"id": 7, "tipo": "fija", "Día": "Miércoles", "Integrante": "Brahiam", "Hora_Inicio_Num": 18.0, "Hora_Fin_Num": 20.0, "Hora_Inicio": "2026-08-05 18:00", "Hora_Fin": "2026-08-05 20:00", "Horario": "06:00 PM - 08:00 PM", "Actividad": "Física de Campos y Lab.", "Lugar / Aula": "Aula M-207 (FRATERNIDAD)"},

        # Jueves
        {"id": 8, "tipo": "fija", "Día": "Jueves", "Integrante": "Brahiam", "Hora_Inicio_Num": 20.0, "Hora_Fin_Num": 22.0, "Hora_Inicio": "2026-08-06 20:00", "Hora_Fin": "2026-08-06 22:00", "Horario": "08:00 PM - 10:00 PM", "Actividad": "Cálculo de Varias Var.", "Lugar / Aula": "Aula Cas-306 (CASTILLA)"},

        # Viernes
        {"id": 9, "tipo": "fija", "Día": "Viernes", "Integrante": "Marcela", "Hora_Inicio_Num": 10.0, "Hora_Fin_Num": 14.0, "Hora_Inicio": "2026-08-07 10:00", "Hora_Fin": "2026-08-07 14:00", "Horario": "10:00 AM - 02:00 PM", "Actividad": "Seminario Ética / Calidad", "Lugar / Aula": "Aula 13-303 / 8-502"},
        {"id": 10, "tipo": "fija", "Día": "Viernes", "Integrante": "Brahiam", "Hora_Inicio_Num": 14.0, "Hora_Fin_Num": 16.0, "Hora_Inicio": "2026-08-07 14:00", "Hora_Fin": "2026-08-07 16:00", "Horario": "02:00 PM - 04:00 PM", "Actividad": "Electrónica Digital", "Lugar / Aula": "Aula G-307 (ROBLEDO)"},
        {"id": 11, "tipo": "fija", "Día": "Viernes", "Integrante": "Brahiam", "Hora_Inicio_Num": 18.0, "Hora_Fin_Num": 20.0, "Hora_Inicio": "2026-08-07 18:00", "Hora_Fin": "2026-08-07 20:00", "Horario": "06:00 PM - 08:00 PM", "Actividad": "Física de Campos y Lab.", "Lugar / Aula": "Aula M-207 (FRATERNIDAD)"}
    ]

# 4. MOTOR DE CÁLCULO DE TRANSPORTE AUTOMÁTICO
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

# 5. PANEL LATERAL: AGREGAR Y ELIMINAR ACTIVIDADES CREADAS
with st.sidebar:
    st.header("➕ Agregar Actividad")
    with st.form("form_nueva_actividad"):
        nuevo_integrante = st.selectbox("Integrante", ["Brahiam", "Marcela", "Hijo 1", "Hijo 2", "Familia"])
        nuevo_dia = st.selectbox("Día", ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"])
        nueva_actividad = st.text_input("Actividad / Tarea")
        nuevo_lugar = st.text_input("Aula / Sede")
        
        h_inicio_val = st.number_input("Hora Inicio (24h, ej: 14 para 2pm)", min_value=0.0, max_value=23.0, value=8.0, step=0.5)
        h_fin_val = st.number_input("Hora Fin (24h, ej: 16 para 4pm)", min_value=0.5, max_value=24.0, value=10.0, step=0.5)
        
        btn_guardar = st.form_submit_button("Guardar Actividad")
        
        if btn_guardar and nueva_actividad:
            dias_dict = {"Lunes": "2026-08-03", "Martes": "2026-08-04", "Miércoles": "2026-08-05", "Jueves": "2026-08-06", "Viernes": "2026-08-07", "Sábado": "2026-08-08", "Domingo": "2026-08-09"}
            fecha_str = dias_dict.get(nuevo_dia, "2026-08-03")
            
            h_in_dt = datetime.strptime(f"{int(h_inicio_val):02d}:{int((h_inicio_val%1)*60):02d}", "%H:%M")
            h_fi_dt = datetime.strptime(f"{int(h_fin_val):02d}:{int((h_fin_val%1)*60):02d}", "%H:%M")
            
            nuevo_id = max([x.get("id", 0) for x in st.session_state.agenda], default=0) + 1
            
            st.session_state.agenda.append({
                "id": nuevo_id,
                "tipo": "dinamica",
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

    st.markdown("---")
    st.header("🗑️ Gestionar Actividades Creadas")
    
    actividades_dinamicas = [x for x in st.session_state.agenda if x.get("tipo") == "dinamica"]
    
    if actividades_dinamicas:
        opciones_eliminar = {f"{item['Día']} - {item['Integrante']}: {item['Actividad']} ({item['Horario']})": item.get('id') for item in actividades_dinamicas}
        seleccion_borrar = st.selectbox("Selecciona la actividad personalizada a borrar:", list(opciones_eliminar.keys()))
        
        if st.button("❌ Eliminar Actividad Seleccionada"):
            id_borrar = opciones_eliminar[seleccion_borrar]
            st.session_state.agenda = [x for x in st.session_state.agenda if x.get('id') != id_borrar]
            st.success("Actividad eliminada con éxito.")
            st.rerun()
    else:
        st.caption("🔒 *Las actividades fijas del código están protegidas. Solo aparecerán aquí para borrar las actividades personalizadas que agregues desde la app.*")

# Procesar datos
df_base = pd.DataFrame(st.session_state.agenda)
df_procesado = calcular_transporte_automatico(df_base) if not df_base.empty else df_base

# Filtros visuales
col1, col2, col3 = st.columns(3)
with col1:
    integrantes_disponibles = list(set([x["Integrante"] for x in st.session_state.agenda])) if not df_base.empty else []
    filtro_persona = st.selectbox("👤 Integrante:", ["Todos"] + integrantes_disponibles)
with col2:
    filtro_dia = st.selectbox("📅 Día de la semana:", ["Todos", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"], index=0)
with col3:
    tipo_vista = st.selectbox("🎨 Estilo de Visualización:", ["📱 Tarjetas Modernas (Bordes & Badges)", "📋 Tabla Detallada"])

# Aplicar filtros
df_view = df_procesado.copy() if not df_procesado.empty else df_procesado
if not df_view.empty:
    if filtro_persona != "Todos":
        df_view = df_view[df_view["Integrante"] == filtro_persona]
    if filtro_dia != "Todos":
        df_view = df_view[df_view["Día"] == filtro_dia]

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

# 6. RENDERIZADO DE VISTAS CON DISEÑO MEJORADO
if tipo_vista == "📱 Tarjetas Modernas (Bordes & Badges)":
    st.subheader("📆 Tarjetero Semanal Interactivo")
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"] if filtro_dia == "Todos" else [filtro_dia]
    cols = st.columns(len(dias_semana))
    
    for i, dia in enumerate(dias_semana):
        with cols[i if len(dias_semana) > 1 else 0]:
            borde_dia = "border: 2px solid #f59e0b;" if dia == dia_hoy_nombre else "border: 1px solid #334155;"
            st.markdown(f"<div style='text-align: center; background: #1e293b; padding: 10px; border-radius: 12px; font-weight: bold; color: #f8fafc; margin-bottom: 12px; {borde_dia}'>{dia} {'⭐' if dia == dia_hoy_nombre else ''}</div>", unsafe_allow_html=True)
            
            df_day = df_view[df_view["Día"] == dia] if not df_view.empty else pd.DataFrame()
            if df_day.empty:
                st.caption("🟢 Día Libre")
            else:
                for _, row in df_day.iterrows():
                    # CONFIGURACIÓN DE COLORES BASADA EN EL ESTILO DE LA HORA
                    if row['Integrante'] == 'Marcela':
                        card_bg = "background: linear-gradient(135deg, #1e3a5f, #1e40af);"
                        border_color = "#93c5fd"
                        badge_bg = "rgba(147, 197, 253, 0.2)"
                    elif row['Integrante'] == 'Brahiam':
                        card_bg = "background: linear-gradient(135deg, #4c1d24, #9f1239);"
                        border_color = "#fca5a5"
                        badge_bg = "rgba(252, 165, 165, 0.2)"
                    else:
                        card_bg = "background: linear-gradient(135deg, #064e3b, #047857);"
                        border_color = "#6ee7b7"
                        badge_bg = "rgba(110, 231, 183, 0.2)"
                    
                    st.markdown(f"""
                    <div style="{card_bg} border: 1.5px solid {border_color}; border-radius: 16px; padding: 14px; margin-bottom: 14px; color: white; box-shadow: 0 4px 14px rgba(0,0,0,0.3);">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <span style="font-size: 12px; font-weight: 700; background: {badge_bg}; border: 1px solid {border_color}; padding: 4px 10px; border-radius: 20px; color: {border_color};">⏰ {row['Horario']}</span>
                            <span style="font-size: 12px; font-weight: bold; opacity: 0.95;">👤 {row['Integrante']}</span>
                        </div>
                        <div style="font-size: 15px; font-weight: 700; margin-top: 10px; line-height: 1.3;">{row['Actividad']}</div>
                        <div style="font-size: 12px; margin-top: 6px; opacity: 0.85;">📍 {row['Lugar / Aula']}</div>
                        <div style="margin-top: 10px; padding-top: 8px; border-top: 1px solid rgba(255,255,255,0.2); font-size: 11px;">
                            <div>🚗 <strong>Llevar:</strong> {row['Llevar (🚗)']}</div>
                            <div style="margin-top: 2px;">🚙 <strong>Recoger:</strong> {row['Recoger (🚙)']}</div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

elif tipo_vista == "📋 Tabla Detallada":
    st.subheader("📋 Vista en Tabla Detallada")
    if not df_view.empty:
        def colorear_filas_suaves(val):
            if "Marcela" in str(val):
                return 'background-color: #1e3a5f; color: #bfdbfe; font-weight: bold;'
            elif "Brahiam" in str(val):
                return 'background-color: #4c1d24; color: #fecaca; font-weight: bold;'
            elif "Hijo" in str(val):
                return 'background-color: #064e3b; color: #a7f3d0; font-weight: bold;'
            return ''
            
        df_tabla = df_view[["Día", "Integrante", "Horario", "Actividad", "Lugar / Aula", "Llevar (🚗)", "Recoger (🚙)"]]
        st.dataframe(df_tabla.style.map(colorear_filas_suaves, subset=['Integrante']), use_container_width=True, hide_index=True)
    else:
        st.info("No hay actividades registradas.")

# 7. MÓDULO DE RECORDATORIOS INDIVIDUALES POR TELEGRAM
st.markdown("---")
st.subheader("🔔 Recordatorios Automáticos Individuales")

with st.form("form_telegram_individual"):
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        api_token = st.text_input("🤖 Telegram Bot Token:", value=secret_token, type="password")
    with col_b:
        chat_id_brahiam = st.text_input("💬 Chat ID de Brahiam:", value=secret_id_brahiam)
    with col_c:
        chat_id_marcela = st.text_input("💬 Chat ID de Marcela:", value=secret_id_marcela)
        
    btn_telegram = st.form_submit_button("🔔 Guardar y Probar Alertas")
    
    if btn_telegram:
        if api_token and (chat_id_brahiam or chat_id_marcela):
            st.session_state['telegram_token'] = api_token
            st.session_state['chat_id_brahiam'] = chat_id_brahiam
            st.session_state['chat_id_marcela'] = chat_id_marcela
            st.success("¡Excelente! Las alertas quedan configuradas sin conflictos.")
        else:
            st.error("Ingresa el Bot Token y al menos un Chat ID.")
