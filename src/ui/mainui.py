"""
Main UI for the application
Author: Tom Aston
"""

import datetime
import sys
import tkinter as Tk
from tkinter import ttk

from src.parser.delay_file_reader import DelayFileReader
from src.parser.folder_scanner import FolderScanner

from src.ui.parser_frame import ParserFrame
from src.ui.managers.stdout_redirector import StdoutRedirector


class MainUI(Tk.Tk):
    """main UI for the application

    Args:
        Tk (_type_): Tkinter bases UI
    """

    def __init__(
        self,
        delay_file_reader: DelayFileReader,
        folder_scanner: FolderScanner,
        screenName: str | None = None,
        baseName: str | None = None,
        className: str | None = "Tk",
        useTk: bool = True,
        sync: bool = False,
        use: str | None = None,
    ) -> None:
        """constructor for the main UI

        Args:
            delay_file_reader (DelayFileReader): delay file reader class
            folder_scanner (FolderScanner): folder scanner class
            screenName (str | None, optional): screen name. Defaults to None.
            baseName (str | None, optional): base name. Defaults to None.
            className (str | None, optional): class name. Defaults to "Tk".
            useTk (bool, optional): Defaults to True.
            sync (bool, optional): Defaults to False.
            use (str | None, optional): Defaults to None.
        """
        super().__init__(screenName, baseName, className, useTk, sync, use)

        self.title("Train Delay File Parser")
        self.geometry("800x600")

        self.main_label_top = ttk.Label(self, text="🚆 Welcome to the DelayFileParser app... 🚆")
        self.main_label_top.pack(fill="x", pady=5)

        self.top_tab_area = ttk.Notebook(self)
        self.top_tab_area.pack(fill="x")
        self.top_tab_area.pack(fill="both", expand=True)

        self.parser_frame = ParserFrame(self.top_tab_area, delay_file_reader, folder_scanner)
        self.parser_frame.pack(fill="both", expand=True)
        self.top_tab_area.add(self.parser_frame, text="🔎 Parser")

        # Define redirector for stdout
        self.console_frame = Tk.Frame(self.top_tab_area)
        self.redirect_textbox = Tk.Text(self.console_frame, background="black", foreground="green")
        self.redirect_textbox.pack(fill="both", expand=True)
        self.stdredirect = StdoutRedirector(self.redirect_textbox)
        sys.stdout = self.stdredirect
        sys.stderr = self.stdredirect
        self.top_tab_area.add(self.console_frame, text="💻 Console")

    def start(self) -> None:
        """Starts the UI"""
        # user interface header
        print(r"""
______     _            ______ _ _     ______                        
|  _  \   | |           |  ___(_) |    | ___ \                       
| | | |___| | __ _ _   _| |_   _| | ___| |_/ /_ _ _ __ ___  ___ _ __ 
| | | / _ \ |/ _` | | | |  _| | | |/ _ \  __/ _` | '__/ __|/ _ \ '__|
| |/ /  __/ | (_| | |_| | |   | | |  __/ | | (_| | |  \__ \  __/ |   
|___/ \___|_|\__,_|\__, \_|   |_|_|\___\_|  \__,_|_|  |___/\___|_|   
                    __/ |                                            
                    |___/                                             
        """)
        print("\n****************************************************************")
        print("\n* Author: Tom Aston, 2024                                      *")
        print("\n* About: App for parsing train delay text files                *")
        print("\n****************************************************************\n")

        time_now = str(datetime.datetime.now())
        print(f"[{time_now}][INFO] ⚙️ DelayFileParser app started...")
        self.mainloop()
