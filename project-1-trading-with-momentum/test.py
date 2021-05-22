import sys
import pandas as pd
import numpy as np
import helper
import project_helper
import project_tests


# ------------------------------------------------------------------
# Market Data
df = pd.read_csv('../../data/project_1/eod-quotemedia.csv', parse_dates=['date'], index_col=False)
close = df.reset_index().pivot(index='date', columns='ticker', values='adj_close')
print('Loaded Data')

# Resample Adjusted Prices
def resample_prices(close_prices, freq='M'):
  """
  Resample close prices for each ticker at specified frequency.
  
  Parameters
  ----------
  close_prices : DataFrame
      Close prices for each ticker and date
  freq : str
      What frequency to sample at
      For valid freq choices, see http://pandas.pydata.org/pandas-docs/stable/timeseries.html#offset-aliases
  
  Returns
  -------
  prices_resampled : DataFrame
      Resampled prices for each ticker and date
  """
  # TODO: Implement Function
  close = pd.DataFrame(close_prices.resample(freq).last())

  return close

project_tests.test_resample_prices(resample_prices)

# ------------------------------------------------------------------
# View Data

monthly_close = resample_prices(close)
project_helper.plot_resampled_prices(
  monthly_close.loc[:, apple_ticker],
  close.loc[:, apple_ticker],
  '{} Stock - Close Vs Monthly Close'.format(apple_ticker))

# ------------------------------------------------------------------
# Compute Log Returns

def compute_log_returns(prices):
  """
  Compute log returns for each ticker.
  
  Parameters
  ----------
  prices : DataFrame
    Prices for each ticker and date
  
  Returns
  -------
  log_returns : DataFrame
    Log returns for each ticker and date
  """
  # TODO: Implement Function
  
  return None

project_tests.test_compute_log_returns(compute_log_returns)