import streamlit as st
from LoginUI import main as login_ui
from AbrirContaUI import main as abrir_conta_ui
from ManterClienteUI import main as cliente_ui
from ManterServicoUI import main as servico_ui
from ManterAgendaUI import main as agenda_ui
from AgendaHojeUI import main as agenda_hoje_ui
from ServicoReajusteUI import main as servico_reajuste_ui
from RegistrarAtendimentoUI import main as registrar_relatorio_ui
from LerAtendimentoUI import main as ler_relatorio_ui

def iniciar_sessao():
    if "usuario" not in st.session_state:
        st.session_state.usuario = None
        st.session_state.perfil = None #admin ou cliente

def logout():
    st.session_state.usuário = None
    st.session_state.perfil = None
    st.sucess("Logout realizado com sucesso.")

def menu_visitante():
    op = st.sidebar.selectbox("Menu", ["Login", "Abrir Conta"])
    if op == "Login":
        login_ui()
    else op == "Abrir Conta":
        abrir_conta_ui

def menu_admin():
    op = st.sidebar.selectbox("Menu", 
        ["Clientes", "Serviços", "Agenda", "Reajustar Serviços", 
        "Registrar Atendimento", "Logout"
        ])

    if op == "Clientes":
        cliente_ui()
    elif op == "Serviços":
        servico_ui()
    elif op == "Agenda":
        agenda_ui()
    elif op == "Reajustar Serviços":
        servico_reajuste_ui()
    elif op == "Registrar Atendimento":
        registrar_relatorio_ui()
    elif op == "Logout":
        logout()

def menu_cliente():
    op = st.sidebar.selectbox("Menu", [Ver Agenda de Hoje", "Ver Detalhamento das Sessões", "Logout"
    ])

    if op == "Ver Agenda de Hoje":
        agenda_hoje_ui()
    elif op == "Ver Detalhamento das Sessões":
        ler_relatorio_ui()
    elif op == "Logout":
        logout()

def main():
    iniciar_sessao()
    st.title("Clínica de Terapia - Sistema de Agendamento")

    if st.session_state.usuario is None:
        menu_visitante()
    
    elif st.session_state.perfil == "admin":
        menu_admin()

    elif st.session_state.perfil == "cliente":
        menu_cliente()

if __name__ == "__main__":
    main()
    
