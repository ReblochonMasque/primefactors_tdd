"""
primefactorstdd.py
:created on: 20160706
__author__ = 'Frederic Dupont'
:License: GPL3
"""

import unittest
from primefactorstdd.primefactors import factors_of


class TestPrimeFactors(unittest.TestCase):
    """test suite for PrimeFactors"""

    def test_factors_of_1(self):
        """test if factor_of(1) returns []
        """
        self.assertEqual(factors_of(1), [])


    def test_factors_of_2(self):
        """test if factors_of(2) returns [2]
        """
        self.assertEqual(factors_of(2), [2])


    def test_factors_of_3(self):
        """test if factors_of(3) returns [3]
        """
        self.assertEqual(factors_of(3), [3])

    def test_factors_of_4(self):
        """test if factors_of(4) returns [2, 2]
        """
        self.assertEqual(factors_of(4), [2, 2])

    def test_factors_of_5(self):
        """test if factors_of(5) returns [5]
        """
        self.assertEqual(factors_of(5), [5])

    def test_factors_of_6(self):
        """test if factors_of(6) returns [2, 3]
        """
        result = factors_of(6)
        self.assertEqual(len(result), 2)
        for elt in result:
            self.assertIn(elt, [2, 3])

    def test_factors_of_7(self):
        """test if factors_of(7) returns [7]
        """
        result = factors_of(7)
        self.assertEqual(len(result), 1)
        for elt in result:
            self.assertIn(elt, [7])

    def test_factors_of_8(self):
        """test if factors_of(8) returns [2, 2, 2]
        """
        result = factors_of(8)
        self.assertEqual(len(result), 3)
        for elt in result:
            self.assertIn(elt, [2, 2, 2])

    def test_factors_of_9(self):
        """test if factors_of(8) returns [2, 2, 2]
        """
        result = factors_of(9)
        self.assertEqual(len(result), 2)
        for elt in result:
            self.assertIn(elt, [3, 3])

    def test_factors_of_2_2_3_3_3_7_11_11_15(self):
        """test if factors_of(8) returns [2, 2, 3, 3, 3, 3, 5, 7, 11, 11]
        """
        result = factors_of(2 * 2 * 3 * 3 * 3 * 7 * 11 * 11 * 15)
        self.assertEqual(len(result), 10)
        for elt in result:
            self.assertIn(elt, [2, 2, 3, 3, 3, 3, 5, 7, 11, 11])

if __name__ == '__main__':
    unittest.main()