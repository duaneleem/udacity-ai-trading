


import pandas as pd

close = pd.DataFrame(
    {
        'ABC': [1, 5, 3, 6, 2],
        'EFG': [12, 51, 43, 56, 22],
        'XYZ': [35, 36, 36, 36, 37],},
    pd.date_range('10/01/2018', periods=5, freq='D'))
close


# Using the returns formula on the closing prices for the ticker "ABC" should give us `[(5-1)/1, (3-5)/5, (6-3)/3, (2-6)/6]` or `[4, -0.4, 1, -0.66]`. To calculate this for the whole DataFrame, we'll use the [DataFrame.shift](https://pandas.pydata.org/pandas-docs/version/0.21/generated/pandas.DataFrame.shift.html) function.

# This function allows us to shift the rows of data. For example, the following shifts the rows in `close` two days back.
close.shift(2)


# The data for the row "2018-10-03" contains data that is two days in the past. You'll also notice the "NaN" values for "2018-10-01" and "2018-10-02". Since there's not data two days in the past for these dates, it returns a "NaN" value.

# Use this function, you can also shift in the future using a negative number. Let's shift one day in the future.
close.shift(-1)


# ----------------------------------------------------------------------------
## Quiz
# Using what you know about the [DataFrame.shift](https://pandas.pydata.org/pandas-docs/version/0.21/generated/pandas.DataFrame.shift.html) function, implement the function.

# Once you successfully implemented the quiz, you can can continue to the next concept in the classroom.
import quiz_tests


def calculate_returns(close):
    """
    Compute returns for each ticker and date in close.
    
    Parameters
    ----------
    close : DataFrame
        Close prices for each ticker and date
    
    Returns
    -------
    returns : DataFrame
        Returns for each ticker and date
    """
    # TODO: Implement Function
    return (close - close.shift(1))/close.shift(1)


quiz_tests.test_calculate_returns(calculate_returns)
