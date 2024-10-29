import streamlit as st
from streamlit_option_menu import option_menu
from concat_files import run_concat_files
from join_files import run_join_files

def main():
    st.title("Manipulação de dados")
    
    # Menu com uma opção
    with st.sidebar:
        st.sidebar.title("Menu")
        choice = option_menu(
            "Menu",
            [
                "Juntar Arquivos",
                "Juntar Arquivos por Colunas Diferentes",
          
            ],
            icons=[ "infinity", "cash-coin"],
            menu_icon="cast",
            default_index=0,
        )
        st.caption('Versão atual: 1.0.0')


    if choice == "Juntar Arquivos":
        run_concat_files()

    
    if choice == "Juntar Arquivos por Colunas Diferentes":
        run_join_files()

if __name__ == '__main__':
    main()