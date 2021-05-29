# AI for Trading | Week 1 | L6: Data Processing

## Using Time Stamps
- Bucket each timestamp
## Corporate Actions: Stock Splits
- Company events affecting stocks
- Stock Splits
  - https://youtu.be/S60WArbQK7k
  - Total Market Capitalization: the dollar value of a company's outstanding shares (Stock Price x Total # of shares outstanding
  - Why? More liquid
  - 3:30 Adjusted Price
- Dividends
  - https://youtu.be/OVZw9tci55w
  - Partial cash distribution of company earnings
  - To get dividend, shareholder must have purchased stock on X-dividend date
  - 2:15 Adjusted Price Factor: 1 + (D/S)
## Technical Indicators
- https://youtu.be/jo740Kq3YN4
- Indicators
- Simple Moving Average (Rolling Mean)
  - Trading strategy that looks for large deviations and generate trading signals based on this
  - Constant Threshold (when |price - average| exceeds x dollars)
    - Not recommended
  - Fraction Threshold
    - when (|price - average| / price)
    - exceeds x percent
  - Signals based on Bollinger Bands
    - 2:38 Standard deviation
    - Inflection points: when price is outside of bollinger bands several times
    - 4:09 Buy when price increases back towards the mean
    - Sell when price decreases back towards mean
## Missing Values
- https://youtu.be/XaMaVFUIc_I
- 0:15 Clumps: Holidays, Weekends, Market Closed
- 2:35 Time when market closes in the day to when it reopens the next day (postmarket->premarket)
- 3:49 Backfill Google's pre-IPO from IPO OHLC data, set volume to 0
- 4:30 Dell de-listed in 2013
  - Prefill with stock forward
## Trading Days
- The NYSE and NASDAQ average about 252 trading days a year. This is from 365.25(days on average per year) * 5/7(proportion work days per week) = 260.89 - 9(holidays) = 251.89 ~ 252.
## Survivor Bias
- The average return from Experiment A would indeed be higher than that from B. This is due to a phenomenon known as Survivor Bias
- https://youtu.be/39MeCCw5ndM
- 0:10 If I picked the stocks from 2005, that has filtered out the failed stocks.
- 0:38 I bought stocks available based on information in 2005
- 0:55 Creating signals based on historical prices.
## Fundamental Information
- Sales Per Share: Company sells a million smartphones for $100 each over the past 3 months, then its revenue is $100 times 1 million, or $100 million. If the company issued ten million shares, then its sales per share is $100 million divided by ten million, or $10 per share.
- Earnings Per Share: Company’s revenue minus its cost of sales
- Dividends Per Share: Company decides to return $10 million of its earnings to its shareholders. The dividend per share is then $10 million divided by 10 million shares, or $1 per share.
## Price to Earnings Ratio
- Stock’s current market price divided by its most recently reported earnings per share (EPS).
- Market price of a stock is based on both its current assets minus liabilities, but also estimates of the company’s future performance.
- Company may have low or negative earnings, but a high stock price. Investors expect potential for high earnings growth, based on the trajectory of past earnings growth. 
- One of many ways to take a snapshot of a company’s financial health.
## Exchange Traded Funds
- https://youtu.be/Zx7v5GCfpvI
- 0:50 Maintain broad portfolio of stocks
- S&P 500 (SPY)
- 4:13 ETF Compositional Data
- An ETF (Exchange Traded Fund) is made up of the same stocks as one of the many indices. However, it may not be exactly the same.
## Available Data
- Deven Desai, Product Lead at Planet
  - Geospatial Data
  - 5:21 Pugis? GIS? Arch GIS?
  - 9:50 NASA, ESA
  - 9:52: Open source Robosat




