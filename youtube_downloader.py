from pytube import YouTube
import streamlit as st
from io import BytesIO

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
            yt = YouTube(url)
            
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
                placeholder="Escolha uma ou mais opções",
                format_func=lambda x: x["label"]
            )

            if st.button("Baixar"):
                for option in selected_options:
                    stream = yt.streams.get_by_itag(option["itag"])
                    
                    # Salva o arquivo em memória usando BytesIO
                    buffer = BytesIO()
                    stream.stream_to_buffer(buffer)
                    buffer.seek(0)
                    
                    # Oferece o arquivo para download
                    st.download_button(
                        label=f"Baixar {option['label']}",
                        data=buffer,
                        file_name=stream.default_filename,
                        mime=stream.mime_type
                    )

        except Exception as e:
            st.error(f"Erro: {str(e)}")

run_youtube_downloader()
