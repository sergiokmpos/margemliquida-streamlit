import streamlit as st
from datetime import datetime, timedelta
import time
from libs.tesouro_direto import TesouroDireto
from st_pages import Page, Section, show_pages, add_page_title
import pytz

## Construção da página
        
st.set_page_config(layout="wide")
add_page_title()
mensagens = st.container()

@st.cache_data
def atualizar_dados_tesouro_direto(data_atual):
    td = TesouroDireto()
    td.atualizar_graficos()
    return td     

# st.set_page_config(
#     page_title="Tesouro Direto",
#     layout="wide",
# )

delta = 0
# st.text(time.tzname)
if time.tzname[0] == "UTC":
     delta = 3;
agora = datetime.today()
# st.text("Agora:")
# st.text(agora)
# st.text("Agora - delta:")
agora = datetime.today() - timedelta(hours=delta, minutes=0) 
# st.text(agora)
# st.text("Agora formatado:")
agora = agora.strftime('%d/%m/%Y')
# st.text(agora)

td = atualizar_dados_tesouro_direto(agora)

# st.sidebar.markdown("# Tesouro Direto")

selic, ipca, pre = st.tabs(["SELIC", ":dragon: IPCA+", "PREFIXADO"])

with selic:
    st.markdown("## Tesouro SELIC")
    # st.sidebar.markdown("## Tesouro SELIC")
    st.plotly_chart(td.retornar_grafico_precos_tesouro_selic(), use_container_width=True)
    st.plotly_chart(td.retornar_grafico_taxas_tesouro_selic(), use_container_width=True)

with ipca:
    st.markdown("## Tesouro IPCA+")
    # st.sidebar.markdown("## Tesouro IPCA+")
    st.plotly_chart(td.retornar_grafico_precos_tesouro_ipca(), use_container_width=True)
    st.plotly_chart(td.retornar_grafico_taxas_tesouro_ipca(), use_container_width=True)

with pre:
    st.markdown("## Tesouro PREFIXADO")
    # st.sidebar.markdown("## Tesouro PREFIXADO")
    st.plotly_chart(td.retornar_grafico_precos_tesouro_pre(), use_container_width=True)
    st.plotly_chart(td.retornar_grafico_taxas_tesouro_pre(), use_container_width=True)