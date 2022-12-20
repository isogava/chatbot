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

c = 5
while c > 0:
        if name == "スズキ":
          st.text(f'ようこそ！{name}さん！')
          list.append(name)
          st.text(list)
        elif name in dict:
          st.text('私の辞書では、' + dict[name] + 'と返事をします。')
          list.append(name)
          st.text(list)
        else:
          if name == '':
            st.text('コメントをお願いします')
          else:
            st.text('何か別の言葉をお願いします')
        c = c - 1
st.text(list)
