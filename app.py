import streamlit as st
from chatbot import responder_usuario  # Usa el modelo entrenado

st.set_page_config(page_title="Asistente de Reuniones", layout="centered")
st.title("🤖 Asistente Virtual de Reuniones")

st.markdown("""
Este asistente te ayuda a agendar reuniones automáticamente.
Solo escribe tu solicitud en lenguaje natural y se encargará del resto.
""")

mensaje = st.text_input("🗨️ Escribe tu solicitud de reunión:")

if mensaje:
    respuesta = responder_usuario(mensaje)
    st.success(respuesta)

    if st.button("✅ Confirmar reunión"):
        from datetime import datetime
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st.write(f"📅 Reunión registrada con éxito el {fecha}.")
