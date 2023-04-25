import unittest
from elliptic.crypto.field import Field

class TestField(unittest.TestCase):
    def test_init(self):
        f = Field(1, 13)
        self.assertEqual(f.value, 1)
        self.assertEqual(f.order, 13)

    def test_eq(self):
        self.assertTrue(Field(1, 13) == Field(1, 13))
        self.assertTrue(Field(13, 1) == Field(13, 1))
        self.assertFalse(Field(2, 1) == Field(1, 1))
        with self.assertRaises(AssertionError):
            Field(1, 2) == Field(1, 1)

    def test_add(self):
        self.assertEqual(Field(1, 13) + Field(10, 13), Field(11, 13))
        self.assertEqual(Field(10, 13) + Field(10, 13), Field(7, 13))
        self.assertEqual(Field(1, 13) + 10, Field(11, 13))
        self.assertEqual(Field(10, 13) + 10, Field(7, 13))
        with self.assertRaises(AssertionError):
            Field(2, 13) + Field(2, 2)

    def test_sub(self):
        self.assertEqual(Field(0, 13) - Field(1, 13), Field(12, 13))
        self.assertEqual(Field(10, 13) - Field(20, 13), Field(3, 13))
        self.assertEqual(Field(0, 13) - 1, Field(12, 13))
        self.assertEqual(Field(10, 13) - 20, Field(3, 13))
        with self.assertRaises(AssertionError):
            Field(2, 13) - Field(2, 2)

    def test_mul(self):
        self.assertEqual(Field(2, 13) * Field(2, 13), Field(4, 13))
        self.assertEqual(Field(4, 13) * Field(4, 13), Field(3, 13))
        self.assertEqual(Field(2, 13) * 2, Field(4, 13))
        self.assertEqual(Field(4, 13) * 4, Field(3, 13))
        with self.assertRaises(AssertionError):
            Field(2, 13) * Field(2, 2)

    def test_pow(self):
        self.assertEqual(Field(2, 13) ** 2, Field(4, 13))
        self.assertEqual(Field(2, 2**256-1) ** 256, Field(1, 2**256-1))
        self.assertEqual(Field(2, 13) ** Field(2, 13), Field(4, 13))
        self.assertEqual(Field(2, 2**256-1) ** Field(256, 2**256-1), Field(1, 2**256-1))

    def test_neg(self):
        self.assertEqual(-Field(1, 3), Field(2, 3))
        self.assertEqual(-Field(2, 3), Field(1, 3))
        self.assertEqual(-Field(17, 29), Field(12, 29))

    def test_neg_add(self):
        for p in [5, 7, 11, 13, 17, 19, 23, 29]:
            for i in range(1, p):
                self.assertEqual(--Field(i, p), Field(i, p))
