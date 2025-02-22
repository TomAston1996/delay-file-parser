'''
This is the main file for the application. It creates the main window and starts the application.

Author: Tom Aston
'''

import tkinter as tk

from src.parser.delay_file_reader import DelayFileReader
from src.parser.folder_scanner import FolderScanner
from src.ui.app import App


def main() -> None:
    '''
    Application entry point
    '''
    root = tk.Tk()
    App(root, DelayFileReader, FolderScanner)
    root.mainloop()


if __name__ == "__main__":
    main()
