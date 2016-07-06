"""
primefactorstdd.py
:created on: 20160706
__author__ = 'Frederic Dupont'
:License: GPL3
"""

import unittest
from primefactorstdd.primefactors import factor_of


class TestPrimeFactors(unittest.TestCase):
    """test suite for PrimeFactors"""

    def test_factors_of(self):
        """test if factor_of(1) returns []
        """
        self.assertEqual(factor_of(1), [])





if __name__ == '__main__':
    unittest.main()