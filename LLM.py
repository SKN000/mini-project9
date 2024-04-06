import streamlit as st
from transformers import pipeline

# 设置标题
st.title('English to Chinese')

# 创建文本输入框，用户可以输入要翻译的英文
text = st.text_area("Input your text in English:", value='', height=150, max_chars=None, key=None)

# 加载Hugging Face模型，这里使用"Helsinki-NLP/opus-mt-en-zh"模型进行翻译
translator = pipeline("translation_en_to_zh", model="Helsinki-NLP/opus-mt-en-zh")

# 当用户输入文本并点击翻译按钮时进行翻译
if st.button('Translate'):
    if text:
        # 执行翻译
        translation = translator(text, max_length=40)
        st.write(translation[0]['translation_text'])
    else:
        st.write('Text...')
