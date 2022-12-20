import streamlit as st

st.title('チャットボットのテスト')
st.caption('キャプション')

list = ['はじめまして！']
dict = {'こんにちは':'コンニチハ','おはよう':'早起きですね！',
        'こんばんは':'コンバンハ',
        'はい':'ハイ'}


text = st.text_input("表示したい単語を入力してください")

if 'text_list' not in st.session_state:
  st.session_state["text_list"] = []

col1, col2 = st.columns(2)

with col1:
  if st.button("追加", key=2):
    st.session_state["text_list"].append(text)

with col2:
  if st.button("削除", key=3): 
    st.session_state["text_list"].remove(text)
      
for output_text in st.session_state["text_list"]:
  st.write("", output_text)

# 風船飛ばす
st.balloons()
