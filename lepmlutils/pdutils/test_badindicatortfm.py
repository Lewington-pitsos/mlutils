import unittest
import os
import pandas as pd
from .badindicatortfm import BadIndicatorTfm
from .lepdataframe import LepDataFrame

class TestAddBadIndicator(unittest.TestCase):
    def setUp(self):
        dirname = os.path.dirname(__file__)
        self.dataset = LepDataFrame(pd.read_csv(dirname + "/resources/train.csv"))

    def test_raises_errors_for_column_overwrite(self):
        tfm = BadIndicatorTfm()
        self.dataset.df["Cabin_is_bad"] = 9

        self.assertRaises(AssertionError, tfm.operate, self.dataset)

    def test_raises_adds_bad_value_columns(self):
        tfm = BadIndicatorTfm()

        self.assertEqual(12, len(self.dataset.df.columns))
        tfm.operate(self.dataset)

        self.assertEqual(15, len(self.dataset.df.columns))
        self.assertEqual(687, self.dataset.df["Cabin_is_bad"].sum())
        self.assertEqual(2, self.dataset.df["Embarked_is_bad"].sum())
        self.assertEqual(177, self.dataset.df["Age_is_bad"].sum())