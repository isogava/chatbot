import streamlit as st

st.title('チャットボットのテスト')
st.caption('キャプション')

#name = ""
#if name == "":
#  print('コメントよろしく')
#else:
#  st.text(f'ようこそ！{name}さん！')

list = ['はじめまして！']
dict = {'こんにちは':'コンニチハ','おはよう':'早起きですね！',
        'こんばんは':'コンバンハ',
        'はい':'ハイ'}
name = st.text_input('コメントをどうぞ！')

if name == "スズキ":
  st.text(f'ようこそ！{name}さん！')
  list = list.append(name)
elif name in dict:
  st.text('私の辞書では、' + dict[name] + 'と返事をします。')
  list = list.append(name)
else:
  if name == '':
    st.text('コメントをお願いします')
  else:
    st.text('何か別の言葉をお願いします')
st.text('もっと話して')

st.text(list)
