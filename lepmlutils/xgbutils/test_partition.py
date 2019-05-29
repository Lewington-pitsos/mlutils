import unittest
import os
import pandas as pd
from typing import Type
from .gridsearcher import GridSearcher
from .partition import Partition

class TestPartition(unittest.TestCase):
    def setUp(self):
        pass

    def test_partitions_correctly(self):
        dirname = os.path.dirname(__file__)
        dataset = pd.read_csv(dirname + "/resources/train.csv")
        p = Partition(dataset)

