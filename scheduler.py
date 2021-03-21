from file_operations.file_operations import FileOperations
from data_operations.data_analysis import DataAnalyser
from shift_allocator.shift_allocator import ShiftAllocator
from prepare_output.prepare_shifts import PrepareShifts

if __name__ == "__main__":
    file_operations = FileOperations()
    data = file_operations.read_csv_file()
    data_analyser = DataAnalyser(data=data)
    data_analyser.perform_basic_data_analysis()
    shift_allocator = ShiftAllocator(data=data)
    shift_allocator.check_allocation()
    allocated_shifts = shift_allocator.get_allocated_shifts()
    shifts_preparer = PrepareShifts(allocated_shifts=allocated_shifts, demand_data=data)
    shifts_preparer.prepare_shifts()
    final_shift_information = shifts_preparer.prepare_final_shift_dataframe()
    file_operations.write_output_shifts_to_file(final_shift_information)
