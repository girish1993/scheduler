import re
import pandas as pd


class PrepareShifts:
    """
    PrepareShifts is the class that implements the business logic of finding the optimum partitions and the
    associated shifts for the Barista demand data.
    """

    def __init__(self, allocated_shifts, demand_data):
        """
        Constructor for PrepareShifts
        :param allocated_shifts: The allocated shifts from shift allocator
        :type allocated_shifts: List
        :param demand_data: The Time column of the Dataframe
        :type demand_data: Series
        """
        self.allocated_shifts = allocated_shifts
        self.demand_data = demand_data
        self.start_time = []
        self.end_time = []
        self.time_format = "{:02d}:00:00"

    def get_allocated_shifts(self):
        """
        Getter for allocated_shifts
        :return: allocated_shifts
        :rtype: List
        """
        return self.allocated_shifts

    def get_demand_data(self):
        """
        Getter for demand_data
        :return: The actual dataframe data from the file
        :rtype: Dataframe
        """
        return self.demand_data

    def set_start_time(self, start_time):
        """
        Setter for start time of a shift
        :param start_time: The string formatted time for start time
        :type start_time: str
        :return: None
        :rtype: None
        """
        self.start_time.append(start_time)

    def get_start_time(self):
        """
        Getter for start time
        :return: The list for start_time
        :rtype: List
        """
        return self.start_time

    def set_end_time(self, end_time):
        """
        Setter for end time
        :param end_time: The string formatted time for end time
        :type end_time: str
        :return: None
        :rtype: None
        """
        self.end_time.append(end_time)

    def get_end_time(self):
        """
        Getter for end_time
        :return: List of end_time
        :rtype: List
        """
        return self.end_time

    def get_time_format(self):
        """
        Getter for time_format
        :return: The set time format
        :rtype: str
        """
        return self.time_format

    def prepare_time_list_according_to_format(self):
        """
        Method to convert the time formats into a 24 hour time format.
        :return: A list of the time formats without am|pm indicators and converted to 24 hour format timings
        :rtype: List
        """
        final_time_list = []
        actual_data = list(self.get_demand_data()["Time"])
        for each in actual_data:
            if "pm" in each and "am" not in each:
                sub_str = []
                res = re.sub('pm', '', each)
                res = res.split("-")
                res = list(map(int, res))
                for each_split in res:
                    if each_split < 12:
                        each_split += 12
                    sub_str.append(str(each_split))
                final_time_list.append("-".join(sub_str))
            if "am" in each and "pm" not in each:
                res = re.sub('am', '', each)
                final_time_list.append(res)
            if "am" in each and "pm" in each:
                res = re.sub('am|pm', '', each)
                final_time_list.append(res)
        return final_time_list

    def get_string_number(self, time_string, position):
        """
        Method to convert the extracted time numeric number into the required format.
        :param time_string: time numeric value
        :type time_string: str
        :param position: to indicate whether the time is to be split at the start or the end
        :type position: str
        :return: Formatted string time representation
        :rtype: str
        """
        if position == "start":
            return self.get_time_format().format(int(time_string.split("-")[0]))
        else:
            return self.get_time_format().format(int(time_string.split("-")[1]))

    def prepare_shifts(self):
        """
        Method to logically evaluates the demand data and the allocated shifts to make entries for start time and end
        time for shifts
        :return: None
        :rtype: None
        """
        actual_data = self.prepare_time_list_according_to_format()
        for time, demand in self.get_allocated_shifts().items():
            demand = list(demand)
            time = list(time)
            start_index = 0
            for i in range(len(demand)):
                start_time_stamp = self.get_string_number(actual_data[start_index], "start")
                end_time_stamp = self.get_string_number(actual_data[start_index + time[i] - 1], "end")
                start_index = start_index + time[i]
                for j in range(demand[i]):
                    self.set_start_time(start_time_stamp)
                    self.set_end_time(end_time_stamp)

    def prepare_final_shift_dataframe(self):
        """
        Method to create a Dataframe out of the lists prepared
        :return: Dataframe with start and end times for shifts
        :rtype: Dataframe
        """
        shift_information = pd.DataFrame({'Shift Start': self.get_start_time(),
                                          'Shift End': self.get_end_time()})
        return shift_information
