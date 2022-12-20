import streamlit as st

st.title('チャットボットのテスト')
st.caption('キャプション')

list = ['はじめまして！']
dict = {'こんにちは':'コンニチハ','おはよう':'早起きですね！',
        'こんばんは':'コンバンハ',
        'パイソン':'Pythonは、超人気のあるプログラミング言語です。\n https://ja.wikipedia.org/wiki/Python',
        'Python':'Pythonは、とっても人気のプログラミング言語ですよ。\n https://ja.wikipedia.org/wiki/Python',
        'iso9001':'こちらをご覧ください。\n https://gtc.co.jp/',
        'iso14001':'こちらをご覧ください。\n https://gtc.co.jp/',
        'iso22000':'こちらをご覧ください。\n https://gtc.co.jp/',
        'グローバルテクノ':'こちらをご覧ください。\n https://gtc.co.jp/',
        'ホームページ':'こちらをご覧ください。\n https://gtc.co.jp/',
        'セミナー':'こちらをご覧ください。\n https://gtc.co.jp/semn/',
        'iso27001':'こちらをご覧ください。\n https://gtc.co.jp/',
        'iso31000':'こちらをご覧ください。\n https://gtc.co.jp/',
        'iso45001':'こちらをご覧ください。\n https://gtc.co.jp/',
        'iso14971':'こちらをご覧ください。\n https://gtc.co.jp/',
        'iso13485':'こちらをご覧ください。\n https://gtc.co.jp/',
        'iatf16949':'こちらをご覧ください。\n https://gtc.co.jp/',
        'iso20000':'こちらをご覧ください。\n https://gtc.co.jp/',
        'はい':'ハイ'}
col1, col2 = st.columns(2)



if 'text_list' not in st.session_state:
  st.session_state["text_list"] = []
with col2:
  text = st.text_input("ご質問をどうぞ")
with col1:
        if st.text_input:
          if len(text) > 0:
            if text in dict:
              st.session_state["text_list"].append('あなた：' + text)
              st.session_state["text_list"].append('ボット：' + dict[text])
            else:
              st.session_state["text_list"].append('あなた：' + text)
              st.session_state["text_list"].append('ボット：' + text + "なんですね。")

        for output_text in st.session_state["text_list"]:
          st.write(output_text)
write('応答用の辞書は、まだこのくらいです。')
write(dict)
        
# 風船飛ばす
st.balloons()
