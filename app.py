from summarizer import generate_summary
from gtts import gTTS
import os
import streamlit as st
import docx2txt


#---------------------------------#
# Page layout
## Page expands to full width
st.set_page_config(page_title='Text Summarizer App',
    layout='wide')
#---------------------------------#


#---------------------------------#
st.write("""
# Text Summarizer App
""")
#---------------------------------#


#---------------------------------#
with st.sidebar.header('Upload your Text file'):
    uploaded_file = st.sidebar.file_uploader("Upload your input text file", type=["txt"])
#---------------------------------#


#---------------------------------#
# Main panel

if uploaded_file is not None:
    raw_text = str(uploaded_file.read(),"utf-8")
    st.write("""
    ### Text Input
    """)
    st.write(raw_text)
    
    with open("uploaded_file.txt", "w") as f:
        f.write(raw_text)

    summarized_text = generate_summary("uploaded_file.txt", 2)
    st.write("""
    ### Summarized Text
    """)
    st.write(summarized_text)
    #print(summarized_text)

    mytext = summarized_text
    audio = gTTS(text=mytext, lang="en", slow=False)

    # Saving the converted audio in a mp3 file
    audio.save("example.mp3")

    # Playing the converted file
    # os.system("start example.mp3")
    st.write("""
    ### Hear the Summarized Text
    """)
    audio_file = open("example.mp3", "rb")
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format="audio/ogg")

else:
    st.info('Awaiting for Text file to be uploaded.')

#---------------------------------#