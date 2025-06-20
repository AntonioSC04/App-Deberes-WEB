import streamlit as st
import Funciones

deberes = Funciones.get_deberes()

def add_deber():
    deber = st.session_state["new_deber"] + "\n"
    deberes.append(deber)
    Funciones.write_deberes(deberes)

st.title("App de Deberes")
st.subheader("Esta es mi app de deberes")
st.write("Esta app es para incrementar tu productividad")

for index, deber in enumerate(deberes):
    checkbox = st.checkbox(deber, key=f"deber_{index}")
    if checkbox:
        deberes.pop(index)
        Funciones.write_deberes(deberes)
        st.rerun()

st.text_input("Nuevo Deber", placeholder="Ingresa un nuevo deber...",
              on_change=add_deber, key="new_deber", label_visibility="collapsed")

