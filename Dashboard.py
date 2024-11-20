import streamlit as st
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Função para conectar ao banco de dados MySQL
def conectar_db():
    conn = mysql.connector.connect(
        host="localhost", 
        user="root", 
        password="1234", 
        database="projetopython_db"  
    )
    return conn

# Função para buscar dados do banco
def buscar_dados(query):
    conn = conectar_db()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Título do Streamlit
st.title("Análise de Equipamentos nas Escolas")

# Opções de visualização
st.sidebar.title("Seleção de Dados")
opcao = st.sidebar.selectbox("Escolha a Região", ["Nacional", "Nordeste", "Norte", "Sudeste"])

# Com base na seleção, definimos a tabela a ser consultada
if opcao == "Nacional":
    query = "SELECT * FROM equip_censu_nacional"
elif opcao == "Nordeste":
    query = "SELECT * FROM equip_censu_nordeste"
elif opcao == "Norte":
    query = "SELECT * FROM equip_censu_norte"
else:
    query = "SELECT * FROM equip_censu_sudeste"

# Buscar os dados
df = buscar_dados(query)

# Exibir os dados em uma tabela
st.write("Dados de Equipamentos", df)

# Plotar gráfico - Quantidade de Internet por tipo de instituição
st.subheader("Quantidade de Internet por Tipo de Instituição")

# Agrupar os dados por tipo de instituição e somar a quantidade de internet
if "INTERNET" in df.columns:
    df_grouped = df.groupby("TIPO_INSTITUICAO")["INTERNET"].sum().reset_index()

    # Plotar o gráfico
    fig, ax = plt.subplots()
    sns.barplot(x="TIPO_INSTITUICAO", y="INTERNET", data=df_grouped, ax=ax)
    plt.xticks(rotation=45, ha='right')
    ax.set_title('Quantidade de Internet por Tipo de Instituição')
    ax.set_xlabel('Tipo de Instituição')
    ax.set_ylabel('Quantidade de Internet')
    st.pyplot(fig)

# Plotar gráfico - Quantidade de projetores por tipo de instituição
st.subheader("Quantidade de Projetores por Tipo de Instituição")

if "PROJETOR" in df.columns:
    df_grouped_proj = df.groupby("TIPO_INSTITUICAO")["PROJETOR"].sum().reset_index()

    # Plotar o gráfico
    fig, ax = plt.subplots()
    sns.barplot(x="TIPO_INSTITUICAO", y="PROJETOR", data=df_grouped_proj, ax=ax)
    plt.xticks(rotation=45, ha='right')
    ax.set_title('Quantidade de Projetores por Tipo de Instituição')
    ax.set_xlabel('Tipo de Instituição')
    ax.set_ylabel('Quantidade de Projetores')
    st.pyplot(fig)

# Plotar gráfico - Quantidade de Notebooks por tipo de instituição
st.subheader("Quantidade de Notebooks por Tipo de Instituição")

if "NOTEBOOK_ALUNOS" in df.columns:
    df_grouped_notebooks = df.groupby("TIPO_INSTITUICAO")["NOTEBOOK_ALUNOS"].sum().reset_index()

    # Plotar o gráfico
    fig, ax = plt.subplots()
    sns.barplot(x="TIPO_INSTITUICAO", y="NOTEBOOK_ALUNOS", data=df_grouped_notebooks, ax=ax)
    plt.xticks(rotation=45, ha='right')
    ax.set_title('Quantidade de Notebooks por Tipo de Instituição')
    ax.set_xlabel('Tipo de Instituição')
    ax.set_ylabel('Quantidade de Notebooks')
    st.pyplot(fig)

# Plotar gráfico - Quantidade de Tablets por tipo de instituição
st.subheader("Quantidade de Tablets por Tipo de Instituição")

if "TABLET_ALUNOS" in df.columns:
    df_grouped_tablets = df.groupby("TIPO_INSTITUICAO")["TABLET_ALUNOS"].sum().reset_index()

    # Plotar o gráfico
    fig, ax = plt.subplots()
    sns.barplot(x="TIPO_INSTITUICAO", y="TABLET_ALUNOS", data=df_grouped_tablets, ax=ax)
    plt.xticks(rotation=45, ha='right')
    ax.set_title('Quantidade de Tablets por Tipo de Instituição')
    ax.set_xlabel('Tipo de Instituição')
    ax.set_ylabel('Quantidade de Tablets')
    st.pyplot(fig)
