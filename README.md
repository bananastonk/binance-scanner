# binance-scanner

## What is this?

This is a program which scans the Binance exchange for suitable trades based on given {$coin}USDT tickers.
- This program is built on websockets which are used to pull candlestick data from the Binance API
- The program analyzes the candlestick data and then alerts the user of suitable trades to take
- Such trade setups are determined by the use a price action strategy known as "The Strat", developed by Rob Smith.
- These trade setups are further filtered by configured parameters (minimum risk-to-reward ratio, full timeframe continuity)

## What is "The Strat"?
- As mentioned, "The Strat" is a price action trading strategy 
- The fundamental concept of this trading strategy is to do with the relative directions of the candlesticks. 
- This trading strategy is unlike many, in the sense that the relevant price levels (entries, exits & stops) are extremely well-defined. Prior to a typical entry, all such levels would already be defined relative to the candlesticks on which the trade setup is based on. Thus, this trading strategy is relatively easy to automate with code.

## How do I use this program?
- Download/clone this repo
- Enter "pip install -r requirements.txt" once you are in the root folder
- Change directory to /bot
- Edit the configuration file (config.py) as needed (see next header).
- Enter "py -3 main.py" for Windows, or "python3 main.py" for Linux.

## How do I configure the program?
- The path for the configuration file is binance-scanner/bot/config.py
- In the "coins" section, you can add as many key:value pairs as you like:
  - The key is the ticker symbol for your chosen coin
  - The value is a dictionary with chosen values for minor and major timeframes, timeframe continuity and the minimum risk-to-reward ratio.
- For each key:value pair, a separate thread will be spawned to handle the scanning. 

