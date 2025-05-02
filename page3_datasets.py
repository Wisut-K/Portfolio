import streamlit as st
import yfinance as yf
import datetime
import os
import pandas as pd
import plotly.graph_objects as go

pd.options.plotting.backend = 'plotly'

st.set_page_config(page_title="The Ramsey Highlights", layout="wide")

#--------------------------------------------#
#--------------- OHCL Price  ----------------#
#--------------------------------------------#

st.markdown("# Download yfinance OHLC price")
# col_A, col_B = st.columns(2)
col_A, col_B = st.columns([0.6,1.0])
with col_A:


    col1, col2, col3 = st.columns(3)

    with col1:
        option_market = st.selectbox("Market",("SP 500","SET 50"))

    with col2:
        start_date = st.date_input("Start Date", datetime.date(2024, 1, 1))

    with col3:
        end_date = st.date_input("End Date", datetime.date(2025, 4, 25))


    st.markdown('#### Stock list')
    if option_market == "SP 500":
        df_symbols = pd.read_csv('Datasets/Symbol/symbols_sp500.csv', header=None).rename(columns={0: 'Symbol'})
        st.write(df_symbols)

    if option_market == "SET 50":  
        df_symbols = pd.read_csv('Datasets/Symbol/symbols_set50.csv', header=None).rename(columns={0: 'Symbol'})
        st.write(df_symbols)

    if st.button("Update", type="primary"):
        if option_market == "SP 500":
            with open('Datasets/Symbol/symbols_sp500.csv') as f:
                lines = f.read().splitlines()
                for symbol in lines:
                    ticker = yf.Ticker(symbol)
                    data = ticker.history(interval='1d', start=start_date, end=end_date)
                    data.to_csv("Datasets/SP500/{}.csv".format(symbol))
                    print(symbol)
                    print(data)
                st.success("Completed", icon="✅")

        if option_market == "SET 50":  
            with open('Datasets/Symbol/symbols_set50.csv') as f:
                lines = f.read().splitlines()
                for symbol in lines:
                    print(symbol)
                    ticker = yf.Ticker(symbol + ".BK")
                    data = ticker.history(interval='1d', start=start_date, end=end_date)
                    data.to_csv("Datasets/SET50/{}.csv".format(symbol))
                    print(symbol)
                    print(data)
                st.success("Completed",icon="✅")



with col_B:
#--------------------------------------------#
#--------------- Price Chart ----------------#
#--------------------------------------------#

    # st.markdown("# Price Chart")

    tuple_symbols = tuple(df_symbols['Symbol'])
    symbol = st.selectbox("Symbol",tuple_symbols ,index=0,placeholder="Select symbol...")

    if option_market == "SP 500":
        df_OHCL = pd.read_csv('Datasets/SP500/{}.csv'.format(symbol))

    if option_market == "SET 50":  
        df_OHCL = pd.read_csv('Datasets/SET50/{}.csv'.format(symbol))
        
    df_chart = pd.DataFrame()
    df_chart['time'] = df_OHCL['Date']
    df_chart['open'] = df_OHCL['Open']
    df_chart['high'] = df_OHCL['High']
    df_chart['low']  = df_OHCL['Low']
    df_chart['close'] = df_OHCL['Close']
    df_chart['volume'] = df_OHCL['Volume']

    st.markdown('#### Price chart')
    st.write(df_chart['close'].plot.line())