import streamlit as st

st.title('チャットボットのテスト')
st.caption('キャプション')

list = ['はじめまして！']
dict = {'こんにちは':'コンニチハ','おはよう':'早起きですね！',
        'こんばんは':'コンバンハ',
        'はい':'ハイ'}


text = st.text_input("ご質問をどうぞ")

if 'text_list' not in st.session_state:
  st.session_state["text_list"] = []

if len(st.text_input) > 0:
    st.session_state["text_list"].append(text)
    st.session_state["text_list"].append(text + "なんですね。")
        
for output_text in st.session_state["text_list"]:
  st.write(output_text)

# 風船飛ばす
st.balloons()
