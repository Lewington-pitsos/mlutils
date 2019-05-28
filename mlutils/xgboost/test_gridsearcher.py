import unittest
from .gridsearcher import GridSearcher

class TestGridSearcher(unittest.TestCase):
    def setUp(self):
        self.params = {
            "a": [2, 4, 6],
            "b": [11, 22, 33]
        }

    def test_iterates_correctly(self):
        srch = GridSearcher(self.params)

        for candidates in srch:
            self.assertTrue("a" in candidates.keys())
            self.assertTrue("b" in candidates.keys())

    def test_iterates_exhaustively(self):
        srch = GridSearcher(self.params)

        first_candidates = next(srch)

        self.assertDictEqual({
            "a": 2,
            "b": 11
        }, first_candidates)

        next(srch)
        next(srch)
        next(srch)
        first_candidates = next(srch)

        self.assertDictEqual({
            "a": 6,
            "b": 33
        }, first_candidates)

        self.assertRaises(StopIteration, srch.__next__)

    def test_works_with_small_params(self):
        params = {
            "a": [2],
            "b": [11]
        }
        
        srch = GridSearcher(params)

        first_candidates = next(srch)

        self.assertDictEqual({
            "a": 2,
            "b": 11
        }, first_candidates)
        self.assertRaises(StopIteration, srch.__next__)

