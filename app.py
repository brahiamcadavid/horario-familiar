from datetime import datetime
from zoneinfo import ZoneInfo
import pandas as pd
import requests
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Agenda Familiar Brahiam & Marcela", page_icon="📅", layout="wide"
)

# 1. RELOJ Y FECHA EN TIEMPO REAL
ahora = datetime.now(ZoneInfo("America/Bogota"))
dias_espanol = {
    "Monday": "Lunes",
    "Tuesday": "Martes",
    "Wednesday": "Miércoles",
    "Thursday": "Jueves",
    "Friday": "Viernes",
    "Saturday": "Sábado",
    "Sunday": "Domingo",
}
dia_hoy_nombre = dias_espanol.get(ahora.strftime("%A"), ahora.strftime("%A"))
fecha_actual_str = f"🕒 **Hoy es:** {dia_hoy_nombre}, {ahora.strftime('%d/%m/%Y')} — **Hora:** {ahora.strftime('%I:%M %p')}"

# Banner de Encabezado
st.title("⚡ Centro de Control & Agenda Familiar")
st.info(fecha_actual_str)

# 2. Cargar credenciales desde Secrets si existen
secret_token = st.secrets.get("TELEGRAM_TOKEN", "")
secret_id_brahiam = st.secrets.get("CHAT_ID_BRAHIAM", "")
secret_id_marcela = st.secrets.get("CHAT_ID_MARCELA", "")


# Función para enviar mensajes vía Telegram API
def enviar_mensaje_telegram(token, chat_id, mensaje):
  url = f"https://api.telegram.org/bot{token}/sendMessage"
  payload = {"chat_id": chat_id, "text": mensaje, "parse_mode": "Markdown"}
  try:
    response = requests.post(url, json=payload, timeout=5)
    return response.status_code == 200
  except Exception as e:
    return False


