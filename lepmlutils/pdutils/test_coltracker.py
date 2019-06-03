import unittest
import os
from .coltracker import ColTracker
from typing import List
from .coltag import ColTag
import pandas as pd

class TestCollTracker(unittest.TestCase):
    def setUp(self):
        dirname = os.path.dirname(__file__)
        self.dataset = pd.read_csv(dirname + "/resources/train.csv")

    def test_initializes_and_returns_tags(self):
        t: ColTracker = ColTracker(self.dataset)
        originals: List[str] = t.tagged_as(ColTag.original)
        self.assertEqual(len(self.dataset.columns.values), len(originals))

        modified: List[str] = t.tagged_as(ColTag.modified)
        self.assertEqual(0, len(modified))

    def test_tracks_and_returns_tags(self):
        t: ColTracker = ColTracker(self.dataset)
        t.tag_column("Cabin", ColTag.modified)
        modified: List[str] = t.tagged_as(ColTag.modified)
        self.assertEqual(1, len(modified))
        self.assertEqual("Cabin", modified[0])

        t.tag_column("Cabin", ColTag.modified)
        modified: List[str] = t.tagged_as(ColTag.modified)
        self.assertEqual(1, len(modified))

        t.tag_column("NewCol", ColTag.modified)
        modified: List[str] = t.tagged_as(ColTag.modified)
        self.assertEqual(2, len(modified))

        originals: List[str] = t.tagged_as(ColTag.original)
        self.assertEqual(len(self.dataset.columns.values), len(originals))

        mapping: List[str] = t.tagged_as(ColTag.mapping)
        self.assertEqual(0, len(mapping))

        t.tag_column("NewCol", ColTag.mapping)
        mapping: List[str] = t.tagged_as(ColTag.mapping)
        self.assertEqual(1, len(mapping))