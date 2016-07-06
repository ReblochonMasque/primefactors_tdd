"""
filename.py
:created on: date
__author__ = 'Frederic Dupont'
:License: GPL3
"""


import sys


def factors_of(num):
    """prime factors decompositon
    :param num: the number to decompose
    :return: a list of the prime factors of num
    """
    factors = []
    divisor = 2
    while num  > 1:
        while num % divisor == 0:
            factors.append(divisor)
            num = num // divisor
        divisor += 1

    return factors


def main(argv):
    pass


if __name__ == '__main__':
    sys.exit(main(sys.argv))
