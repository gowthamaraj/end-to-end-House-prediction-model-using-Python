import unittest
from model import model
import numpy as np

class TestModel(unittest.TestCase):
    def test_model(self):
        self.assertEqual(int(model.predict([[5,5,5]])[0]), 51924)

if __name__ == '__main__':
    unittest.main()