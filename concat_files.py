import streamlit as st
import pandas as pd

# Função para concatenar arquivos
def concatenate_files(files):
    dataframes = []
    for file in files:
        if file.name.endswith('.csv'):
            df = pd.read_csv(file)
        elif file.name.endswith('.xlsx'):
            df = pd.read_excel(file)
        else:
            st.error(f"Arquivo {file.name} não suportado.")
            return None
        dataframes.append(df)
    
    # Concatenar todos os DataFrames sem considerar as colunas
    concatenated_df = pd.concat(dataframes, axis=0, ignore_index=True)
    return concatenated_df

# Aplicação principal
def run_concat_files():
    st.title("Concatenar Arquivos Excel/CSV")

    tab1, tab2 = st.tabs(["🧮 Concatenar", "⚠ Como usar"])


    with tab1:
    
        uploaded_files = st.file_uploader("Envie seus arquivos", type=["csv", "xlsx"], accept_multiple_files=True)
        
        if uploaded_files:
            concatenated_df = concatenate_files(uploaded_files)
            
            if concatenated_df is not None:
                st.write("Arquivos concatenados com sucesso!")
                st.dataframe(concatenated_df)
                
                # Opção para baixar o arquivo concatenado
                csv = concatenated_df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="Baixar arquivo concatenado",
                    data=csv,
                    file_name='concatenated_files.csv',
                    mime='text/csv',
                )
    with tab2:
        st.title("Como Usar")