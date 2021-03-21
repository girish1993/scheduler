from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractFileOperations(ABC):

    @abstractmethod
    def read_csv_file(self):
        pass

    @abstractmethod
    def is_file_exists(self):
        pass

    @abstractmethod
    def write_output_shifts_to_file(self, shift_output):
        pass
