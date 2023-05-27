import unittest

from zkmarek.crypto.ec_affine import ECAffine
from zkmarek.crypto.weierstrass_curve import Secp256k1_41
from zkmarek.test.constant import SMALL_PRIMES

def naive_mul(p: ECAffine, k: int) -> ECAffine:
    res = p.infinity()
    for _ in range(k):
        res += p
    return res

class TestMul(unittest.TestCase):
    def test_double_and_add(self):
        for prime in SMALL_PRIMES:
            points = ECAffine.generate_points(Secp256k1_41)
            for p in points:
                for i in range(prime + 2):
                    expected=naive_mul(p, i)
                    actual = p.double_and_add(i)
                    if p.y.value != 0:
                        self.assertEqual(expected, actual)

