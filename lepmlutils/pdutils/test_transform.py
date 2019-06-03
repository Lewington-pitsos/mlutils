import unittest
import os
from .coltracker import ColTracker
from typing import List
from .transform import Transform
import pandas as pd
from .cleaning import *

class TestCollTracker(unittest.TestCase):
    def setUp(self):
        dirname = os.path.dirname(__file__)
        self.dataset = pd.read_csv(dirname + "/resources/train.csv")

    def test_initializes_and_returns_tags(self):
        t: ColTracker = ColTracker(self.dataset)
        originals: List[str] = t.get_all(ColTag.original)
        self.assertEqual(len(self.dataset.columns.values), len(originals))

        modified: List[str] = t.get_all(ColTag.modified)
        self.assertEqual(0, len(modified))

    def test_tracks_and_returns_tags(self):
        t: ColTracker = ColTracker(self.dataset)
        t.tag("Cabin", ColTag.modified)
        modified: List[str] = t.get_all(ColTag.modified)
        self.assertEqual(1, len(modified))
        self.assertEqual("Cabin", modified[0])

        t.tag("Cabin", ColTag.modified)
        modified: List[str] = t.get_all(ColTag.modified)
        self.assertEqual(1, len(modified))

        t.tag("NewCol", ColTag.modified)
        modified: List[str] = t.get_all(ColTag.modified)
        self.assertEqual(2, len(modified))

        originals: List[str] = t.get_all(ColTag.original)
        self.assertEqual(len(self.dataset.columns.values), len(originals))

        mapping: List[str] = t.get_all(ColTag.mapping)
        self.assertEqual(0, len(mapping))

        t.tag("NewCol", ColTag.mapping)
        mapping: List[str] = t.get_all(ColTag.mapping)
        self.assertEqual(1, len(mapping))