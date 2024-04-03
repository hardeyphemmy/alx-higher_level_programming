#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        """Test that max_integer returns None for an empty list."""
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        """Test that max_integer returns the only element for a list with one element."""
        self.assertEqual(max_integer([5]), 5)

    def test_positive_integers(self):
        """Test that max_integer returns the maximum value for a list of positive integers."""
        self.assertEqual(max_integer([1, 3, 5, 2, 7]), 7)

    def test_negative_integers(self):
        """Test that max_integer returns the maximum value for a list of negative integers."""
        self.assertEqual(max_integer([-5, -2, -8, -1]), -1)

    def test_mixed_integers(self):
        """Test that max_integer returns the maximum value for a list of mixed positive and negative integers."""
        self.assertEqual(max_integer([-3, 6, -1, 2, 8]), 8)

    def test_duplicate_values(self):
        """Test that max_integer returns the maximum value correctly when there are duplicate values in the list."""
        self.assertEqual(max_integer([4, 7, 4, 2, 7]), 7)
        self.assertEqual(max_integer([5]), 5)

    def test_positive_integers(self):
        """Test that max_integer returns the maximum value for a list of positive integers."""
        self.assertEqual(max_integer([1, 3, 5, 2, 7]), 7)

    def test_negative_integers(self):
        """Test that max_integer returns the maximum value for a list of negative integers."""
        self.assertEqual(max_integer([-5, -2, -8, -1]), -1)

    def test_mixed_integers(self):
        """Test that max_integer returns the maximum value for a list of mixed positive and negative integers."""
        self.assertEqual(max_integer([-3, 6, -1, 2, 8]), 8)

    def test_duplicate_values(self):
        """Test that max_integer returns the maximum value correctly when there are duplicate values in the list."""
        self.assertEqual(max_integer([4, 7, 4, 2, 7]), 7)

    def test_max_at_beginning(self):
        """Test that max_integer returns the correct maximum value when the maximum value is at the beginning of the list."""
        self.assertEqual(max_integer([10,5,7,3,8]), 10)

    def test_max_in_middle(self):
        """Test that max_integer returns the correct maximum value when the maximum value is in the middle of the list."""
        self.assertEqual(max_integer([3,8,5,12,5,2]), 12)



if __name__ == '__main__':
    unittest.main()

