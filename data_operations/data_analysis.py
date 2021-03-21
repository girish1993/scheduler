from pandas.api.types import is_numeric_dtype


class DataAnalyser:
    """
    A simple class to perform basic Data Analysis on the read data
    """

    def __init__(self, data):
        """
        constructor for Data Analyser
        :param data: The read data from the file
        :type data: Dataframe
        """
        self.data = data

    def get_data(self):
        """
        The getter for data
        :return: The Dataframe containing the data
        :rtype: Dataframe
        """
        return self.data

    def set_data(self, new_data):
        """
        Setter for Data
        :param new_data: The changed or modified data
        :type new_data: Dataframe
        :return: None
        :rtype: None
        """
        self.data = new_data

    def check_for_null_values_and_perform_mean_imputation(self):
        """
        Method to detect null values in the dataframe and impute the missing values with mean value of the column
        :return: None
        :rtype: None
        """
        column_names = list(self.get_data().columns)
        for each_column in column_names:
            if self.get_data()[each_column].isnull().sum():
                print(
                    "There are {} null missing values in {} column".format(self.get_data()[each_column].isnull().sum(),
                                                                           each_column))
                self.get_data()[each_column].fillna(self.get_data()[each_column].mean(), inplace=True)
            else:
                print("No missing values in column ", each_column)

    def check_for_syntactical_and_semantic_errors_and_correct(self):
        """
        Method to check for syntactical and semantic errors in the data and correct them.
        The errors can arise out of 2 situations:

        <li>Synatactical error could be a scenario where the integer data is presented as str. In which case,
        we would typecast it to integer.</li?>
        <li>Semantic errors when the data in not within the limit of 1-6
        baristas. In which case, we would replace the failing conditional checks with right value</li?>
        :return: None
        :rtype: None
        """
        data = self.get_data()
        if not is_numeric_dtype(data["Total number of Baristas needed"]):
            print("The baristas needed column is not of type integer. converting it to integer..")
            data["Total number of Baristas needed"] = data["Total number of Baristas needed"].astype(int)
            self.set_data(data)
        if not data["Total number of Baristas needed"].between(1, 6).all():
            print("There are values in the Barista needed column outside the limit of 1 and 6. Correcting them...")
            data.loc[data["Total number of Baristas needed"] > 6, "Total number of Baristas needed"] = 6
            data.loc[data["Total number of Baristas needed"] < 1, "Total number of Baristas needed"] = 1
            print("Data after correction")
            print("-------------------------------------------------------------------------------")
            self.set_data(data)
            print(self.get_data())
            print("-------------------------------------------------------------------------------")
        else:
            print("All the values are in the expected range")

    def perform_basic_data_analysis(self):
        """
        A Facilitator method that displays all the Analysis done at various stages.
        :return: None
        :rtype: None
        """
        print("-------------------------------------------------------------------------------")
        print("Producing some basic information about the data")
        print("-------------------------------------------------------------------------------")
        print(self.get_data().describe())
        print("-------------------------------------------------------------------------------")
        print("Having a peek at the data")
        print("-------------------------------------------------------------------------------")
        print(self.get_data().head())
        print("-------------------------------------------------------------------------------")
        print("There are in total {} columns".format(len(self.get_data().columns)))
        print("The column names are ", list(self.get_data().columns))
        print("-------------------------------------------------------------------------------")
        print("Checking for null values")
        print("-------------------------------------------------------------------------------")
        self.check_for_null_values_and_perform_mean_imputation()
        print("-------------------------------------------------------------------------------")
        print("Checking for syntactical and semantic errors and correcting them")
        self.check_for_syntactical_and_semantic_errors_and_correct()
