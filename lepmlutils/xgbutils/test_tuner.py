import unittest
import os
import pandas as pd
from .tuner import Tuner

class TestPartition(unittest.TestCase):
    def setUp(self):
        pass

    def test_partitions_correctly(self):
        dirname = os.path.dirname(__file__)
        dataset = pd.read_csv(dirname + "/resources/train.csv")
        
        features = [
            "Pclass", 
            "Sex", 
            "Age", 
            "SibSp", 
            "Parch", 
            "Fare", 
            "Embarked"
        ]
        target = [
            "Survived",
        ]
        candidates = {
            'max_depth': range(4, 40, 10),
        }
        set_params = {
            "n_estimators": 40,
        }

        tuner = Tuner()
        results = tuner.tune(
            candidates,
            set_params,
            dataset,
            features,
            target,
            3,
        )

        self.assertEqual(4, len(results))
