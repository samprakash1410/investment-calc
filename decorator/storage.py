"""This module has code for decorators
"""
from persistences.csv_files import write_result

def store_in_csv(func):
    """
    This decorater writes the results to csv file
    """
    def store_results(*args, **kwargs):
        write_result(*args, **kwargs)
        func(*args, **kwargs)
    return store_results