# 3. BASE DE DATOS COMPLETA EN SESSION_STATE
if "agenda" not in st.session_state:
  st.session_state.agenda = [
      # --- BRAHIAM & MARCELA ---
      {
          "id": 1,
          "tipo": "fija",
          "Día": "Lunes",
          "Integrante": "Marcela",
          "Hora_Inicio_Num": 12.0,
          "Hora_Fin_Num": 16.0,
          "Hora_Inicio": "2026-08-03 12:00",
          "Hora_Fin": "2026-08-03 16:00",
          "Horario": "12:00 PM - 04:00 PM",
          "Actividad": "Seminario de Investigación / Empatía",
          "Lugar / Aula": "Aula 14-201 / 6-504",
      },
      {
          "id": 2,
          "tipo": "fija",
          "Día": "Lunes",
          "Integrante": "Brahiam",
          "Hora_Inicio_Num": 18.0,
          "Hora_Fin_Num": 22.0,
          "Hora_Inicio": "2026-08-03 18:00",
          "Hora_Fin": "2026-08-03 22:00",
          "Horario": "06:00 PM - 10:00 PM",
          "Actividad": "Estadística General",
          "Lugar / Aula": "Colegio Alcaldía-5 (BELÉN)",
      },
      {
          "id": 3,
          "tipo": "fija",
          "Día": "Martes",
          "Integrante": "Brahiam",
          "Hora_Inicio_Num": 18.0,
          "Hora_Fin_Num": 20.0,
          "Hora_Inicio": "2026-08-04 18:00",
          "Hora_Fin": "2026-08-04 20:00",
          "Horario": "06:00 PM - 08:00 PM",
          "Actividad": "Física de Campos y Lab.",
          "Lugar / Aula": "Aula M-106 (FRATERNIDAD)",
      },
      {
          "id": 4,
          "tipo": "fija",
          "Día": "Martes",
          "Integrante": "Brahiam",
          "Hora_Inicio_Num": 20.0,
          "Hora_Fin_Num": 22.0,
          "Hora_Inicio": "2026-08-04 20:00",
          "Hora_Fin": "2026-08-04 22:00",
          "Horario": "08:00 PM - 10:00 PM",
          "Actividad": "Cálculo de Varias Var.",
          "Lugar / Aula": "Aula Cas-306 (CASTILLA)",
      },
      {
          "id": 5,
          "tipo": "fija",
          "Día": "Miércoles",
          "Integrante": "Marcela",
          "Hora_Inicio_Num": 6.0,
          "Hora_Fin_Num": 14.0,
          "Hora_Inicio": "2026-08-05 06:00",
          "Hora_Fin": "2026-08-05 14:00",
          "Horario": "06:00 AM - 02:00 PM",
          "Actividad": "Taller de Diseño / Higiene",
          "Lugar / Aula": "Aula 14-201 / 13-304",
      },
      {
          "id": 6,
          "tipo": "fija",
          "Día": "Miércoles",
          "Integrante": "Brahiam",
          "Hora_Inicio_Num": 14.0,
          "Hora_Fin_Num": 16.0,
          "Hora_Inicio": "2026-08-05 14:00",
          "Hora_Fin": "2026-08-05 16:00",
          "Horario": "02:00 PM - 04:00 PM",
          "Actividad": "Electrónica Digital",
          "Lugar / Aula": "Aula C-204 (ROBLEDO)",
      },
      {
          "id": 7,
          "tipo": "fija",
          "Día": "Miércoles",
          "Integrante": "Brahiam",
          "Hora_Inicio_Num": 18.0,
          "Hora_Fin_Num": 20.0,
          "Hora_Inicio": "2026-08-05 18:00",
          "Hora_Fin": "2026-08-05 20:00",
          "Horario": "06:00 PM - 08:00 PM",
          "Actividad": "Física de Campos y Lab.",
          "Lugar / Aula": "Aula M-207 (FRATERNIDAD)",
      },
      {
          "id": 8,
          "tipo": "fija",
          "Día": "Jueves",
          "Integrante": "Brahiam",
          "Hora_Inicio_Num": 20.0,
          "Hora_Fin_Num": 22.0,
          "Hora_Inicio": "2026-08-06 20:00",
          "Hora_Fin": "2026-08-06 22:00",
          "Horario": "08:00 PM - 10:00 PM",
          "Actividad": "Cálculo de Varias Var.",
          "Lugar / Aula": "Aula Cas-306 (CASTILLA)",
      },
      {
          "id": 9,
          "tipo": "fija",
          "Día": "Viernes",
          "Integrante": "Marcela",
          "Hora_Inicio_Num": 10.0,
          "Hora_Fin_Num": 14.0,
          "Hora_Inicio": "2026-08-07 10:00",
          "Hora_Fin": "2026-08-07 14:00",
          "Horario": "10:00 AM - 02:00 PM",
          "Actividad": "Seminario Ética / Calidad",
          "Lugar / Aula": "Aula 13-303 / 8-502",
      },
      {
          "id": 10,
          "tipo": "fija",
          "Día": "Viernes",
          "Integrante": "Brahiam",
          "Hora_Inicio_Num": 14.0,
          "Hora_Fin_Num": 16.0,
          "Hora_Inicio": "2026-08-07 14:00",
          "Hora_Fin": "2026-08-07 16:00",
          "Horario": "02:00 PM - 04:00 PM",
          "Actividad": "Electrónica Digital",
          "Lugar / Aula": "Aula G-307 (ROBLEDO)",
      },
      {
          "id": 11,
          "tipo": "fija",
          "Día": "Viernes",
          "Integrante": "Brahiam",
          "Hora_Inicio_Num": 18.0,
          "Hora_Fin_Num": 20.0,
          "Hora_Inicio": "2026-08-07 18:00",
          "Hora_Fin": "2026-08-07 20:00",
          "Horario": "06:00 PM - 08:00 PM",
          "Actividad": "Física de Campos y Lab.",
          "Lugar / Aula": "Aula M-207 (FRATERNIDAD)",
      },
      # --- ISAAC (SEXTO 2 - AULA 2) ---
      {
          "id": 12,
          "tipo": "fija",
          "Día": "Lunes",
          "Integrante": "Isaac",
          "Hora_Inicio_Num": 6.33,
          "Hora_Fin_Num": 8.16,
          "Hora_Inicio": "2026-08-03 06:20",
          "Hora_Fin": "2026-08-03 08:10",
          "Horario": "06:20 AM - 08:10 AM",
          "Actividad": "Tecnología S1",
          "Lugar / Aula": "Aula 2",
      },
      {
          "id": 13,
          "tipo": "fija",
          "Día": "Lunes",
          "Integrante": "Isaac",
          "Hora_Inicio_Num": 8.5,
          "Hora_Fin_Num": 10.33,
          "Hora_Inicio": "2026-08-03 08:30",
          "Hora_Fin": "2026-08-03 10:20",
          "Horario": "08:30 AM - 10:20 AM",
          "Actividad": "Español",
          "Lugar / Aula": "Aula 2",
      },
      {
          "id": 14,
          "tipo": "fija",
          "Día": "Lunes",
          "Integrante": "Isaac",
          "Hora_Inicio_Num": 10.5,
          "Hora_Fin_Num": 11.42,
          "Hora_Inicio": "2026-08-03 10:30",
          "Hora_Fin": "2026-08-03 11:25",
          "Horario": "10:30 AM - 11:25 AM",
          "Actividad": "Sociales",
          "Lugar / Aula": "Aula 2",
      },
      {
          "id": 15,
          "tipo": "fija",
          "Día": "Lunes",
          "Integrante": "Isaac",
          "Hora_Inicio_Num": 11.42,
          "Hora_Fin_Num": 12.33,
          "Hora_Inicio": "2026-08-03 11:25",
          "Hora_Fin": "2026-08-03 12:20",
          "Horario": "11:25 AM - 12:20 PM",
          "Actividad": "Matemáticas",
          "Lugar / Aula": "Aula 2",
      },
      {
          "id": 16,
          "tipo": "fija",
          "Día": "Martes",
          "Integrante": "Isaac",
          "Hora_Inicio_Num": 6.33,
          "Hora_Fin_Num": 6.83,
          "Hora_Inicio": "2026-08-04 06:20",
          "Hora_Fin": "2026-08-04 06:50",
          "Horario": "06:20 AM - 06:50 AM",
          "Actividad": "Orientación de Grupo",
          "Lugar / Aula": "Aula 2",
      },
      {
          "id": 17,
          "tipo": "fija",
          "Día": "Martes",
          "Integrante": "Isaac",
          "Hora_Inicio_Num": 6.83,
          "Hora_Fin_Num": 8.5,
          "Hora_Inicio": "2026-08-04 06:50",
          "Hora_Fin": "2026-08-04 08:30",
          "Horario": "06:50 AM - 08:30 AM",
          "Actividad": "Biología",
          "Lugar / Aula": "Aula 2",
      },
      {
          "id": 18,
          "tipo": "fija",
          "Día": "Martes",
          "Integrante": "Isaac",
          "Hora_Inicio_Num": 8.83,
          "Hora_Fin_Num": 10.5,
          "Hora_Inicio": "2026-08-04 08:50",
          "Hora_Fin": "2026-08-04 10:30",
          "Horario": "08:50 AM - 10:30 AM",
          "Actividad": "Español",
          "Lugar / Aula": "Aula 2",
      },
      {
          "id": 19,
          "tipo": "fija",
          "Día": "Martes",
          "Integrante": "Isaac",
          "Hora_Inicio_Num": 10.67,
          "Hora_Fin_Num": 12.33,
          "Hora_Inicio": "2026-08-04 10:40",
          "Hora_Fin": "2026-08-04 12:20",
          "Horario": "10:40 AM - 12:20 PM",
          "Actividad": "Ética",
          "Lugar / Aula": "Aula 2",
      },
      {
          "id": 20,
          "tipo": "fija",
          "Día": "Miércoles",
          "Integrante": "Isaac",
          "Hora_Inicio_Num": 6.33,
          "Hora_Fin_Num": 8.16,
          "Hora_Inicio": "2026-08-05 06:20",
          "Hora_Fin": "2026-08-05 08:10",
          "Horario": "06:20 AM - 08:10 AM",
          "Actividad": "Matemáticas",
          "Lugar / Aula": "Aula 2",
      },
      {
          "id": 21,
          "tipo": "fija",
          "Día": "Miércoles",
          "Integrante": "Isaac",
          "Hora_Inicio_Num": 8.5,
          "Hora_Fin_Num": 10.33,
          "Hora_Inicio": "2026-08-05 08:30",
          "Hora_Fin": "2026-08-05 10:20",
          "Horario": "08:30 AM - 10:20 AM",
          "Actividad": "Sociales",
          "Lugar / Aula": "Aula 2",
      },
      {
          "id": 22,
          "tipo": "fija",
          "Día": "Miércoles",
          "Integrante": "Isaac",
          "Hora_Inicio_Num": 10.5,
          "Hora_Fin_Num": 11.42,
          "Hora_Inicio": "2026-08-05 10:30",
          "Hora_Fin": "2026-08-05 11:25",
          "Horario": "10:30 AM - 11:25 AM",
          "Actividad": "Inglés",
          "Lugar / Aula": "Aula 2",
      },
      {
          "id": 23,
          "tipo": "fija",
          "Día": "Miércoles",
          "Integrante": "Isaac",
          "Hora_Inicio_Num": 11.42,
          "Hora_Fin_Num": 12.33,
          "Hora_Inicio": "2026-08-05 11:25",
          "Hora_Fin": "2026-08-05 12:20",
          "Horario": "11:25 AM - 12:20 PM",
          "Actividad": "Química",
          "Lugar / Aula": "Aula 2",
      },
      {
          "id": 24,
          "tipo": "fija",
          "Día": "Miércoles",
          "Integrante": "Isaac",
          "Hora_Inicio_Num": 13.0,
          "Hora_Fin_Num": 17.5,
          "Hora_Inicio": "2026-08-05 13:00",
          "Hora_Fin": "2026-08-05 17:30",
          "Horario": "01:00 PM - 05:30 PM",
          "Actividad": "Configuración de Robótica",
          "Lugar / Aula": "Sede / Aula Robótica",
      },
      {
          "id": 25,
          "tipo": "fija",
          "Día": "Jueves",
          "Integrante": "Isaac",
          "Hora_Inicio_Num": 6.33,
          "Hora_Fin_Num": 7.25,
          "Hora_Inicio": "2026-08-06 06:20",
          "Hora_Fin": "2026-08-06 07:15",
          "Horario": "06:20 AM - 07:15 AM",
          "Actividad": "Física",
          "Lugar / Aula": "Aula 2",
      },
      {
          "id": 26,
          "tipo": "fija",
          "Día": "Jueves",
          "Integrante": "Isaac",
          "Hora_Inicio_Num": 7.25,
          "Hora_Fin_Num": 8.16,
          "Hora_Inicio": "2026-08-06 07:15",
          "Hora_Fin": "2026-08-06 08:10",
          "Horario": "07:15 AM - 08:10 AM",
          "Actividad": "Artística",
          "Lugar / Aula": "Aula 2",
      },
      {
          "id": 27,
          "tipo": "fija",
          "Día": "Jueves",
          "Integrante": "Isaac",
          "Hora_Inicio_Num": 8.5,
          "Hora_Fin_Num": 10.33,
          "Hora_Inicio": "2026-08-06 08:30",
          "Hora_Fin": "2026-08-06 10:20",
          "Horario": "08:30 AM - 10:20 AM",
          "Actividad": "Inglés",
          "Lugar / Aula": "Aula 2",
      },
      {
          "id": 28,
          "tipo": "fija",
          "Día": "Jueves",
          "Integrante": "Isaac",
          "Hora_Inicio_Num": 10.5,
          "Hora_Fin_Num": 11.42,
          "Hora_Inicio": "2026-08-06 10:30",
          "Hora_Fin": "2026-08-06 11:25",
          "Horario": "10:30 AM - 11:25 AM",
          "Actividad": "Religión",
          "Lugar / Aula": "Aula 2",
      },
      {
          "id": 29,
          "tipo": "fija",
          "Día": "Jueves",
          "Integrante": "Isaac",
          "Hora_Inicio_Num": 11.42,
          "Hora_Fin_Num": 12.33,
          "Hora_Inicio": "2026-08-06 11:25",
          "Hora_Fin": "2026-08-06 12:20",
          "Horario": "11:25 AM - 12:20 PM",
          "Actividad": "Matemáticas",
          "Lugar / Aula": "Aula 2",
      },
      {
          "id": 30,
          "tipo": "fija",
          "Día": "Viernes",
          "Integrante": "Isaac",
          "Hora_Inicio_Num": 6.33,
          "Hora_Fin_Num": 7.08,
          "Hora_Inicio": "2026-08-07 06:20",
          "Hora_Fin": "2026-08-07 07:05",
          "Horario": "06:20 AM - 07:05 AM",
          "Actividad": "Matemáticas",
          "Lugar / Aula": "Aula 2",
      },
      {
          "id": 31,
          "tipo": "fija",
          "Día": "Viernes",
          "Integrante": "Isaac",
          "Hora_Inicio_Num": 7.08,
          "Hora_Fin_Num": 7.83,
          "Hora_Inicio": "2026-08-07 07:05",
          "Hora_Fin": "2026-08-07 07:50",
          "Horario": "07:05 AM - 07:50 AM",
          "Actividad": "Emprendimiento",
          "Lugar / Aula": "Aula 2",
      },
      {
          "id": 32,
          "tipo": "fija",
          "Día": "Viernes",
          "Integrante": "Isaac",
          "Hora_Inicio_Num": 8.16,
          "Hora_Fin_Num": 9.67,
          "Hora_Inicio": "2026-08-07 08:10",
          "Hora_Fin": "2026-08-07 09:40",
          "Horario": "08:10 AM - 09:40 AM",
          "Actividad": "Sociales",
          "Lugar / Aula": "Aula 2",
      },
      {
          "id": 33,
          "tipo": "fija",
          "Día": "Viernes",
          "Integrante": "Isaac",
          "Hora_Inicio_Num": 9.83,
          "Hora_Fin_Num": 11.33,
          "Hora_Inicio": "2026-08-07 09:50",
          "Hora_Fin": "2026-08-07 11:20",
          "Horario": "09:50 AM - 11:20 AM",
          "Actividad": "Ed. Física",
          "Lugar / Aula": "Aula 2",
      },
      # --- MATEO (DÉCIMO 2 - SISTEMAS 1) ---
      {
          "id": 34,
          "tipo": "fija",
          "Día": "Lunes",
          "Integrante": "Mateo",
          "Hora_Inicio_Num": 6.33,
          "Hora_Fin_Num": 8.16,
          "Hora_Inicio": "2026-08-03 06:20",
          "Hora_Fin": "2026-08-03 08:10",
          "Horario": "06:20 AM - 08:10 AM",
          "Actividad": "Español A2",
          "Lugar / Aula": "Sistemas 1",
      },
      {
          "id": 35,
          "tipo": "fija",
          "Día": "Lunes",
          "Integrante": "Mateo",
          "Hora_Inicio_Num": 8.5,
          "Hora_Fin_Num": 10.33,
          "Hora_Inicio": "2026-08-03 08:30",
          "Hora_Fin": "2026-08-03 10:20",
          "Horario": "08:30 AM - 10:20 AM",
          "Actividad": "Física",
          "Lugar / Aula": "Sistemas 1",
      },
      {
          "id": 36,
          "tipo": "fija",
          "Día": "Lunes",
          "Integrante": "Mateo",
          "Hora_Inicio_Num": 10.5,
          "Hora_Fin_Num": 11.42,
          "Hora_Inicio": "2026-08-03 10:30",
          "Hora_Fin": "2026-08-03 11:25",
          "Horario": "10:30 AM - 11:25 AM",
          "Actividad": "Biología",
          "Lugar / Aula": "Sistemas 1",
      },
      {
          "id": 37,
          "tipo": "fija",
          "Día": "Lunes",
          "Integrante": "Mateo",
          "Hora_Inicio_Num": 11.42,
          "Hora_Fin_Num": 12.33,
          "Hora_Inicio": "2026-08-03 11:25",
          "Hora_Fin": "2026-08-03 12:20",
          "Horario": "11:25 AM - 12:20 PM",
          "Actividad": "Química / Media T.",
          "Lugar / Aula": "Sistemas 1",
      },
      {
          "id": 38,
          "tipo": "fija",
          "Día": "Lunes",
          "Integrante": "Mateo",
          "Hora_Inicio_Num": 13.0,
          "Hora_Fin_Num": 16.5,
          "Hora_Inicio": "2026-08-03 13:00",
          "Hora_Fin": "2026-08-03 16:30",
          "Horario": "01:00 PM - 04:30 PM",
          "Actividad": "Media Técnica - Asistencia Administrativa",
          "Lugar / Aula": "Sistemas 1",
      },
      {
          "id": 39,
          "tipo": "fija",
          "Día": "Martes",
          "Integrante": "Mateo",
          "Hora_Inicio_Num": 6.33,
          "Hora_Fin_Num": 6.83,
          "Hora_Inicio": "2026-08-04 06:20",
          "Hora_Fin": "2026-08-04 06:50",
          "Horario": "06:20 AM - 06:50 AM",
          "Actividad": "Orientación de Grupo",
          "Lugar / Aula": "Sistemas 1",
      },
      {
          "id": 40,
          "tipo": "fija",
          "Día": "Martes",
          "Integrante": "Mateo",
          "Hora_Inicio_Num": 6.83,
          "Hora_Fin_Num": 8.5,
          "Hora_Inicio": "2026-08-04 06:50",
          "Hora_Fin": "2026-08-04 08:30",
          "Horario": "06:50 AM - 08:30 AM",
          "Actividad": "Matemáticas A3",
          "Lugar / Aula": "Sistemas 1",
      },
      {
          "id": 41,
          "tipo": "fija",
          "Día": "Martes",
          "Integrante": "Mateo",
          "Hora_Inicio_Num": 8.83,
          "Hora_Fin_Num": 9.67,
          "Hora_Inicio": "2026-08-04 08:50",
          "Hora_Fin": "2026-08-04 09:40",
          "Horario": "08:50 AM - 09:40 AM",
          "Actividad": "Religión",
          "Lugar / Aula": "Sistemas 1",
      },
      {
          "id": 42,
          "tipo": "fija",
          "Día": "Martes",
          "Integrante": "Mateo",
          "Hora_Inicio_Num": 9.67,
          "Hora_Fin_Num": 10.5,
          "Hora_Inicio": "2026-08-04 09:40",
          "Hora_Fin": "2026-08-04 10:30",
          "Horario": "09:40 AM - 10:30 AM",
          "Actividad": "Filosofía",
          "Lugar / Aula": "Sistemas 1",
      },
      {
          "id": 43,
          "tipo": "fija",
          "Día": "Martes",
          "Integrante": "Mateo",
          "Hora_Inicio_Num": 10.67,
          "Hora_Fin_Num": 12.33,
          "Hora_Inicio": "2026-08-04 10:40",
          "Hora_Fin": "2026-08-04 12:20",
          "Horario": "10:40 AM - 12:20 PM",
          "Actividad": "Inglés",
          "Lugar / Aula": "Sistemas 1",
      },
      {
          "id": 44,
          "tipo": "fija",
          "Día": "Miércoles",
          "Integrante": "Mateo",
          "Hora_Inicio_Num": 6.33,
          "Hora_Fin_Num": 7.25,
          "Hora_Inicio": "2026-08-05 06:20",
          "Hora_Fin": "2026-08-05 07:15",
          "Horario": "06:20 AM - 07:15 AM",
          "Actividad": "Ética",
          "Lugar / Aula": "Sistemas 1",
      },
      {
          "id": 45,
          "tipo": "fija",
          "Día": "Miércoles",
          "Integrante": "Mateo",
          "Hora_Inicio_Num": 7.25,
          "Hora_Fin_Num": 8.16,
          "Hora_Inicio": "2026-08-05 07:15",
          "Hora_Fin": "2026-08-05 08:10",
          "Horario": "07:15 AM - 08:10 AM",
          "Actividad": "Inglés",
          "Lugar / Aula": "Sistemas 1",
      },
      {
          "id": 46,
          "tipo": "fija",
          "Día": "Miércoles",
          "Integrante": "Mateo",
          "Hora_Inicio_Num": 8.5,
          "Hora_Fin_Num": 10.33,
          "Hora_Inicio": "2026-08-05 08:30",
          "Hora_Fin": "2026-08-05 10:20",
          "Horario": "08:30 AM - 10:20 AM",
          "Actividad": "Matemáticas A1",
          "Lugar / Aula": "Sistemas 1",
      },
      {
          "id": 47,
          "tipo": "fija",
          "Día": "Miércoles",
          "Integrante": "Mateo",
          "Hora_Inicio_Num": 10.5,
          "Hora_Fin_Num": 11.42,
          "Hora_Inicio": "2026-08-05 10:30",
          "Hora_Fin": "2026-08-05 11:25",
          "Horario": "10:30 AM - 11:25 AM",
          "Actividad": "Artística",
          "Lugar / Aula": "Sistemas 1",
      },
      {
          "id": 48,
          "tipo": "fija",
          "Día": "Miércoles",
          "Integrante": "Mateo",
          "Hora_Inicio_Num": 11.42,
          "Hora_Fin_Num": 12.33,
          "Hora_Inicio": "2026-08-05 11:25",
          "Hora_Fin": "2026-08-05 12:20",
          "Horario": "11:25 AM - 12:20 PM",
          "Actividad": "Sociales / Media T.",
          "Lugar / Aula": "Sistemas 1",
      },
      {
          "id": 49,
          "tipo": "fija",
          "Día": "Miércoles",
          "Integrante": "Mateo",
          "Hora_Inicio_Num": 13.0,
          "Hora_Fin_Num": 16.5,
          "Hora_Inicio": "2026-08-05 13:00",
          "Hora_Fin": "2026-08-05 16:30",
          "Horario": "01:00 PM - 04:30 PM",
          "Actividad": "Media Técnica - Asistencia Administrativa",
          "Lugar / Aula": "Sistemas 1",
      },
      {
          "id": 50,
          "tipo": "fija",
          "Día": "Jueves",
          "Integrante": "Mateo",
          "Hora_Inicio_Num": 6.33,
          "Hora_Fin_Num": 8.16,
          "Hora_Inicio": "2026-08-06 06:20",
          "Hora_Fin": "2026-08-06 08:10",
          "Horario": "06:20 AM - 08:10 AM",
          "Actividad": "Sociales",
          "Lugar / Aula": "Sistemas 1",
      },
      {
          "id": 51,
          "tipo": "fija",
          "Día": "Jueves",
          "Integrante": "Mateo",
          "Hora_Inicio_Num": 8.5,
          "Hora_Fin_Num": 10.33,
          "Hora_Inicio": "2026-08-06 08:30",
          "Hora_Fin": "2026-08-06 10:20",
          "Horario": "08:30 AM - 10:20 AM",
          "Actividad": "Ed. Física",
          "Lugar / Aula": "Sistemas 1",
      },
      {
          "id": 52,
          "tipo": "fija",
          "Día": "Jueves",
          "Integrante": "Mateo",
          "Hora_Inicio_Num": 10.5,
          "Hora_Fin_Num": 11.42,
          "Hora_Inicio": "2026-08-06 10:30",
          "Hora_Fin": "2026-08-06 11:25",
          "Horario": "10:30 AM - 11:25 AM",
          "Actividad": "Tecnología",
          "Lugar / Aula": "Sistemas 1",
      },
      {
          "id": 53,
          "tipo": "fija",
          "Día": "Jueves",
          "Integrante": "Mateo",
          "Hora_Inicio_Num": 11.42,
          "Hora_Fin_Num": 12.33,
          "Hora_Inicio": "2026-08-06 11:25",
          "Hora_Fin": "2026-08-06 12:20",
          "Horario": "11:25 AM - 12:20 PM",
          "Actividad": "Eco y Pol / MT SENA",
          "Lugar / Aula": "Sistemas 1",
      },
      {
          "id": 54,
          "tipo": "fija",
          "Día": "Jueves",
          "Integrante": "Mateo",
          "Hora_Inicio_Num": 13.0,
          "Hora_Fin_Num": 17.5,
          "Hora_Inicio": "2026-08-06 13:00",
          "Hora_Fin": "2026-08-06 17:30",
          "Horario": "01:00 PM - 05:30 PM",
          "Actividad": "Clases SENA",
          "Lugar / Aula": "SENA / Aula Asignada",
      },
      {
          "id": 55,
          "tipo": "fija",
          "Día": "Viernes",
          "Integrante": "Mateo",
          "Hora_Inicio_Num": 6.33,
          "Hora_Fin_Num": 7.83,
          "Hora_Inicio": "2026-08-07 06:20",
          "Hora_Fin": "2026-08-07 07:50",
          "Horario": "06:20 AM - 07:50 AM",
          "Actividad": "Español",
          "Lugar / Aula": "Sistemas 1",
      },
      {
          "id": 56,
          "tipo": "fija",
          "Día": "Viernes",
          "Integrante": "Mateo",
          "Hora_Inicio_Num": 8.16,
          "Hora_Fin_Num": 8.92,
          "Hora_Inicio": "2026-08-07 08:10",
          "Hora_Fin": "2026-08-07 08:55",
          "Horario": "08:10 AM - 08:55 AM",
          "Actividad": "Física",
          "Lugar / Aula": "Sistemas 1",
      },
      {
          "id": 57,
          "tipo": "fija",
          "Día": "Viernes",
          "Integrante": "Mateo",
          "Hora_Inicio_Num": 8.92,
          "Hora_Fin_Num": 9.67,
          "Hora_Inicio": "2026-08-07 08:55",
          "Hora_Fin": "2026-08-07 09:40",
          "Horario": "08:55 AM - 09:40 AM",
          "Actividad": "Emprendimiento",
          "Lugar / Aula": "Sistemas 1",
      },
      {
          "id": 58,
          "tipo": "fija",
          "Día": "Viernes",
          "Integrante": "Mateo",
          "Hora_Inicio_Num": 9.83,
          "Hora_Fin_Num": 11.33,
          "Hora_Inicio": "2026-08-07 09:50",
          "Hora_Fin": "2026-08-07 11:20",
          "Horario": "09:50 AM - 11:20 AM",
          "Actividad": "Química",
          "Lugar / Aula": "Sistemas 1",
      },
  ]


