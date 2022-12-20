import streamlit as st

st.title('チャットボットのテスト')
st.caption('キャプション')

#name = ""
#if name == "":
#  print('コメントよろしく')
#else:
#  st.text(f'ようこそ！{name}さん！')

dict = {'こんにちは':'コンニチハ', 'こんばんは':'コンバンハ', 'はい':'ハイ'}
name = st.text_input('コメントをどうぞ！')

if name == "aaa":
  name = name, name*2 
  st.text(f'ようこそ！{name}さん！')
elif name in dict:
  st.text(f'{name}さんですね！')
else:
  st.text('何か別の言葉をお願いします')
