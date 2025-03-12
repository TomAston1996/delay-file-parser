"""
ProgressTracker class is responsible for updating the progress bar in the UI.

Author: Tom Aston
"""

import datetime
from tkinter import ttk

from src.ui.iprogress_tracker import IProgressTracker


class ProgressTracker(IProgressTracker):
    """
    ProgressTracker class is responsible for updating the progress bar in the UI.
    """

    def __init__(self, progress: ttk.Progressbar) -> None:
        """
        Constructor for ProgressTracker class
        """
        self.progress = progress
        self.progress["value"] = 0

    def update_progress(self, value: int, max_value: int) -> None:
        """
        update_progress updates the progress bar in the UI.
        """
        percentage = (value / max_value) * 100
        time_now = str(datetime.datetime.now())
        print(f"[{time_now}][INFO] ⏳ Progress Update: {percentage}% complete")
        progress_bar_value = min(round((value / max_value) * 100, 0), 100)
        self.progress["value"] = progress_bar_value
