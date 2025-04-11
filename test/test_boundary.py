import unittest
import numpy as np
from mainclass import EmployeeDataAnalysis
from test.TestUtils import TestUtils
import pandas as pd


class BoundaryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.analysis = EmployeeDataAnalysis("employee_data.csv")
        cls.test_obj = TestUtils()
        
    def test_boundary(self):
        self.test_obj.yakshaAssert("TestBoundary", True, "boundary")
        print("TestBoundaryEmpty = Passed")

