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


if __name__ == '__main__':
    unittest.main()