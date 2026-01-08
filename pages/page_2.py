import streamlit as st
import datetime

name = st.text_input("名前")
address = st.text_input("住所")

mali_subscribe = st.checkbox("メールマガジンを購読する")

height = st.slider("身長", min_value=110, max_value=210)

start_date = st.date_input("開始日", datetime.date(2024, 1, 1))

color = st.color_picker("テーマカラー", "#00f900")

age_category = st.radio("年齢層", ("子ども(18才未満)", "大人(18歳以上)"))

hobby = st.multiselect("趣味", ("スポーツ", "プログラミング", "読書", "釣り"))

submit_btn = st.button("送信")
cancel_btn = st.button("キャンセル")
print(f"submit_btn:{submit_btn}")
print(f"cancel_btn:{cancel_btn}")

if submit_btn:
    st.text(f"ようこそ!{name}さん!{address}に書類を送りました!")
    st.text(f"年齢層:{age_category}")
    st.text(f'趣味:{",".join(hobby)}')
