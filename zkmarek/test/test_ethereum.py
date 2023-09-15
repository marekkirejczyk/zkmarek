import unittest
from zkmarek.crypto.ethereum import hash_message
from zkmarek.test.constant import TEST_MESSAGE


class TestEthereum(unittest.TestCase):

    def test_hash_message(self):
            actual = hash_message(TEST_MESSAGE)
            expected = "2de4a69a7663970b80a2e37678eb1f73b0fe9209bfd4a191fea3d31588e451fd"
            self.assertEqual(expected.lower(), actual.lower())
