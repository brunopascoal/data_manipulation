from pytubefix import YouTube
import streamlit as st

def run_youtube_downloader():
    
    st.markdown(f"""
            <div style='display: flex; align-items: center; justify-content: center;'>
                <h2>Youtube Downloader</h2>
            </div>
        """, unsafe_allow_html=True)


    st.divider() 
    st.markdown(f"""
            <div style='display: flex; align-items: center; justify-content: center;'>
                <p>Escolha as opções conforme desejado para baixar!</p>
            </div>
        """, unsafe_allow_html=True)
      
    url = st.text_input("Insira a URL do YouTube")

    if url:
        try:
            yt = YouTube(url, use_po_token=True)
            
            options = [
                {
                    "label": f"{stream.type.upper()} - {stream.resolution or stream.abr} - {stream.mime_type} - Itag: {stream.itag}",
                    "itag": stream.itag
                }
                for stream in yt.streams
            ]
            
            selected_options = st.multiselect(
                "Escolha as opções de download",
                options,
                laceholder="Escolha uma ou mais opções",
                format_func=lambda x: x["label"]
            )

            if st.button("Baixar"):
                for option in selected_options:
                    stream = yt.streams.get_by_itag(option["itag"])
                    stream.download()
                    st.success(f"Download concluído: {option['label']}")

        except Exception as e:
            st.error(f"Erro: {str(e)}")

