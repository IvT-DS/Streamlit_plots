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

ticker_list = ["AAPL", "GOOGL", "MSFT", "AMZN", "META"]
ticker_dict = {
    "AAPL": "Apple Inc.",
    "GOOGL": "Alphabet Inc",
    "MSFT": "Microsoft Corporation",
    "AMZN": "Amazon.com Inc.",
    "META": "Meta Platforms Inc.",
}
selected_ticker = st.selectbox("Выберите тикер", ticker_list)

# 3. Get data on this ticker.
ticker_data = yf.Ticker(selected_ticker)

# 4. get the historical prices for this ticker
start_date = st.date_input(
    "Выберите начальную дату",
    value=pd.to_datetime("2000-01-01"),
    min_value=pd.to_datetime("1900-01-01"),
    max_value=pd.to_datetime("2100-12-31"),
)

end_date = st.date_input(
    "Выберите конечную дату",
    value=pd.to_datetime("2024-01-16"),
    min_value=pd.to_datetime("1900-01-01"),
    max_value=pd.to_datetime("2100-12-31"),
)


ticker_df = ticker_data.history(period="1s", start=start_date, end=end_date)

# Index     Open    High    Low Close   Volume  Dividends   tock Splits
# Date
st.write(
    f"### График стоимости акций {ticker_dict.get(selected_ticker, 'No Data')} на закрытии торговой сессии."
)
st.line_chart(ticker_df["Close"])
st.write(
    f"### График объема торгов акциями {ticker_dict.get(selected_ticker, 'No Data')} в течение торговой сессии."
)
st.line_chart(ticker_df["Volume"])
