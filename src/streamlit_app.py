import streamlit as st
import streamlit_authenticator as stauth
import yaml
from menu import Menu
from streamlit_option_menu import option_menu
from yaml.loader import SafeLoader

st.set_page_config(page_title="Sistema Margem Líquida", layout="wide")

st.markdown("## :bank: Sistema MargemLíquida :bank:")

with st.sidebar:

    pagina = option_menu(
        menu_title=None,  # required
        options=Menu.labels,  # required
        icons=None,  # optional
        menu_icon="menu-down",  # optional
        default_index=0,  # optional
        )   

Menu.carregar_pagina(pagina)