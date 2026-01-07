import streamlit as st
from PIL import Image
import datetime
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./data/data.csv", index_col="月")
st.line_chart(df)
st.bar_chart(df["2024年"])
