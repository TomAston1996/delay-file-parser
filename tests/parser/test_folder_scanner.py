"""
Test suite for the FolderScanner class

Author: Tom Aston
"""

from pathlib import Path

from src.parser.folder_scanner import FolderScanner

TEST_FILE_PATH = Path(__file__).parent.resolve()
MOCK_DIR_PATH = f"{TEST_FILE_PATH}/../files/mock_folder/"


class TestSuiteFolderScanner:
    """
    TestSuiteFolderScanner class tests the FolderScanner class
    """

    def test_get_list_of_files_in_folder(self) -> None:
        """
        test_get_list_of_files_in_folder tests the get_list_of_files_in_folder method
        """
        files = FolderScanner.get_list_of_files_in_folder(MOCK_DIR_PATH)
        assert len(files) == 2

    def test_get_list_of_files_in_folder_folder_not_found(self) -> None:
        """
        test_get_list_of_files_in_folder_folder_not_found tests the get_list_of_files_in_folder method
        when the folder does not exist
        """
        files = FolderScanner.get_list_of_files_in_folder("non_existent_folder")
        assert files is None
