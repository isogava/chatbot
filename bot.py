import streamlit as st

st.title('チャットボットのテスト')
st.caption('キャプション')

name = ""
if name == "":

else:
  st.text(f'ようこそ！{name}さん！')


name = st.text_input('コメント')
print(name)
