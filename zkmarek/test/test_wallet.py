import unittest

from zkmarek.crypto.wallet import Wallet, hash_message
from zkmarek.test.constant import TEST_MESSAGE, TEST_SECRET


class TestWallet(unittest.TestCase):
    def test_generate_ethereum_address(self):
        expected_address = "0xE31cC18f3F3718588E9a878A516C7889AF047171"
        actual_address = Wallet(TEST_SECRET).get_address()
        self.assertEqual(expected_address.lower(), actual_address.lower())

    def test_sign(self):
        wallet = Wallet(TEST_SECRET)
        seed = "9de347a715a200cd8e83cecc4277c7fdf2ebd95766720abec8364d879483b69b2de4a69a7663970b80a2e37678eb1f73b0fe9209bfd4a191fea3d31588e451fd"
        expected = "0x41877abc1100a650bbf1076853767b47f93732cdf649bf1c745aa7f2189fe51d58343ef9a986cbc52379556d466b4f9a6c1790b11d3e01220ec038539437123f1c"
        actual = wallet.sign(TEST_MESSAGE, seed)
        self.assertEqual(expected.lower(), actual)

