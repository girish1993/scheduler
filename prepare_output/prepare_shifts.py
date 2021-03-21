import re
import pandas as pd


class PrepareShifts:

    def __init__(self, allocated_shifts, demand_data):
        self.allocated_shifts = allocated_shifts
        self.demand_data = demand_data
        self.start_time = []
        self.end_time = []
        self.time_format = "{:02d}:00:00"

    def get_allocated_shifts(self):
        return self.allocated_shifts

    def get_demand_data(self):
        return self.demand_data

    def set_start_time(self, start_time):
        self.start_time.append(start_time)

    def get_start_time(self):
        return self.start_time

    def set_end_time(self, end_time):
        self.end_time.append(end_time)

    def get_end_time(self):
        return self.end_time

    def get_time_format(self):
        return self.time_format

    def prepare_time_list_according_to_format(self):
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
        if position == "start":
            return self.get_time_format().format(int(time_string.split("-")[0]))
        else:
            return self.get_time_format().format(int(time_string.split("-")[1]))

    def prepare_shifts(self):
        actual_data = self.prepare_time_list_according_to_format()
        for time, demand in self.get_allocated_shifts().items():
            demand = list(demand)
            time = list(time)
            start_index = 0
            for i in range(len(demand)):
                while True:
                    start_time_stamp = self.get_string_number(actual_data[start_index], "start")
                    end_time_stamp = self.get_string_number(actual_data[start_index + time[i] - 1], "end")
                    start_index = start_index + time[i]
                    for j in range(demand[i]):
                        self.set_start_time(start_time_stamp)
                        self.set_end_time(end_time_stamp)
                    break

    def prepare_final_shift_dataframe(self):
        shift_information = pd.DataFrame({'Shift Start': self.get_start_time(),
                                          'Shift End': self.get_end_time()})
        return shift_information
