import streamlit as st
from PIL import Image
import datetime
import pandas as pd
import matplotlib.pyplot as plt

st.title("サプーアプリ")
st.caption("これはサプーの動画用のテストアプリです")

image = Image.open("./data/タイトルなし.png")
st.image(image, width=200)
