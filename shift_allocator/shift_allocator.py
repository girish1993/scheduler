from shift_allocator.utility import ShiftUtility
from shift_allocator.abstract_shift_allocator import AbstractShiftAllocator
from statistics import mode
from statistics import mean
import math

BARISTAS_NEEDED = "Total number of Baristas needed"


class ShiftAllocator(AbstractShiftAllocator):

    def __init__(self, data):
        self.data = data
        self.two_shift_partitions = [(7, 3), (6, 4), (5, 5)]
        self.three_shift_partitions = [(3, 3, 4), (3, 4, 3), (4, 3, 3)]
        self.demand_data = list(self.get_data()[BARISTAS_NEEDED])
        self.two_shift_dicts = {}
        self.three_shift_dicts = {}
        self.allocated_shifts = {}

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_two_shift_partitions(self):
        return self.two_shift_partitions

    def get_three_shift_partitions(self):
        return self.three_shift_partitions

    def get_demand_data(self):
        return self.demand_data

    def get_two_shift_dicts(self):
        return self.two_shift_dicts

    def get_three_shift_dicts(self):
        return self.three_shift_dicts

    def get_allocated_shifts(self):
        return self.allocated_shifts

    def add_shifts(self, index, no_of_baristas):
        if index not in self.get_allocated_shifts():
            self.allocated_shifts[index] = no_of_baristas

    def set_two_shift_dicts(self, key):
        if key not in self.two_shift_dicts:
            self.two_shift_dicts[key] = (
                self.get_demand_data()[:key[0]], self.get_demand_data()[key[0]:key[0] + key[1]])

    def set_three_shift_dicts(self, key):
        if key not in self.three_shift_dicts:
            self.three_shift_dicts[key] = (self.get_demand_data()[:key[0]],
                                           self.get_demand_data()[key[0]:key[1] + key[0]],
                                           self.get_demand_data()[key[1] + key[0]:key[1] + key[0] + key[2]])

    def create_two_shift_partitions(self):
        for each_two_shift in self.get_two_shift_partitions():
            if each_two_shift[0] != each_two_shift[1]:
                print("creating partition for {}".format(each_two_shift))
                self.set_two_shift_dicts(each_two_shift)
                swap_list = list(each_two_shift)
                swap_list[0], swap_list[1] = swap_list[1], swap_list[0]
                self.set_two_shift_dicts(tuple(swap_list))
            else:
                self.set_two_shift_dicts(each_two_shift)

    def create_three_shift_partitions(self):
        for each_three_shift in self.get_three_shift_partitions():
            print("creating partition for {}".format(each_three_shift))
            self.set_three_shift_dicts(each_three_shift)

    def check_two_shift_feasibility(self):
        for shift, partition in self.get_two_shift_dicts().items():
            if ShiftUtility().check_for_optimum_result_two_shifts(shift, partition):
                self.perform_allocation(shift, partition)

    def check_three_shift_feasibility(self):
        for shift, partition in self.get_three_shift_dicts().items():
            if ShiftUtility().check_for_optimum_result_three_shifts(shift, partition):
                self.perform_allocation(shift, partition)

    def check_allocation(self):
        self.create_two_shift_partitions()
        self.create_three_shift_partitions()
        if not self.check_two_shift_feasibility():
            self.check_three_shift_feasibility()

    def perform_allocation(self, shift, partition):
        if shift == (3, 3, 4):
            part_a_alloc = mode(partition[0])
            part_b_alloc = mode(partition[1])
            part_c_alloc = int(math.ceil(mean(partition[2])))
            self.add_shifts(shift, (part_a_alloc, part_b_alloc, part_c_alloc))
        elif shift == (3, 4, 3):
            part_a_alloc = mode(partition[0])
            part_b_alloc = int(math.ceil(mean(partition[1])))
            part_c_alloc = mode(partition[2])
            self.add_shifts(shift, (part_a_alloc, part_b_alloc, part_c_alloc))
        elif shift == (4, 3, 3):
            part_a_alloc = int(math.ceil(mean(partition[0])))
            part_b_alloc = mode(partition[1])
            part_c_alloc = mode(partition[2])
            self.add_shifts(shift, (part_a_alloc, part_b_alloc, part_c_alloc))
        else:
            part_a_alloc = mode(partition[0])
            part_b_alloc = mode(partition[1])
            self.add_shifts(shift, (part_a_alloc, part_b_alloc))

