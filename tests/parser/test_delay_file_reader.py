"""
Test suite for the DelayFileReader class

Author: Tom Aston
"""

import pytest

from src.parser.delay_file_reader import DelayFileReader
from src.parser.enums import DelayFilter

from pathlib import Path


TEST_FILE_PATH = Path(__file__).parent.resolve()
MOCK_FILE_PATH = f"{TEST_FILE_PATH}/../files/mock_folder/mock_file_1.txt"

# Event Filters => ["All Events", "Arrival", "Departure", "Destination"]
# (event_filter, delay_filter, expected_length)
test_cases = [
    ("All Events", DelayFilter.FIFTEEN_PLUS, 2),
    ("All Events", DelayFilter.THREE_TO_FIFTEEN, 2),
    ("Arrival", DelayFilter.THREE_TO_FIFTEEN, 1),
]


class TestSuiteDelayFileReader:
    """
    TestSuiteDelayFileReader class tests the DelayFileReader class
    """

    @pytest.mark.parametrize("event_filter, delay_filter, expected_length", test_cases)
    def test_parse_train_delay_file(self, event_filter: str, delay_filter: DelayFilter, expected_length: int) -> None:
        """
        test_parse_train_delay_file tests the parse_train_delay_file method
        """
        delay_dataframe = DelayFileReader.parse_train_delay_file(MOCK_FILE_PATH, event_filter, delay_filter)

        assert len(delay_dataframe) == expected_length
