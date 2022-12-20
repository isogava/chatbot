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

col1, col2 = st.columns(2)

with col2:
  if st.text_input:
    st.session_state["text_list"].append(text)
with col1:
  if st.text_input:
    st.write(text,"desu")
      
for output_text in st.session_state["text_list"]:
  st.write('<span style="color:red;background:pink">', output_text, '</span>')

# 風船飛ばす
st.balloons()
