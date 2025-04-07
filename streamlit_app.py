import streamlit as st
import pandas as pd
import numpy as np
import requests
import psycopg2

symbol = st.sidebar.text_input("Symbol", value="APPL", max_chars=5)
option = st.sidebar.selectbox("Which dashboard?",("chart","Pattern","Wallstreetbets"))

connection = psycopg2.connect(host=cocnfig.DB_HOST, database=config.DB_NAME, user=config.DB_USER, password=config.DB+PASS)

st.header(option)


if option == "Chart":
    st.subheader("Chart Dashboard")

if option == "Pattern":
    st.subheader("Pattern Dashboard")


if option == "Wallstreetbets":
    st.subheader("Wallstreetbets Dashboard")

    