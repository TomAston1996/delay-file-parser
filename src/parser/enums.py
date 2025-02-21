"""
ExcelBuilder class

Author: Tom Aston
"""

from enum import Enum

class DelayFilter(Enum):
    FIFTEEN_PLUS = '15mins+'
    THREE_TO_FIFTEEN = '3-15mins'