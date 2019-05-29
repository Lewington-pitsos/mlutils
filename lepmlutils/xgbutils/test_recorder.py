import unittest
from .recorder import Recorder

class TestRecorder(unittest.TestCase):
    def setUp(self):
        pass

    def test_sorts_correctly(self):
        records = [
            {'test_score': 0.8410596026490066,
            'params': {'n_estimators': 260,
            'subsample': 0.7800000000000002,
            'min_split_loss': 0.75,
            'max_depth': 8}},
            {'test_score': 0.8675496688741722,
            'params': {'n_estimators': 260,
            'subsample': 0.9600000000000004,
            'min_split_loss': 0.75,
            'max_depth': 8}},
            {'test_score': 0.8543046357615894,
            'params': {'n_estimators': 260,
            'subsample': 0.6000000000000001,
            'min_split_loss': 0.75,
            'max_depth': 8}},
            {'test_score': 0.8807947019867549,
            'params': {'n_estimators': 260,
            'subsample': 0.9400000000000004,
            'min_split_loss': 0.75,
            'max_depth': 8}}
        ]

        r = Recorder()
        r.records = records
        r.sort_records()

        self.assertEqual(r.best_params()["test_score"],0.8807947019867549) 
        self.assertEqual(r.best_params()["params"]["subsample"],0.9400000000000004) 
        self.assertEqual(r.best_n_params(2)[1]["test_score"],  0.8675496688741722)
        self.assertEqual(r.best_n_params(2)[1]["params"]["subsample"],  0.9600000000000004)


