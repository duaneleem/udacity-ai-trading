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


