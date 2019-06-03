import unittest
import os
from .lepdataframe import LepDataFrame
from .badindicatortfm import BadIndicatorTfm
import pandas as pd

class TestLepDataFrame(unittest.TestCase):
    def setUp(self):
        dirname = os.path.dirname(__file__)
        self.dataset = pd.read_csv(dirname + "/resources/train.csv")

    def test_applies_transform(self):
        l = LepDataFrame(self.dataset)
        tfm = BadIndicatorTfm()
        l.apply(tfm)