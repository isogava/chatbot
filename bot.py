import streamlit as st

st.title('チャットボットのテスト')
st.caption('キャプション')

name = st.text_input('コメント')
print(name)

st.text('コメント {name} ありがとうございます！')
