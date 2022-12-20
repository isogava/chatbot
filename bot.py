import streamlit as st

st.title('チャットボットのテスト')
st.caption('キャプション')

list = ['はじめまして！']
dict = {'こんにちは':'コンニチハ','おはよう':'早起きですね！',
        'こんばんは':'コンバンハ',
        'はい':'ハイ'}
col1, col2 = st.columns(2)



if 'text_list' not in st.session_state:
  st.session_state["text_list"] = []
with col2:
  text = st.text_input("ご質問をどうぞ")
with col1:
        if st.text_input:
          if len(text) > 0:
            st.session_state["text_list"].append('あなた：', text)
            st.session_state["text_list"].append('ボット：', text + "なんですね。")

        for output_text in st.session_state["text_list"]:
          st.write(output_text)

# 風船飛ばす
st.balloons()
