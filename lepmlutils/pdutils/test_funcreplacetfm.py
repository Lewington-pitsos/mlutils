import unittest
import os
from .funcreplacetfm import FuncReplaceTfm 
from .taggeddataframe import TaggedDataFrame 
from .coltag import ColTag
import pandas as pd

class TestFuncReplaceTfm(unittest.TestCase):
    def setUp(self):
        self.dirname = os.path.dirname(__file__)
        self.dataset = TaggedDataFrame(pd.read_csv(self.dirname + "/resources/train.csv"))

    def test_applies_static_callback(self):
        tfm = FuncReplaceTfm(eight)
        self.assertEqual(4, (self.dataset.frame["Age"] == 8.0).sum())
        tfm.operate(self.dataset, ["Age"])
        self.assertEqual(181, (self.dataset.frame["Age"] == 8.0).sum())

    def test_applies_meidan(self):
        tfm = FuncReplaceTfm(median)
        self.assertEqual(25, (self.dataset.frame["Age"] == 28.0).sum())
        tfm.operate(self.dataset, ["Age"])
        self.assertEqual(202, (self.dataset.frame["Age"] == 28.0).sum())


    


def eight(a, b) -> float:
    return 8.0

def median(name: str, df: pd.DataFrame) -> float:
    return df[name].median()