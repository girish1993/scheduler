from file_operations.abstract_file_operations import AbstractFileOperations
import os
from pathlib import Path
import pandas as pd
import logging as LOGGER


class FileOperations(AbstractFileOperations):
    """
    A class to implement and perform all operations in relation to a file. The main operations include, reading the
    contents of the file, checking for the file's existence and writing to a file.
    """

    def __init__(self):
        """
        Creating a constructor of the class File Operations
        """
        self.input_dir_name = os.path.dirname("data/input/")
        self.output_dir_name = os.path.dirname("data/output/")
        self.input_file_path = os.path.join(self.input_dir_name, "Barista_needed.csv")
        self.output_file_path = os.path.join(self.output_dir_name, "Barista_shifts_alloted.csv")

    def get_input_file_path(self):
        """
        Getter of the input file path
        :return: input_file_path
        :rtype: str
        """
        return self.input_file_path

    def get_output_file_path(self):
        """
        Getter of output file path
        :return: output_file_path
        :rtype: str
        """
        return self.output_file_path

    def is_file_exists(self):
        """
        Method to check if input file path exists
        :return: True if exists, FileNotFoundError Exception if it doesn't.
        :rtype: bool
        """
        try:
            file_path = Path(self.get_input_file_path())
            if file_path.exists():
                return True
            else:
                raise FileNotFoundError("The path of the input file is not valid.")
        except Exception:
            raise Exception("There was an error while checking for the existence of the file")

    def read_csv_file(self):
        """
        Method to read the csv file contents as a pandas dataframe
        :return: data
        :rtype: dataframe
        """
        try:
            if self.is_file_exists():
                LOGGER.info("Reading the csv file")
                return pd.read_csv(self.get_input_file_path())
        except FileNotFoundError:
            LOGGER.error("Cannot read csv file as the provided path was invalid")

    def write_output_shifts_to_file(self, output_shifts):
        """
        Writing the contents of the shifts to the output file
        :param output_shifts: The ordered shift allocation data
        :type output_shifts: dataframe
        :return: None
        :rtype: None
        """
        output_shifts.to_csv(self.get_output_file_path(), index=False)
