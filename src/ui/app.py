"""
This module contains the App class which is the main class for the GUI

Author: Tom Aston
"""

import threading
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

from src.ui.progress_tracker import ProgressTracker
from src.parser.delay_file_reader import DelayFileReader
from src.parser.excel_builder import ExcelBuilder
from src.parser.folder_scanner import FolderScanner
from src.parser.enums import DelayFilter


class App:
    """
    App class is the main class for the GUI
    """

    def __init__(
        self,
        root: tk.Tk,
        delay_file_reader: DelayFileReader,
        folder_scanner: FolderScanner,
    ) -> None:
        """
        Constructor for App class
        """
        self.delay_file_reader = delay_file_reader
        self.folder_scanner = folder_scanner

        self.root = root
        self.root.title("Train Delay File Parser")
        self.root.geometry("600x450")  # Width x Height

        # Prevent resizing (optional)
        # self.root.resizable(False, False)

        # Folder paths
        self.search_folder_path = tk.StringVar()
        self.destination_folder_path = tk.StringVar()

        # Event Dropdown Filter
        self.selected_event_filter = tk.StringVar()
        self.event_filter_label = tk.Label(root, text="Select Event Filter:")
        self.event_filter_label.pack(pady=5)

        self.event_filter_options = ["All Events", "Arrival", "Departure", "Destination"]
        self.event_filter_dropdown = ttk.Combobox(
            root,
            values=self.event_filter_options,
            textvariable=self.selected_event_filter,
            state="readonly",
        )
        self.event_filter_dropdown.pack(pady=5)
        self.event_filter_dropdown.current(0)

        # DelayDropdown Filter
        self.delay_filter_map = {
            "15mins+": DelayFilter.FIFTEEN_PLUS,
            "3-15mins": DelayFilter.THREE_TO_FIFTEEN
        }
        self.selected_delay_filter = tk.StringVar()
        self.delay_filter_label = tk.Label(root, text="Select Delay Filter:")
        self.delay_filter_label.pack(pady=5)

        self.delay_filter_options = list(self.delay_filter_map.keys())
        self.delay_filter_dropdown = ttk.Combobox(
            root,
            values=self.delay_filter_options,
            textvariable=self.selected_delay_filter,
            state="readonly",
        )
        self.delay_filter_dropdown.pack(pady=5)
        self.delay_filter_dropdown.current(0)

        # Train Delay Folder Selection
        self.folder1_button = tk.Button(
            root,
            text="Select Train Delay Directory",
            command=self.select_train_delay_folder,
        )
        self.folder1_button.pack(pady=5)
        self.folder1_label = tk.Label(root, textvariable=self.search_folder_path, wraplength=400)
        self.folder1_label.pack(pady=5)

        # Destination Folder Selection
        self.folder2_button = tk.Button(
            root,
            text="Select Destination Directory",
            command=self.select_destination_folder,
        )
        self.folder2_button.pack(pady=5)
        self.folder2_label = tk.Label(root, textvariable=self.destination_folder_path, wraplength=400)
        self.folder2_label.pack(pady=5)

        # Action Button
        self.action_button = tk.Button(root, text="Run", command=self.run, bg="green", fg="white")
        self.action_button.pack(pady=10)

        # Progress Bar
        self.progress = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
        self.progress.pack(pady=10)

        self.__configure_styling()

    def __configure_styling(self) -> None:
        """
        Configure the styling of the GUI
        """

        style = ttk.Style()

        # Change the background color of the Combobox dropdown and field
        style.configure("TCombobox", fieldbackground="#444746", background="#444746")

        self.root.configure(bg="#202124")
        self.event_filter_label.configure(bg="#202124", fg="white", pady=5)
        self.event_filter_dropdown.configure(style="TCombobox")

        self.delay_filter_label.configure(bg="#202124", fg="white", pady=5)
        self.delay_filter_dropdown.configure(style="TCombobox")

        self.folder1_button.configure(bg="#444746", fg="white")
        self.folder1_label.configure(bg="#202124", fg="white")

        self.folder2_button.configure(bg="#444746", fg="white")
        self.folder2_label.configure(bg="#202124", fg="white")

        self.action_button.configure(bg="#3f4542")

    def select_train_delay_folder(self) -> None:
        """
        Select the folder where the train delay files are located
        """
        folder_path = filedialog.askdirectory(title="Select Train Delay Directory")
        if folder_path:
            self.search_folder_path.set(folder_path)

    def select_destination_folder(self) -> None:
        """
        Select the folder where the excel file will be saved
        """
        folder_path = filedialog.askdirectory(title="Select Destination Directory")
        if folder_path:
            self.destination_folder_path.set(folder_path)

    def run(self) -> None:
        """
        Run the process to build the excel file
        """
        print(f"Train Delay Directory: {self.search_folder_path.get()}")
        print(f"Destination Directory: {self.destination_folder_path.get()}")

        if not self.search_folder_path.get() or not self.destination_folder_path.get():
            messagebox.showwarning("Warning", "Please select both folders before proceeding.")
            return

        progress_tracker = ProgressTracker(self.progress)

        excel_builder = ExcelBuilder(
            delay_file_reader=self.delay_file_reader,
            folder_scanner=self.folder_scanner,
            folder_path=self.search_folder_path.get(),
            destination_path=self.destination_folder_path.get(),
            event_filter=self.selected_event_filter.get(),
            progress_tracker=progress_tracker,
            delay_filter=self.delay_filter_map[self.selected_delay_filter.get()],
        )

        thread = threading.Thread(target=self.run_excel_bulder, args=(excel_builder, progress_tracker))
        thread.start()

    def run_excel_bulder(self, excel_builder: ExcelBuilder, progress_tracker: ProgressTracker) -> None:
        """
        Run the excel builder process
        """
        excel_builder.build_excel_file()

        self.root.after(
            0,
            lambda: messagebox.showinfo(
                "Action Completed",
                f"Processing complete!\n\nResult in: {self.search_folder_path.get()}\n",
            ),
        )
        self.root.after(0, lambda: progress_tracker.update_progress(100, 100))


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
