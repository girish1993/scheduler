from file_operations.file_operations import FileOperations
from data_operations.data_analysis import DataAnalyser
from shift_allocator.shift_allocator import ShiftAllocator

if __name__ == "__main__":
    file_operations = FileOperations()
    data = file_operations.read_csv_file()
    data_analyser = DataAnalyser(data=data)
    data_analyser.perform_basic_data_analysis()
    shift_allocator = ShiftAllocator(data=data)
    shift_allocator.check_allocation()
    print(shift_allocator.get_allocated_shifts())
