import streamlit as st
import pandas as pd
from openai import OpenAI

client = OpenAI(
  organization='org-UQuGzwzlmTQL61uA4vE5ZTkn',
  project='proj_Qj5H908LWvkgwtSuRGYhAhY0',
)

st.title("Generador de descripciones de cursos CLIE")

areas = pd.read_csv("https://raw.githubusercontent.com/EIEM-TEC/CLIE/refs/heads/main/areas.csv")
cursos = pd.read_csv("https://raw.githubusercontent.com/EIEM-TEC/CLIE/refs/heads/main/cursos/cursos_malla.csv")
rasgos = pd.read_csv("https://raw.githubusercontent.com/EIEM-TEC/CLIE/refs/heads/main/rasgos.csv")
saberes = pd.read_csv("https://raw.githubusercontent.com/EIEM-TEC/CLIE/refs/heads/main/saberes.csv")
cursos_rasgos = pd.read_csv("https://raw.githubusercontent.com/EIEM-TEC/CLIE/refs/heads/main/cursos/cursos_rasgos.csv")

nomArea = st.selectbox(
    'Area',
    areas["nombre"])

codArea = areas[areas["nombre"]==nomArea]["codArea"].item()
cursos = cursos[(cursos["area"]==codArea) & (cursos["semestre"]<=10)]
saberes = saberes[saberes["codArea"]==codArea]


nomCurso = st.selectbox(
    "Curso",
    cursos[cursos["area"]==codArea]["nombre"])


codCurso = cursos[cursos["nombre"]==nomCurso]["codigo"].item()
idCurso = cursos[cursos["nombre"]==nomCurso]["id"].item()

codSaber = cursos_rasgos[cursos_rasgos["id"]==idCurso]["codSaber"].str.split(';', expand=False).item()

"Saberes del curso:"

for index in range(len(codSaber)):
    st.text(saberes[saberes["codSaber"]==codSaber[index]]["nombre"])
    st.text(saberes[saberes["codSaber"]==codSaber[index]]["nombre"].item())


if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4o"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})