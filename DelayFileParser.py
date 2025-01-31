import tkinter as tk

from src.parser.delay_file_reader import DelayFileReader
from src.parser.folder_scanner import FolderScanner
from src.ui.app import App

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root, DelayFileReader, FolderScanner)
    root.mainloop()
