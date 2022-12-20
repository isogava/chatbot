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
  st.text(f'ようこそ！{name}さん！')
elif name in dict:
  st.text(f'{name}さんですね！')
else:
  if name == '':
    st.text('コメントをお願いします')
  else:
    st.text('何か別の言葉をお願いします')
