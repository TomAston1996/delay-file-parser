import tkinter as tk

from src.parser.delay_file_reader import DelayFileReader
from src.parser.folder_scanner import FolderScanner
from src.ui.app import App


def main():
    root = tk.Tk()
    App(root, DelayFileReader, FolderScanner)
    root.mainloop()


if __name__ == "__main__":
    main()
