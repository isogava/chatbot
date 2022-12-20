import streamlit as st

st.title('チャットボットのテスト')
st.caption('キャプション')

#name = ""
#if name == "":
#  print('コメントよろしく')
#else:
#  st.text(f'ようこそ！{name}さん！')

counter = 5
while counter > 0:
    print(counter)
    name = st.text_input('コメント')
    st.text(f'ようこそ！{name}さん！')
    counter = counter -1

st.text(f'こんばんは！{name}さん！')
