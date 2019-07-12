from .persister import Persister
import unittest
import pandas as pd

class TestPersister(unittest.TestCase):
    def setUp(self):
        pass
        
    
    def test_no_implicit_overrides(self):
        p = Persister("somedir")
        set1 = pd.DataFrame()

        p.save("somename", set1)

        self.assertRaises(KeyError, p.save, "somename", set1)

    
