import unittest

from zkmarek.crypto.wallet import Wallet


class TestWallet(unittest.TestCase):
    def test_generate_ethereum_address(self):
        secret_key: str = "9de347a715a200cd8e83cecc4277c7fdf2ebd95766720abec8364d879483b69b"
        expected_address = "0xE31cC18f3F3718588E9a878A516C7889AF047171"
        actual_address = Wallet(secret_key).get_address()
        self.assertEqual(expected_address.lower(), actual_address.lower())
