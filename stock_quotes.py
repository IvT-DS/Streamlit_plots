# 1. Import libraries
import yfinance as yf
import streamlit as st
import pandas as pd

st.write(
    """
# WEB-приложение для отображения котировок компании Apple.

Показаны цена закрытия акции и объем продаж Apple!
"""
)

# 2. Define the ticker symbol.
ticker_symbol = "AAPL"

# 3. Get data on this ticker.
ticker_data = yf.Ticker(ticker_symbol)

# 4. get the historical prices for this ticker
ticker_df = ticker_data.history(period="1s", start="2000-1-01", end="2024-1-16")

# Index     Open    High    Low Close   Volume  Dividends   tock Splits
# Date
st.write("### График стоимости акций Apple на закрытии торговой сессии.")
st.line_chart(ticker_df["Close"])
st.write("### График объема торгов акциями Apple в течение торговой сессии.")
st.line_chart(ticker_df["Volume"])