# 4. MOTOR DE CÁLCULO DE TRANSPORTE AUTOMÁTICO
def calcular_transporte_automatico(df_total):
  df_brahiam = df_total[df_total["Integrante"] == "Brahiam"]
  llevar_list, recoger_list = [], []

  for idx, row in df_total.iterrows():
    if row["Integrante"] == "Brahiam":
      llevar_list.append("N/A")
      recoger_list.append("N/A")
    else:
      dia = row["Día"]
      h_inicio_pasajero = row["Hora_Inicio_Num"]
      h_fin_pasajero = row["Hora_Fin_Num"]
      clases_b_dia = df_brahiam[df_brahiam["Día"] == dia]

      ocupado_llevar = any(
          c_b["Hora_Inicio_Num"] <= h_inicio_pasajero < c_b["Hora_Fin_Num"]
          for _, c_b in clases_b_dia.iterrows()
      )
      if ocupado_llevar:
        llevar_list.append("🔴 NO (Brahiam en clase)")
      else:
        h_str = datetime.strptime(
            f"{int(h_inicio_pasajero)}:00", "%H:%M"
        ).strftime("%I:%M %p")
        llevar_list.append(f"🟢 SÍ ({h_str})")

      ocupado_recoger = any(
          c_b["Hora_Inicio_Num"] <= h_fin_pasajero <= c_b["Hora_Fin_Num"]
          for _, c_b in clases_b_dia.iterrows()
      )
      if ocupado_recoger:
        recoger_list.append("🔴 NO (Brahiam en clase)")
      else:
        h_str_fin = datetime.strptime(
            f"{int(h_fin_pasajero)}:00", "%H:%M"
        ).strftime("%I:%M %p")
        recoger_list.append(f"🟢 SÍ ({h_str_fin})")

  df_total["Llevar (🚗)"] = llevar_list
  df_total["Recoger (🚙)"] = recoger_list
  return df_total


