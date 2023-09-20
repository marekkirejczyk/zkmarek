import unittest

from zkmarek.crypto.wallet import Wallet
from zkmarek.test.test_ethereum import TEST_SECRET_KEY, TEST_MESSAGE


class TestWallet(unittest.TestCase):
    def test_generate_ethereum_address(self):
        expected_address = "0xE31cC18f3F3718588E9a878A516C7889AF047171"
        actual_address = Wallet(TEST_SECRET_KEY).get_address()
        self.assertEqual(expected_address.lower(), actual_address.lower())

    def test_ethereum_sign_message(self):
        wallet = Wallet(TEST_SECRET_KEY)
        sig = wallet.sign(TEST_MESSAGE)

        # Expected test values generated on https://www.myetherwallet.com/wallet/sign
        expected_r = 0x41877abc1100a650bbf1076853767b47f93732cdf649bf1c745aa7f2189fe51d
        expected_s = 0x58343ef9a986cbc52379556d466b4f9a6c1790b11d3e01220ec038539437123f
        expected_v = 28
        expected_signature = "41877abc1100a650bbf1076853767b47f93732cdf649bf1c745aa7f2189fe51d58343ef9a986cbc5237955" \
                             "6d466b4f9a6c1790b11d3e01220ec038539437123f1c"

        self.assertEqual(expected_r, sig.r, "Incorrect value r")
        self.assertEqual(expected_s, sig.s, "Incorrect value s")
        self.assertEqual(expected_v, sig.v, "Incorrect value v")
        self.assertEqual(expected_signature, sig.to_hex_encoding())
