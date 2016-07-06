"""
filename.py
:created on: date
__author__ = 'Frederic Dupont'
:License: GPL3
"""


# import sys


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


# def main(argv):
#     len_max = 0
#     nums = []
#     result = None
#     for _ in range(100000, 110000):
#         res = factors_of(_)
#         if len(res) > len_max:
#             nums = [_]
#             len_max = len(res)
#         elif len(res) == len_max:
#             nums.append(_)
#             len_max = len(res)
#         else:
#             continue
#     print('number of nums with', len_max, 'factors :', len(nums))
#     for num in nums:
#         print('num :', num, 'factors = ', factors_of(num))
#
#
#
#
#
#
# if __name__ == '__main__':
#     sys.exit(main(sys.argv))