# Función para calcular franjas horarias desocupadas (06:00 a 22:00)
def obtener_franjas_libres(df_persona_dia):
  if df_persona_dia.empty:
    return ["🟢 Todo el día libre (06:00 AM - 10:00 PM)"]

  # Ordenar ocupaciones por hora de inicio
  ocupaciones = df_persona_dia.sort_values(by="Hora_Inicio_Num")[
      ["Hora_Inicio_Num", "Hora_Fin_Num"]
  ].values.tolist()

  franjas_libres = []
  inicio_ventana = 6.0  # 06:00 AM
  fin_ventana = 22.0  # 10:00 PM

  actual = inicio_ventana
  for h_in, h_fi in ocupaciones:
    if h_in > actual:
      franjas_libres.append((actual, min(h_in, fin_ventana)))
    actual = max(actual, h_fi)

  if actual < fin_ventana:
    franjas_libres.append((actual, fin_ventana))

  # Formatear a texto comprensible
  resultado = []
  for f_in, f_fi in franjas_libres:
    if f_fi - f_in >= 0.25:  # Mostrar bloques mayores a 15 minutos
      str_in = datetime.strptime(
          f"{int(f_in):02d}:{int((f_in%1)*60):02d}", "%H:%M"
      ).strftime("%I:%M %p")
      str_fi = datetime.strptime(
          f"{int(f_fi):02d}:{int((f_fi%1)*60):02d}", "%H:%M"
      ).strftime("%I:%M %p")
      resultado.append(f"🟢 {str_in} - {str_fi}")

  return resultado if resultado else ["🔴 Sin franjas libres discontinuas"]


