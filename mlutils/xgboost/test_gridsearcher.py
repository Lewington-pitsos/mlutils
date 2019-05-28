import unittest
from .gridsearcher import GridSearcher

class TestGridSearcher(unittest.TestCase):
    def test_iterates_correctly(self):

        params = {
            "a": [2, 4, 6],
            "b": [11, 22, 33]
        }

        srch = GridSearcher(params)

        for candidates in srch:
            self.assertTrue("a" in candidates.keys())
            self.assertTrue("b" in candidates.keys())