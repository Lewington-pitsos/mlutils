import unittest
from .tuner import lol

class TestTest(unittest.TestCase):
    def test(self):
        self.assertEqual(lol(), 4)