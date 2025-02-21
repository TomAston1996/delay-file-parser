"""
DelayFileReader class

Author: Tom Aston
"""

import pandas as pd

from .enums import DelayFilter


class DelayFileReader:
    """
    DelayFileReader class reads the delay file from the path given and returns the pandas dataframe
    with only delays greater than 15 minutes
    """

    @staticmethod
    def parse_train_delay_file(path: str, event_filter: str = None, delay_filter: DelayFilter = DelayFilter.FIFTEEN_PLUS) -> pd.DataFrame:
        """
        parse_train_delay_file parses the delay file from the path given and returns the pandas dataframe
        """
        delay_dataframe = DelayFileReader.__read_file(path)
        if delay_dataframe is None:
            return None

        delay_dataframe = DelayFileReader.__apply_delay_filter(delay_dataframe, delay_filter)

        delay_dataframe = DelayFileReader.__filter_by_event_type(delay_dataframe, event_filter)

        return delay_dataframe

    @staticmethod
    def __read_file(path: str) -> pd.DataFrame:
        """
        read_file reads the delay file from the path given and returns the pandas dataframe
        """
        try:
            delay_dataframe = pd.read_csv(path, sep="\t")
            return delay_dataframe
        except FileNotFoundError:
            print(f"File not found at {path}")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    @staticmethod
    def __apply_delay_filter(
        delay_dataframe: pd.DataFrame,
        delay_filter: DelayFilter = DelayFilter.FIFTEEN_PLUS,
    ) -> pd.DataFrame:
        """
        filter_delay_greater_than_15_minutes filters the delays greater than 15 minutes
        """
        if "Variation" not in delay_dataframe.columns:
            print("Variation column not found in the delay file")
            return None
        
        if delay_filter == DelayFilter.FIFTEEN_PLUS:
            delay_dataframe = delay_dataframe[delay_dataframe["Variation"] >= 15].reset_index(drop=True)
        elif delay_filter == DelayFilter.THREE_TO_FIFTEEN:
            delay_dataframe = delay_dataframe[
                (delay_dataframe["Variation"] >= 3) & (delay_dataframe["Variation"] < 15)
            ].reset_index(drop=True)
        
        return delay_dataframe

    @staticmethod
    def __filter_by_event_type(delay_dataframe: pd.DataFrame, event_filter: str) -> pd.DataFrame:
        """
        filter_by_event_type filters the delays by the event type
        """
        if event_filter == "All Events" or not event_filter:
            return delay_dataframe

        # //print(f"Filtering by event type: {event_filter}")

        return delay_dataframe[delay_dataframe["PlannedEvent"] == event_filter].reset_index(drop=True)
