import streamlit as st
import pandas as pd

def read_file(file):
    if file.name.endswith('.csv'):
        return pd.read_csv(file)
    elif file.name.endswith('.xlsx'):
        return pd.read_excel(file)
    else:
        st.error(f"Arquivo {file.name} não é suportado.")
        return None

def get_columns(file):
    df = read_file(file)
    if df is not None:
        return df.columns.tolist()
    else:
        return []

def merge_files(df1, df2, join_type, join_column1, join_column2):
    """Realiza a junção de dois DataFrames com base nas colunas e tipo de join especificados."""
    return pd.merge(df1, df2, left_on=join_column1, right_on=join_column2, how=join_type)

def run_join_files():
    st.subheader("Juntar Arquivos Excel/CSV com Base em Colunas Diferentes")
    
    tab1, tab2 = st.tabs(["🧮 Juntar", "⚠ Como usar"])

    with tab1:
        file1 = st.file_uploader("Envie o primeiro arquivo", type=["csv", "xlsx"])
        file2 = st.file_uploader("Envie o segundo arquivo", type=["csv", "xlsx"])
        
        if file1 and file2:
            df1_columns = get_columns(file1)
            df2_columns = get_columns(file2)

            if df1_columns and df2_columns:
                join_column1 = st.selectbox("Escolha a coluna do primeiro arquivo", df1_columns)
                join_column2 = st.selectbox("Escolha a coluna do segundo arquivo", df2_columns)

                join_options = {
                    "Inner Join (Apenas registros presentes em ambos os arquivos)": "inner",
                    "Left Join (Todos os registros do primeiro arquivo)": "left",
                    "Right Join (Todos os registros do segundo arquivo)": "right",
                    "Full Outer Join (Todos os registros de ambos os arquivos)": "outer"
                }

                join_choice = st.selectbox("Escolha o tipo de combinação:", list(join_options.keys()))
                selected_join_type = join_options[join_choice]
                
                if st.button("Juntar Arquivos"):
                    df1 = read_file(file1)
                    df2 = read_file(file2)
                    if df1 is not None and df2 is not None:
                        merged_df = merge_files(df1, df2, selected_join_type, join_column1, join_column2)
                        st.success("Arquivos combinados com sucesso!")
                        st.dataframe(merged_df)
                        
                        csv_data = merged_df.to_csv(index=False).encode('utf-8')
                        st.download_button(
                            label="Baixar arquivo combinado",
                            data=csv_data,
                            file_name='arquivos_combinados.csv',
                            mime='text/csv',
                        )
            else:
                st.error("Não foi possível ler as colunas dos arquivos. Verifique se os arquivos estão corretos.")

    with tab2:
        st.title("Como usar")