# 5. PANEL LATERAL: AGREGAR Y ELIMINAR ACTIVIDADES
with st.sidebar:
  st.header("➕ Agregar Actividad")
  with st.form("form_nueva_actividad"):
    nuevo_integrante = st.selectbox(
        "Integrante", ["Brahiam", "Marcela", "Isaac", "Mateo", "Familia"]
    )
    nuevo_dia = st.selectbox(
        "Día",
        [
            "Lunes",
            "Martes",
            "Miércoles",
            "Jueves",
            "Viernes",
            "Sábado",
            "Domingo",
        ],
    )
    nueva_actividad = st.text_input("Actividad / Tarea")
    nuevo_lugar = st.text_input("Aula / Sede")
    h_inicio_val = st.number_input(
        "Hora Inicio (24h)",
        min_value=0.0,
        max_value=23.0,
        value=8.0,
        step=0.5,
    )
    h_fin_val = st.number_input(
        "Hora Fin (24h)", min_value=0.5, max_value=24.0, value=10.0, step=0.5
    )

    btn_guardar = st.form_submit_button("Guardar Actividad")

    if btn_guardar and nueva_actividad:
      dias_dict = {
          "Lunes": "2026-08-03",
          "Martes": "2026-08-04",
          "Miércoles": "2026-08-05",
          "Jueves": "2026-08-06",
          "Viernes": "2026-08-07",
          "Sábado": "2026-08-08",
          "Domingo": "2026-08-09",
      }
      fecha_str = dias_dict.get(nuevo_dia, "2026-08-03")
      h_in_dt = datetime.strptime(
          f"{int(h_inicio_val):02d}:{int((h_inicio_val%1)*60):02d}", "%H:%M"
      )
      h_fi_dt = datetime.strptime(
          f"{int(h_fin_val):02d}:{int((h_fin_val%1)*60):02d}", "%H:%M"
      )
      nuevo_id = (
          max([x.get("id", 0) for x in st.session_state.agenda], default=0) + 1
      )

      st.session_state.agenda.append({
          "id": nuevo_id,
          "tipo": "dinamica",
          "Día": nuevo_dia,
          "Integrante": nuevo_integrante,
          "Hora_Inicio_Num": h_inicio_val,
          "Hora_Fin_Num": h_fin_val,
          "Hora_Inicio": f"{fecha_str} {h_in_dt.strftime('%H:%M')}",
          "Hora_Fin": f"{fecha_str} {h_fi_dt.strftime('%H:%M')}",
          "Horario": (
              f"{h_in_dt.strftime('%I:%M %p')} - {h_fi_dt.strftime('%I:%M %p')}"
          ),
          "Actividad": nueva_actividad,
          "Lugar / Aula": nuevo_lugar,
      })
      st.success(f"¡Guardado para {nuevo_integrante}!")

  st.markdown("---")
  st.header("🗑️ Gestionar Actividades Creadas")
  actividades_dinamicas = [
      x for x in st.session_state.agenda if x.get("tipo") == "dinamica"
  ]
  if actividades_dinamicas:
    opciones_eliminar = {
        f"{item['Día']} - {item['Integrante']}: {item['Actividad']}"
        f" ({item['Horario']})": item.get("id")
        for item in actividades_dinamicas
    }
    seleccion_borrar = st.selectbox(
        "Selecciona actividad a borrar:", list(opciones_eliminar.keys())
    )
    if st.button("❌ Eliminar Actividad Seleccionada"):
      id_borrar = opciones_eliminar[seleccion_borrar]
      st.session_state.agenda = [
          x for x in st.session_state.agenda if x.get("id") != id_borrar
      ]
      st.success("Actividad eliminada.")
      st.rerun()
  else:
    st.caption("🔒 *Las actividades fijas están protegidas.*")

