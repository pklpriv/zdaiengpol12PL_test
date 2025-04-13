import unittest
from file_to_test import euclidian_distance, divide

class TestFile(unittest.TestCase):
    def test_standard_division(self):
        self.assertEqual(divide(4,2),2)
        
    def test_negative_division(self):
        self.assertEqual(divide(5,-5), -1)
        
    def test_zero_vector(self):
        self.assertEqual(euclidian_distance([0,0,0]),0)
        
    def test_zero_division(self):
        self.assertRaises(divide(2,0), ValueError)
        