import streamlit as st
import yfinance as yf
import datetime
import os
import pandas as pd
import plotly.graph_objects as go
# from lightweight_charts import Chart
import json

# import lightweight-charts

#--------------------------------------------#
#--------------- OHCL Price  ----------------#
#--------------------------------------------#

st.markdown("# Download yfinance OHLC price")

col1, col2, col3 = st.columns(3)

with col1:
    option_market = st.selectbox("Market: ",("SP 500","SET 50"))

with col2:
    start_date = st.date_input("Start Date", datetime.date(2024, 1, 1))

with col3:
    end_date = st.date_input("End Date", datetime.date(2025, 4, 25))


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



if option_market == "SP 500":
    df_symbols = pd.read_csv('Datasets/Symbol/symbols_sp500.csv', header=None).rename(columns={0: 'Symbol'})
    st.write(df_symbols)

if option_market == "SET 50":  
    df_symbols = pd.read_csv('Datasets/Symbol/symbols_set50.csv', header=None).rename(columns={0: 'Symbol'})
    st.write(df_symbols)

#--------------------------------------------#
#--------------- Price Chart ----------------#
#--------------------------------------------#

st.markdown("# Price Chart")

if option_market == "SP 500":
    symbol = st.text_input("Symbol", "AAPL")
    df_OHCL = pd.read_csv('Datasets/SP500/{}.csv'.format(symbol))
    # st.write(df_OHCL)

if option_market == "SET 50":  
    symbol = st.text_input("Symbol", "AOT")
    df_OHCL = pd.read_csv('Datasets/SET50/{}.csv'.format(symbol))
    # st.write(df_OHCL)

df_chart = pd.DataFrame()
df_chart['time'] = df_OHCL['Date']  #.dt.strftime('%Y-%m-%d')
df_chart['open'] = df_OHCL['Open']
df_chart['high'] = df_OHCL['High']
df_chart['low']  = df_OHCL['Low']
df_chart['close'] = df_OHCL['Close']
df_chart['volume'] = df_OHCL['Volume']
st.write(df_chart)

# if st.button("Display", type="primary"):
#     candlestick = go.Candlestick(x=df_OHCL['Date'],open=df_OHCL['Open'],high=df_OHCL['High'],low=df_OHCL['Low'],close=df_OHCL['Close'])
#     fig = go.Figure(data=[candlestick])
#     fig.show()

# if st.button("Display Chart", type="primary"):



# chart = Chart()
# chart.set(df_chart)
# chart.show(block=True)