# Procesar datos
df_base = pd.DataFrame(st.session_state.agenda)
df_procesado = (
    calcular_transporte_automatico(df_base) if not df_base.empty else df_base
)

# 6. CONTROLES Y FILTROS MULTI-SELECCIÓN
col1, col2, col3 = st.columns([1.5, 1, 1])
with col1:
  integrantes_disponibles = sorted(
      list(set([x["Integrante"] for x in st.session_state.agenda]))
  )
  # MULTISELECT: Permite elegir 1, 2, 3 o todos los integrantes
  filtro_personas = st.multiselect(
      "👥 Integrantes (Comparativa):",
      options=integrantes_disponibles,
      default=integrantes_disponibles,
  )
with col2:
  filtro_dia = st.selectbox(
      "📅 Día de la semana:",
      [
          "Todos",
          "Lunes",
          "Martes",
          "Miércoles",
          "Jueves",
          "Viernes",
          "Sábado",
          "Domingo",
      ],
      index=0,
  )
with col3:
  tipo_vista = st.selectbox(
      "🎨 Estilo de Visualización:",
      ["📱 Tarjetas Modernas (Bordes & Badges)", "📋 Tabla Detallada"],
  )

# Aplicar Filtros
df_view = df_procesado.copy() if not df_procesado.empty else df_procesado
if not df_view.empty:
  if filtro_personas:
    df_view = df_view[df_view["Integrante"].isin(filtro_personas)]
  else:
    df_view = df_view.iloc[0:0]  # Vacío si no selecciona a nadie

  if filtro_dia != "Todos":
    df_view = df_view[df_view["Día"] == filtro_dia]

  df_view["Inicio_dt"] = pd.to_datetime(df_view["Hora_Inicio"])
  df_view["Fin_dt"] = pd.to_datetime(df_view["Hora_Fin"])
  df_view["Horas_Invertidas"] = (
      df_view["Fin_dt"] - df_view["Inicio_dt"]
  ).dt.total_seconds() / 3600

