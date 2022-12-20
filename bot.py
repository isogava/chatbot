import streamlit as st

st.title('チャットボットのテスト')
st.caption('キャプション')

#name = ""
#if name == "":
#  print('コメントよろしく')
#else:
#  st.text(f'ようこそ！{name}さん！')


name = st.text_input('コメント')
st.text(f'ようこそ！{name}さん！')

message = 'Hello Python'

for ch in message:
    print(ch)
