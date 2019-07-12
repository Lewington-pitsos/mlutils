from .persister import Persister
import os
import pandas as pd
import shutil
import unittest

class TestPersister(unittest.TestCase):
    def setUp(self):
        self.data_dir = os.path.dirname(__file__) + "/data"
        os.mkdir(self.data_dir)
    
    def test_no_implicit_overrides(self):
        p = Persister(self.data_dir)
        set1 = pd.DataFrame({"apples":[2, 3,3, 4]})
        self.assertRaises(KeyError, p.load, "somename")

        p.save("somename", set1)

        self.assertRaises(KeyError, p.save, "somename", set1)

        df = p.load("somename")

        self.assertTrue(df.equals(set1))

    def tearDown(self):
        shutil.rmtree(self.data_dir)
    
