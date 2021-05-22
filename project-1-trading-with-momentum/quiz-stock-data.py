import quiz_tests
import pandas as pd
# import numpy as np

def csv_to_close(csv_filepath, field_names):
    """Reads in data from a csv file and produces a DataFrame with close data.
    
    Parameters
    ----------
    csv_filepath : str
        The name of the csv file to read
    field_names : list of str
        The field names of the field in the csv file

    Returns
    -------
    close : DataFrame
        Close prices for each ticker and date
    """
    
    # Completed: Implement Function
    ## Task 1: Read the CSV
    prices_df = pd.read_csv(csv_filepath, names=field_names)
    
    ## Task 2: Put in a DF with close data.
    close_prices = prices_df.pivot(index='date', columns='ticker', values='close')
    
    return close_prices


quiz_tests.test_csv_to_close(csv_to_close)

