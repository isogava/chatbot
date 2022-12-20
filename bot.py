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

name = name, name*2 
st.text(f'ようこそ！{name}さん！')
#st.text(f'こんばんは！{name}さん！')
