import unittest
import os
import pandas as pd
from .cleaning import *

class TestAddBadIndicator(unittest.TestCase):
    def setUp(self):
        dirname = os.path.dirname(__file__)
        self.dataset = pd.read_csv(dirname + "/resources/train.csv")

    def test_raises_errors_for_column_overwrite(self):
        self.dataset["Cabin_is_bad"] = 9

        self.assertRaises(AssertionError, add_bad_indicator_vars, self.dataset)

    def test_raises_adds_bad_value_columns(self):
        self.assertEqual(12, len(self.dataset.columns))
        add_bad_indicator_vars(self.dataset)

        self.assertEqual(15, len(self.dataset.columns))
        self.assertEqual(687, self.dataset["Cabin_is_bad"].sum())
        self.assertEqual(2, self.dataset["Embarked_is_bad"].sum())
        self.assertEqual(177, self.dataset["Age_is_bad"].sum())

class TestColumnReplace(unittest.TestCase):
    def setUp(self):
        dirname = os.path.dirname(__file__)
        self.dataset = pd.read_csv(dirname + "/resources/train.csv")
    
    def test_raises_adds_bad_value_columns(self):
        self.assertEqual(3, self.dataset.isna().any().sum())
        self.dataset.apply(replace_bad_values_with_median)
        self.assertEqual(0, self.dataset.isna().any().sum())