import unittest
import os
import pandas as pd
from .taggeddataframe import TaggedDataFrame
from .categorizetfm import CategorizeTfm

class TestCategorization(unittest.TestCase):
    def setUp(self):
        dirname = os.path.dirname(__file__)
        self.houses: TaggedDataFrame = TaggedDataFrame(pd.read_csv(dirname + "/resources/houses_train.csv"))
    
    def test_converts_objects_to_categorical(self):
        self.assertEqual(43, len(self.houses.frame.select_dtypes(include="object").columns))
        self.assertEqual(0, len(self.houses.frame.select_dtypes(include="category").columns))

        tfm: CategorizeTfm = CategorizeTfm()
        tfm.operate(self.houses)
        self.assertEqual(0, len(self.houses.frame.select_dtypes(include="object").columns))
        self.assertEqual(43, len(self.houses.frame.select_dtypes(include="category").columns))
        self.assertEqual(124, len(self.houses.frame.columns))

    def test_raises_error_on_col_name_conflicts(self):
        tfm: CategorizeTfm = CategorizeTfm()
        self.houses.frame["LandSlope_mapping"] = 0
        self.assertRaises(AssertionError, tfm.operate, self.houses)
