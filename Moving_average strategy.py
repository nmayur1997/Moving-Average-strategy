import yfinance as yf
import pandas as pd
import numpy as np

# Define stock and time period
Stock = "RELIANCE.NS"
data = yf.download(Stock, start="2021-01-01", end="2023-12-31")

# Prepare the data
T3 = pd.DataFrame({"Close": data["Close"]})
T3['Year'] = T3.index.year

# DataFrame to store results
T2 = pd.DataFrame(columns=["cumpnl_long", "cumpnl_short", "cumpnl", "SMA", "LMA", "Stock", "Year"])

# Loop through different years and moving average parameters
for z in range(2021, 2024):
    T = T3[T3.Year == z].dropna()
    for x in range(1, 35, 2):  # Short moving average window
        for y in range(x, 35, 2):  # Long moving average window
            SMA = x
            LMA = y

            # Calculate moving averages
            T['Short_average'] = T['Close'].rolling(window=SMA, min_periods=1).mean()
            T['Long_average'] = T['Close'].rolling(window=LMA, min_periods=1).mean()

            # Define entry and exit signals
            T['long_entry'] = T['Short_average'] > T['Long_average']
            T['long_exit'] = T['Short_average'] <= T['Long_average']
            T['positions_long'] = np.nan
            T.loc[T.long_entry, 'positions_long'] = 1
            T.loc[T.long_exit, 'positions_long'] = 0
            T['positions_long'] = T['positions_long'].fillna(method='ffill')

            T['short_entry'] = T['Short_average'] < T['Long_average']
            T['short_exit'] = T['Short_average'] >= T['Long_average']
            T['positions_short'] = np.nan
            T.loc[T.short_entry, 'positions_short'] = -1
            T.loc[T.short_exit, 'positions_short'] = 0
            T['positions_short'] = T['positions_short'].fillna(method='ffill')

            # Calculate P&L and cumulative P&L
            T['price_difference'] = T['Close'] - T['Close'].shift(1)
            T['pnllong'] = T['positions_long'].shift(1) * T['price_difference']
            T['pnlshort'] = T['positions_short'].shift(1) * T['price_difference']
            T['pnl'] = T['pnllong'] + T['pnlshort']
            T['cumpnl_long'] = T['pnllong'].cumsum()
            T['cumpnl_short'] = T['pnlshort'].cumsum()
            T['cumpnl'] = T['pnl'].cumsum()

            # Collect results for the current combination
            T1 = T[['cumpnl_short', 'cumpnl_long', 'cumpnl']].tail(1)
            T1['SMA'] = SMA
            T1['LMA'] = LMA
            T1['Stock'] = Stock
            T1['Year'] = z
            T2 = pd.concat([T2, T1], ignore_index=True)

# Display the results
print(T2)

# Optionally, save results to an Excel file
T2.to_excel("moving_average_strategy_results.xlsx", index=False)
