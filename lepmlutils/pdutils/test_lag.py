import unittest
import os
from sklearn import neighbors
from .lag import *
from .internal import *
from .globals import *

class TestLag(unittest.TestCase):
    def setUp(self):
        pass
        # self.dirname = os.path.dirname(__file__)
        # self.dataset = pd.read_csv(self.dirname + "/resources/train.csv")
        # self.houses = pd.read_csv(self.dirname + "/resources/houses_train.csv")
        # self.houses_test = pd.read_csv(self.dirname + "/resources/houses_t.csv")
    
    def test_grouping_check(self):
        df = pd.DataFrame({
                "day":   [3,  3,  4,  4,  4,  5,   5, 7],
                "price": [99, 21, 77, 32, 32, 109, 7, 8],
                "dist":  [1,  2,  2,  1,  1,  1,   2, 1],
        }, )


        df["hash"] = multi_concat_feat(df, ["dist", "day"])
        self.assertTrue(already_grouped(df, "hash", "price"))

        df = pd.DataFrame({
            "day":   [3,  3,  4,  4,  4,  5,   5, 7],
            "price": [99, 21, 77, 32, 99999, 109, 7, 8],
            "dist":  [1,  2,  2,  1,  1,  1,   2, 1],
        }, )
        df["hash"] = multi_concat_feat(df, ["dist", "day"])
        self.assertFalse(already_grouped(df, "hash", "price"))


    def test_creatinglags(self):
        df = pd.DataFrame({
                "day":   [3,  3,  4,  4,  4,  5,   5, 7],
                "price": [99, 21, 77, 32, 32, 109, 7, 8],
                "dist":  [1,  2,  2,  1,  1,  1,   2, 1],
        }, )

        create_lag(df, "price", "day", 1, ["dist"])

        for col in [hash_col, lagged_time_col, lagged_hash_col]:
            self.assertTrue(not contains(df, col))
        
        self.assertEqual(4, df.shape[1])
        self.assertTrue("price-dist-dayLag1" in list(df.columns))