st.markdown("---")

# 7. CÁLCULO DE HORAS Y FRANJAS DISPONIBLES (6 AM a 10 PM = 16h/día)
if filtro_personas:
  # Definición de la ventana de tiempo base
  dias_conteo = 1 if filtro_dia != "Todos" else 5
  base_horas_por_persona = 16.0 * dias_conteo

  cols_metrics = st.columns(len(filtro_personas))
  for idx, persona in enumerate(filtro_personas):
    df_p = df_view[df_view["Integrante"] == persona]
    horas_ocupadas = df_p["Horas_Invertidas"].sum() if not df_p.empty else 0.0
    horas_libres = max(0.0, base_horas_por_persona - horas_ocupadas)

    with cols_metrics[idx]:
      st.metric(
          f"👤 {persona} ({filtro_dia})",
          f"📚 {horas_ocupadas:.1f}h ocupadas",
          f"🌴 {horas_libres:.1f}h libres (de {base_horas_por_persona:.0f}h)",
      )

  # Si se selecciona un día específico, mostrar módulo de Franjas Libres
  if filtro_dia != "Todos":
    st.markdown("### 🟢 Franjas Horarias Disponibles (Desocupadas)")
    cols_franjas = st.columns(len(filtro_personas))
    for idx, persona in enumerate(filtro_personas):
      df_p_dia = df_view[df_view["Integrante"] == persona]
      franjas = obtener_franjas_libres(df_p_dia)

      with cols_franjas[idx]:
        st.markdown(f"**Disponibilidad de {persona}:**")
        for f in franjas:
          st.success(f)

st.markdown("---")

