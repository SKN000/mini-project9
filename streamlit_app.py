import streamlit as st
from transformers import pipeline

st.title('English to Chinese')
text = st.text_area("Input your text in English:", value='', height=150, max_chars=None, key=None)

translator = pipeline("translation_en_to_zh", model="Helsinki-NLP/opus-mt-en-zh")

if st.button('Translate'):
    if text:
        # 执行翻译
        translation = translator(text, max_length=40)
        st.write(translation[0]['translation_text'])
    else:
        st.write('Text...')
