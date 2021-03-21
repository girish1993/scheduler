from file_operations.file_operations import FileOperations
from data_operations.data_analysis import DataAnalyser

if __name__ == "__main__":
    file_operations = FileOperations()
    data = file_operations.read_csv_file()
    data_analyser = DataAnalyser(data=data)
    data_analyser.perform_basic_data_analysis()
