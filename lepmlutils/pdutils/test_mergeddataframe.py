import unittest
import os
import pandas as pd
from .mergeddataframe import MergedDataFrame, merged_df

class TestHelp(unittest.TestCase):
    def setUp(self):
        self.dirname = os.path.dirname(__file__)
        self.houses = pd.read_csv(self.dirname + "/resources/houses_train.csv")
        self.houses_test = pd.read_csv(self.dirname + "/resources/houses_t.csv")

    def test_can_extract(self):
        self.assertEqual(1460, self.houses.shape[0])
        df = merged_df(self.houses, self.houses_test, ["SalePrice"], "Id")
        self.assertEqual(1460, df.train_indices.shape[0])
        self.assertEqual(1459, df.test_indices.shape[0])

        df2 = df[["OverallQual", "YearBuilt"]]
        self.assertEqual(1460, df2.train_indices.shape[0])
        self.assertEqual(1459, df2.test_indices.shape[0])

        self.assertTrue(self.houses["MSSubClass"].equals(df.trainFrame()["MSSubClass"]))
        


    
