import unittest
import pandas as pd
from mainclass import EmployeeDataAnalysis
from test.TestUtils import TestUtils
import os


class FunctionalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.analysis = EmployeeDataAnalysis("employee_data.csv")
        cls.test_obj = TestUtils()

    def test_csv_loading(self):
        """Test if the CSV file is loaded correctly."""
        try:
            if not self.analysis:
                self.test_obj.yakshaAssert("TestCSVLoading", False, "functional")
                print("TestCSVLoading = Failed")
                return
            obj = not self.analysis.df.empty
            self.test_obj.yakshaAssert("TestCSVLoading", obj, "functional")
            print("TestCSVLoading = Passed" if obj else "TestCSVLoading = Failed")
        except:
            self.test_obj.yakshaAssert("TestCSVLoading", False, "functional")
            print("TestCSVLoading = Failed")
                

    def test_handle_missing_values(self):
        """Test if missing values are replaced with column means."""
        try:
            # Count the initial number of missing values
            initial_missing = self.analysis.df.isnull().sum().sum()
            # Call the function to handle missing values
            self.analysis.handle_missing_values()
            # Count the final number of missing values
            final_missing = self.analysis.df.isnull().sum().sum()
            # Assert that the number of missing values decreased
            obj = initial_missing > final_missing
            self.test_obj.yakshaAssert("TestHandleMissingValues", obj, "functional")
            print("TestHandleMissingValues = Passed" if obj else "TestHandleMissingValues = Failed")
        except Exception as e:
            print("TestHandleMissingValues = Failed")

    def test_export_updated_csv(self):
        """Test if the updated CSV file is saved correctly."""
        try:
            output_file = self.analysis.export_updated_csv()
            obj = pd.read_csv(output_file) is not None
            self.test_obj.yakshaAssert("TestExportUpdatedCSV", obj, "functional")
            print("TestExportUpdatedCSV = Passed" if obj else "TestExportUpdatedCSV = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestExportUpdatedCSV", False, "functional")
            print("TestExportUpdatedCSV = Failed")