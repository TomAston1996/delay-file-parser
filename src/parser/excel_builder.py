'''
ExcelBuilder class

Author: Tom Aston
'''
import time
import pandas as pd

from src.ui.iprogress_tracker import IProgressTracker

from .delay_file_reader import DelayFileReader
from .folder_scanner import FolderScanner


class ExcelBuilder:
    '''
    ExcelBuilder class builds the excel file from the pandas dataframes parsed from the delay files
    '''
    def __init__(
        self,
        delay_file_reader: DelayFileReader,
        folder_scanner: FolderScanner,
        folder_path: str,
        destination_path: str,
        event_filter: str = None,
        progress_tracker: IProgressTracker = None
        ) -> None:
        '''
        Constructor for ExcelBuilder class
        '''
        self.delay_file_reader = delay_file_reader
        self.folder_scanner = folder_scanner
        self.folder_path = folder_path
        self.destination_path = destination_path
        self.event_filter = event_filter
        self.progress_tracker = progress_tracker
        
        self.excel_dataframe: pd.DataFrame = None


    def build_excel_file(self) -> None:
        '''
        build_excel_file builds the excel file from the pandas dataframes parsed from the delay files
        '''
        files_to_parse = self.folder_scanner.get_list_of_files_in_folder(self.folder_path)
        
        if files_to_parse is None:
            return
        
        self.__build_dataframe_from_files(files_to_parse)
        self.__format_dataframe()
        
        self.excel_dataframe.to_excel(f'{self.destination_path}/results-{time.time()}.xlsx', index=False)


    def __build_dataframe_from_files(self, files_to_parse: list[str]) -> None:
        '''
        build_dataframe_from_files builds the dataframe from the files to parse
        '''
        total_number_files = len(files_to_parse)

        for i, file in enumerate(files_to_parse, 1):
            delay_dataframe = self.delay_file_reader.parse_train_delay_file(f"{self.folder_path}/{file}", self.event_filter)
            if delay_dataframe is None:
                continue
            
            if self.excel_dataframe is None:
                self.excel_dataframe = delay_dataframe
            else:
                self.excel_dataframe = pd.concat([self.excel_dataframe, delay_dataframe], ignore_index=True)

            self.progress_tracker.update_progress(i, total_number_files)


    def __format_dataframe(self) -> None:
        '''
        format_dataframe formats the excel dataframe
        '''
        if self.excel_dataframe is None:
            return

        self.excel_dataframe['PlannedTimestamp'] = pd.to_datetime(self.excel_dataframe['PlannedTimestamp'], dayfirst=True)

        self.excel_dataframe = self.excel_dataframe.sort_values(by=["CurrentTiploc", "PlannedTimestamp"], ascending=[True, True])
        self.excel_dataframe = self.excel_dataframe.reset_index(drop=True)