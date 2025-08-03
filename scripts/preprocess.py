# scripts/preprocess.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load raw data
def load_data(file_path):
    df = pd.read_csv(file_path, parse_dates=['Date'], dayfirst=True)
    df.sort_values('Date', inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df

# Preprocess: clean, set datetime, calculate log returns
def preprocess_data(df):
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
    df = df.dropna()

    df['Log_Return'] = (df['Price']).apply(lambda x: float(x)).apply(np.log).diff()
    return df

# Plot price and log return trends
def plot_time_series(df, out_dir="reports/figures"):
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    plt.figure(figsize=(14, 5))
    plt.plot(df['Date'], df['Price'])
    plt.title('Brent Oil Price Over Time')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.savefig(f"{out_dir}/brent_price_trend.png")

    plt.figure(figsize=(14, 5))
    plt.plot(df['Date'], df['Log_Return'])
    plt.title('Log Returns of Brent Oil Prices')
    plt.xlabel('Date')
    plt.ylabel('Log Return')
    plt.savefig(f"{out_dir}/log_returns.png")


if __name__ == "__main__":
    import numpy as np

    raw_path="data/BrentOilPrices.csv"
    output_path = "data/processed_prices.csv"

    print("[INFO] Loading raw data...")
    df_raw = load_data(raw_path)

    print("[INFO] Preprocessing...")
    df_processed = preprocess_data(df_raw)

    print("[INFO] Saving processed data...")
    df_processed.to_csv(output_path, index=False)

    print("[INFO] Plotting figures...")
    plot_time_series(df_processed)

