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
                "Pagina inicial",
                "Juntar Arquivos",
                "Juntar Arquivos por Colunas Diferentes",
          
            ],
            icons=[ "infinity", "cash-coin"],
            menu_icon="cast",
            default_index=0,
        )
        st.caption('Versão atual: 1.0.0')


    if choice == "Pagina inicial":
    

        st.markdown(f"""
            <div style='display: flex; align-items: center; justify-content: center;'>
                <h2>Sistema Manipulação de dados</h2>
            </div>
        """, unsafe_allow_html=True)


        st.divider()  # 👈 Draws a horizontal rule
        st.markdown(f"""
            <div style='display: flex; align-items: center; justify-content: center;'>
                <p>Boas vindas! Selecione no menu à esquerda a ferramenta que deseja utilizar e bom trabalho!</p>
            </div>
        """, unsafe_allow_html=True)
    elif choice == "Juntar Arquivos":
        run_concat_files()

    
    elif choice == "Juntar Arquivos por Colunas Diferentes":
        run_join_files()


if __name__ == '__main__':
    main()
