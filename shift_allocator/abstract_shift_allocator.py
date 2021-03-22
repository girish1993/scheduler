from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractShiftAllocator(ABC):
    """
    Abstract Shift Allocator method that specifies the minimum mandatory actions for shift allocation
    """

    @abstractmethod
    def check_allocation(self):
        """
        Method to check for allocation of a shift
        :return: None
        :rtype: None
        """
        pass

    @abstractmethod
    def perform_allocation(self, shift, partition):
        """
        Method to perform allocation for the given shift and partition
        :param shift: The time indicies of time column for which there should be a shift
        :type shift: tuple
        :param partition: The demand for the corresponding shifts
        :type partition: tuple
        :return:None
        :rtype:None
        """
        pass
