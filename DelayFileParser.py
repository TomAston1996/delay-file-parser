from src.parser.delay_file_reader import DelayFileReader
from src.parser.folder_scanner import FolderScanner
from src.ui.app import App

import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root, DelayFileReader, FolderScanner)
    root.mainloop()
