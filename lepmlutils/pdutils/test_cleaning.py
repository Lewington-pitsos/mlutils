import unittest
import os
import pandas as pd
from .cleaning import *

class TestCategorization(unittest.TestCase):
    def setUp(self):
        dirname = os.path.dirname(__file__)
        self.houses = pd.read_csv(dirname + "/resources/houses_train.csv")
    
    def test_converts_objects_to_categorical(self):
        self.assertEqual(43, len(self.houses.select_dtypes(include="object").columns))
        self.assertEqual(0, len(self.houses.select_dtypes(include="category").columns))

        categorize(self.houses)
        self.assertEqual(0, len(self.houses.select_dtypes(include="object").columns))
        self.assertEqual(43, len(self.houses.select_dtypes(include="category").columns))
        self.assertEqual(124, len(self.houses.columns))


    def test_raises_error_on_col_name_conflicts(self):
        self.houses["LandSlope_mapping"] = 0
        self.assertRaises(AssertionError, categorize, self.houses)
