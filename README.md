FOR EDUCATION PURPOSE ONLY

# Moving-Average-strategy

## Overview

This repository contains an implementation of a Moving Average Trading Strategy for the stock market, specifically applied to "RELIANCE.NS" using historical data from Yahoo Finance. The strategy uses short and long moving averages to generate trading signals, which are then analyzed to evaluate performance metrics such as cumulative profit and loss.

## Strategy Description

### Moving Average Crossover Strategy

The Moving Average Crossover Strategy involves two types of moving averages:
- **Short Moving Average (SMA)**: A moving average with a shorter window period.
- **Long Moving Average (LMA)**: A moving average with a longer window period.

**Trading Signals**:
- **Long Entry Signal**: Generated when the Short Moving Average crosses above the Long Moving Average.
- **Long Exit Signal**: Generated when the Short Moving Average crosses below the Long Moving Average.
- **Short Entry Signal**: Generated when the Short Moving Average crosses below the Long Moving Average.
- **Short Exit Signal**: Generated when the Short Moving Average crosses above the Long Moving Average.

**Profit and Loss Calculation**:
- **Long Positions**: Profit or loss is calculated based on the difference in closing prices while holding a long position.
- **Short Positions**: Profit or loss is calculated based on the difference in closing prices while holding a short position.
- **Cumulative Profit and Loss**: Aggregated profit and loss over the period of the strategy.

## Installation

To run the strategy and analyze the data, follow these steps:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/moving-average-strategy.git
    cd moving-average-strategy
    ```

2. **Install Required Libraries**:
    Ensure you have Python installed. Then, install the required libraries using pip:
    ```bash
    pip install yfinance pandas numpy openpyxl
    ```

## Usage

1. **Script Execution**:
    Run the script to fetch data, apply the strategy, and save the results:
    ```bash
    python moving_average_strategy.py
    ```

2. **Review Results**:
    The results will be saved in `moving_average_strategy_results.xlsx`. The Excel file will contain:
    - Cumulative profit and loss for long and short positions.
    - Parameters for short and long moving averages used in the strategy.

## Code Explanation

1. **Data Fetching**:
    - Historical stock data is fetched using `yfinance`.

2. **Strategy Implementation**:
    - Short and long moving averages are calculated.
    - Trading signals are generated based on crossovers of the moving averages.
    - Profit and loss are calculated for both long and short positions.

3. **Results Aggregation**:
    - Results are compiled and saved to an Excel file for further analysis.

## Results

The results include:
- **Cumulative Profit and Loss (Long and Short Positions)**: Track the performance of the strategy over the specified period.
- **SMA and LMA Parameters**: The moving average windows used in the strategy.
