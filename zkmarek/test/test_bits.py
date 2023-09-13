import unittest

from zkmarek.crypto.bits import truncate_bits


class TestBits(unittest.TestCase):
    def test_truncate_bits(self):
        params = [
            ('0b1010', 1, 0b1),
            ('0b1010', 2, 0b10),
            ('0b1111', 3, 0b111),
            ('0b0001', 1, 0b0),
            ('0b0001', 2, 0b0),
            ('0b0001', 3, 0b0),
            ('0b0001', 4, 0b0001),
            ('0b0000000000000000000000000000000000000000000000000000000000000001', 63, 0b0),
            ('0b0000000000000000000000000000000000000000000000000000000000000001', 64, 0b1),
        ]

        for n, number_truncate, expected in params:
            with self.subTest(f'Truncate {n} by {number_truncate} bits'):
                self.assertEqual(expected, truncate_bits(n, number_truncate))
