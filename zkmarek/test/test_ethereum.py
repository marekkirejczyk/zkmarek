import unittest
from zkmarek.crypto.ethereum import hash_message


TEST_SECRET: str = "9de347a715a200cd8e83cecc4277c7fdf2ebd95766720abec8364d879483b69b"
TEST_MESSAGE: str = "Whatever"

class TestEthereum(unittest.TestCase):

    def test_hash_message(self):
        actual = hash_message(TEST_MESSAGE)
        expected = "2de4a69a7663970b80a2e37678eb1f73b0fe9209bfd4a191fea3d31588e451fd"
        self.assertEqual(expected.lower(), actual.lower())
