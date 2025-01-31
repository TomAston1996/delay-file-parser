"""
IProgressTracker is an interface for progress tracking.

Author: Tom Aston
"""

from abc import ABCMeta, abstractmethod


class IProgressTracker(metaclass=ABCMeta):
    """
    Interface for progress tracking.
    """

    @abstractmethod
    def update_progress(self, value: int, max_value: int) -> None:
        """
        update_progress updates the progress bar in the UI.
        """
        pass
