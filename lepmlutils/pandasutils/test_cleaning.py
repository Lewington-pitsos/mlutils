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

