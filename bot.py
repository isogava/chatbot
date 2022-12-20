import streamlit as st

st.title('チャットボットのテスト')
st.caption('キャプション')

name = st.text_input('コメント')
print(name)


name2 = st.text_input('お返事')
print(name2)
