###
## Module for basic statistics
###

## Here I need functions to take in data
## and do the following:
##
## 1. Calculate mean. Calculate median. Calculate 
##    standard deviation.
##
## 2. Display the result with a nice print statement.
##
## 3. Plot a histogram of the data, with the mean and median 
##    marked on the plot. This should be part of a new Python
##    file in the package, called graphics.py.
##
## 4. Remember to provide a mechanism for checking that the input
##    is a numpy array or a list (if a list, you must convert it
##    to a numpy array).
##
## 5. Also, do something and/or throw an exception/message if the
##    numpy and matplotlib packages are not installed.

import numpy as np

def calculate_statistics(data):
    if not isinstance(data, (np.ndarray, list)):
        raise ValueError("Input must be a numpy array or a list")
    if isinstance(data, list):
        data = data
    
    mean = np.mean(data)
    median = np.median(data)
    std_dev = np.std(data)
    
    return mean, median, std_dev

def display_statistics(mean, median, std_dev):
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Standard Deviation: {std_dev}")