# 8. RENDERIZADO DE VISTAS (TARJETAS O TABLA)
if tipo_vista == "📱 Tarjetas Modernas (Bordes & Badges)":
  st.subheader("📆 Tarjetero Semanal Interactivo")
  dias_semana = (
      ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
      if filtro_dia == "Todos"
      else [filtro_dia]
  )
  cols = st.columns(len(dias_semana))

  for i, dia in enumerate(dias_semana):
    with cols[i if len(dias_semana) > 1 else 0]:
      borde_dia = (
          "border: 2px solid #f59e0b;"
          if dia == dia_hoy_nombre
          else "border: 1px solid #334155;"
      )
      st.markdown(
          f"<div style='text-align: center; background: #1e293b; padding:"
          " 10px; border-radius: 12px; font-weight: bold; color: #f8fafc;"
          f" margin-bottom: 12px; {borde_dia}'>{dia} {'⭐' if dia == dia_hoy_nombre else ''}</div>",
          unsafe_allow_html=True,
      )

      df_day = (
          df_view[df_view["Día"] == dia]
          if not df_view.empty
          else pd.DataFrame()
      )
      if df_day.empty:
        st.caption("🟢 Sin actividades")
      else:
        for _, row in df_day.iterrows():
          if row["Integrante"] == "Marcela":
            card_bg, border_color = (
                "background: linear-gradient(135deg, #1e3a5f, #1e40af);",
                "#93c5fd",
            )
          elif row["Integrante"] == "Brahiam":
            card_bg, border_color = (
                "background: linear-gradient(135deg, #4c1d24, #9f1239);",
                "#fca5a5",
            )
          elif row["Integrante"] == "Isaac":
            card_bg, border_color = (
                "background: linear-gradient(135deg, #064e3b, #047857);",
                "#6ee7b7",
            )
          elif row["Integrante"] == "Mateo":
            card_bg, border_color = (
                "background: linear-gradient(135deg, #78350f, #b45309);",
                "#fcd34d",
            )
          else:
            card_bg, border_color = (
                "background: linear-gradient(135deg, #374151, #4b5563);",
                "#d1d5db",
            )

          st.markdown(
              f"""
                    <div style="{card_bg} border: 1.5px solid {border_color}; border-radius: 16px; padding: 14px; margin-bottom: 14px; color: white;">
                        <div style="display: flex; justify-content: space-between;">
                            <span style="font-size: 11px; font-weight: bold;">⏰ {row['Horario']}</span>
                            <span style="font-size: 11px; font-weight: bold;">👤 {row['Integrante']}</span>
                        </div>
                        <div style="font-size: 14px; font-weight: 700; margin-top: 8px;">{row['Actividad']}</div>
                        <div style="font-size: 12px; opacity: 0.85;">📍 {row['Lugar / Aula']}</div>
                        <div style="margin-top: 8px; padding-top: 6px; border-top: 1px solid rgba(255,255,255,0.2); font-size: 10px;">
                            <div>🚗 Llevar: {row['Llevar (🚗)']}</div>
                            <div>🚙 Recoger: {row['Recoger (🚙)']}</div>
                        </div>
                    </div>
                    """,
              unsafe_allow_html=True,
          )

elif tipo_vista == "📋 Tabla Detallada":
  st.subheader("📋 Vista en Tabla Detallada")
  if not df_view.empty:
    df_tabla = df_view[[
        "Día",
        "Integrante",
        "Horario",
        "Actividad",
        "Lugar / Aula",
        "Llevar (🚗)",
        "Recoger (🚙)",
    ]]
    st.dataframe(df_tabla, use_container_width=True, hide_index=True)

# 9. MÓDULO DE TELEGRAM
st.markdown("---")
st.subheader("🔔 Panel de Alertas y Notificaciones por Telegram")

with st.form("form_telegram_individual"):
  col_a, col_b, col_c = st.columns(3)
  with col_a:
    api_token = st.text_input(
        "🤖 Telegram Bot Token:", value=secret_token, type="password"
    )
  with col_b:
    chat_id_brahiam = st.text_input(
        "💬 Chat ID de Brahiam:", value=secret_id_brahiam
    )
  with col_c:
    chat_id_marcela = st.text_input(
        "💬 Chat ID de Marcela:", value=secret_id_marcela
    )

  col_btn1, col_btn2 = st.columns(2)
  with col_btn1:
    btn_probar = st.form_submit_button("⚡ Enviar Mensaje de Prueba")
  with col_btn2:
    btn_enviar_hoy = st.form_submit_button("📅 Enviar Agenda de Hoy")

  if btn_probar:
    if api_token and (chat_id_brahiam or chat_id_marcela):
      msg_prueba = (
          "✅ *¡Conexión Exitosa!*\nEl Centro de Control Familiar está"
          " conectado correctamente a tu Telegram."
      )
      ok_b = (
          enviar_mensaje_telegram(api_token, chat_id_brahiam, msg_prueba)
          if chat_id_brahiam
          else True
      )
      ok_m = (
          enviar_mensaje_telegram(api_token, chat_id_marcela, msg_prueba)
          if chat_id_marcela
          else True
      )

      if ok_b and ok_m:
        st.success("¡Prueba enviada correctamente a Telegram!")
      else:
        st.error("Error enviando la prueba. Revisa la consola o configuración.")
    else:
      st.error("Ingresa el Bot Token y al menos un Chat ID.")

  if btn_enviar_hoy:
    if api_token and (chat_id_brahiam or chat_id_marcela):
      df_hoy = df_procesado[df_procesado["Día"] == dia_hoy_nombre]
      if df_hoy.empty:
        msg_agenda = (
            f"📅 *Agenda para Hoy ({dia_hoy_nombre})*\n\n🎉 ¡No hay actividades"
            " programadas para hoy! Día Libre."
        )
      else:
        msg_agenda = f"📅 *AGENDA FAMILIAR - {dia_hoy_nombre.upper()}*\n\n"
        for _, r in df_hoy.iterrows():
          msg_agenda += f"👤 *{r['Integrante']}*\n"
          msg_agenda += f"⏰ {r['Horario']}\n"
          msg_agenda += f"📚 {r['Actividad']} ({r['Lugar / Aula']})\n"
          if r["Integrante"] != "Brahiam":
            msg_agenda += (
                f"🚗 Llevar: {r['Llevar (🚗)']}\n🚙 Recoger:"
                f" {r['Recoger (🚙)']}\n"
            )
          msg_agenda += "-----------------------------\n"

      if chat_id_brahiam:
        enviar_mensaje_telegram(api_token, chat_id_brahiam, msg_agenda)
      if chat_id_marcela:
        enviar_mensaje_telegram(api_token, chat_id_marcela, msg_agenda)
      st.success(f"¡Agenda de hoy ({dia_hoy_nombre}) enviada por Telegram!")
