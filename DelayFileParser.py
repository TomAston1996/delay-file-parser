"""
This is the main file for the application. It creates the main window and starts the application.

Author: Tom Aston
"""

from src.parser.delay_file_reader import DelayFileReader
from src.parser.folder_scanner import FolderScanner
from src.ui.mainui import MainUI


def main() -> None:
    """
    Application entry point
    """
    main_ui = MainUI(
        delay_file_reader=DelayFileReader,
        folder_scanner=FolderScanner,
        screenName="Train Delay File Parser",
        baseName="Train Delay File Parser",
    )
    main_ui.start()


if __name__ == "__main__":
    main()
