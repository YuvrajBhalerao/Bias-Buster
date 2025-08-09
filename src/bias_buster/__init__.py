"""
Bias Buster: A package for detecting and suggesting fixes for bias in datasets.

This package provides a suite of tools to analyze a pandas DataFrame for common
sources of statistical bias, such as class imbalance, feature skewness, and
missing data. It then suggests appropriate data science techniques to mitigate
these issues.
"""

# Define the package version
__version__ = "0.1.0"

# Import key functions to make them available at the package level
from .data_handler import load_and_validate_dataset
from .detector import detect_biases
from .suggester import generate_suggestions

# You can also define what gets imported when a user does 'from bias_buster import *'
# This is generally good practice to control the package's public API.
__all__ = [
    "load_and_validate_dataset",
    "detect_biases",
    "generate_suggestions",
]
