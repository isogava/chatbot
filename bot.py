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
  list.append(name)
elif name in dict:
  st.text('私の辞書では、' + dict[name] + 'と返事をします。')
  list.append(name)
else:
  if len(name) > 0:
    list.append(name)
st.text(list)



while True:
        command = input('pybot')
        if 'こんにちは' in  command:
                print('hello')
        elif 'こんばんは' in command:
                print('good night')
        else:
                print('??')
        
