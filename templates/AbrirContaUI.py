import streamlit as st
from models.Cliente import Cliente, Clientes

def main():
    st.subheader("Abrir Conta - Novo Cliente")

    nome = st.text_input("Nome")
    email = st.text_input("Email")
    senha = st.text_input("Senha", type="password")
    fone = st.text_input("Telefone")

    if st.button("Cadastrar"):
        try:
            for c in Clientes.listar():
                if c.get_email == email:
                    st.warning("Já existe cliente com esse email")
                    return
            
            novo = Cliente(0, email, senha, nome, fone)
            Clientes.inserir(novo)
            st.sucess("Conta criada")
        except Exception as e:
            st.error(f"Erro ao cadastrar: {e}")
            