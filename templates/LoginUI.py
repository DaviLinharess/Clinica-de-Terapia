import streamlit as st
from models.Cliente import Clientes

def main():
    st.subheader("Login")

    email = st.text_input("Email")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        for c in Clientes.listar():
            if c.get_email() == email and c.get_senha() == senha:
                st.session_state.usuario = c
                st.session_state.perfil = "admin" if c.get_id() == 1 else "cliente" #admin fixo, tendo id 1
                st.sucess("Login Realizado")
                st.rerun()
                return
            st.error("Email ou senha inválidos.")
            