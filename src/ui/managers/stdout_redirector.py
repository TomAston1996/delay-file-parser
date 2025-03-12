"""
This module contains the StdoutRedirector class which is used to redirect the stdout to a text box.
Author: Tom Aston
"""

import tkinter as Tk


class StdoutRedirector:
    """Redirects stdout to a text box

    Args:
        object (object): Tkinter Text Box
    """

    def __init__(self, text_box: Tk.Text) -> None:
        self.text_box = text_box

    def write(self, string: str) -> None:
        """Writes to the text box

        Args:
            string (str): String to write
        """
        self.text_box.insert("end", string)

    def flush(self) -> None:
        """Flushes the text box"""
        pass
