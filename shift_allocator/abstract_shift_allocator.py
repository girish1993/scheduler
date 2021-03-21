from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractShiftAllocator(ABC):

    @abstractmethod
    def check_allocation(self):
        pass

    @abstractmethod
    def perform_allocation(self, shift, partition):
        pass
