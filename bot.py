import streamlit as st

st.title('チャットボットのテスト')
st.caption('キャプション')

list = ['はじめまして！']
dict = {'こんにちは':'コンニチハ','おはよう':'早起きですね！',
        'こんばんは':'コンバンハ',
        'はい':'ハイ'}


@st.cache(allow_output_mutation=True)
def cache_lst():
    lst = []
    return lst

lst = cache_lst()
input = st.text_input("文字入力")

if input:
    lst.append(input)
st.table(lst)

# 風船飛ばす
st.balloons()
