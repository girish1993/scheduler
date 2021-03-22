from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractFileOperations(ABC):
    """
    Abstract class to declare the minimum functionality to be implemented when working with Files.
    """

    @abstractmethod
    def read_csv_file(self):
        """
        Method to read the csv file
        :return: content of the file as a Dataframe if successful, exception if not.
        :rtype: Dataframe
        """
        pass

    @abstractmethod
    def is_file_exists(self):
        """
        Method to check if the file exists
        :return: True if the input file exits. FileNotFoundError Otherwise
        :rtype: Bool
        """
        pass

    @abstractmethod
    def write_output_shifts_to_file(self, shift_output):
        """
        Writing the allocated shifts to a csv file
        :param shift_output: The dataframe containing the allocated shifts
        :type shift_output: Dataframe
        :return: None
        :rtype: None
        """
        pass
