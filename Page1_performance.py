import streamlit as st


st.markdown("# P.1 - Dashboard")
st.sidebar.markdown("# Page 1 - Dashboard")

# Side Bar
option = st.sidebar.selectbox("Dashboard",("chart","Pattern","Wallstreetbets"))
st.header(option)
if option == "Chart":           st.subheader("Chart Dashboard")
if option == "Pattern":         st.subheader("Pattern Dashboard")
if option == "Wallstreetbets":  st.subheader("Wallstreetbets Dashboard")

symbol = st.sidebar.text_input("Symbol", value="APPL", max_chars=5)

