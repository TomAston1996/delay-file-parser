'''
FolderScanner class

Author: Tom Aston
'''
import os

class FolderScanner:
    '''
    FolderScanner class scans the folder given and returns the list of files in the folder
    '''
    @staticmethod
    def get_list_of_files_in_folder(folder_path: str) -> list[str]:
        '''
        get_list_of_files_in_folder returns the list of files in the folder
        '''
        try:
            files = os.listdir(folder_path)
            return [file for file in files if file.endswith('.txt')]
        except FileNotFoundError:
            print(f"Folder not found at {folder_path}")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None