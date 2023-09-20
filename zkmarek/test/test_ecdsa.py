from unittest import TestCase

from zkmarek.crypto.ecdsa import ECDSASignature


class TestECDSASignature(TestCase):
    def test_to_der(self):
        for r, s, expected_der in [
            (0xe4e87c417196c6e5cd63f93e94929ccda6d04fc0a7446922baf3070e854ec4f4,
             0xa1ecd098008329de9bc93fb2ded6aaceecc921f7183d6b3cfc673b3ef8af219e,
             '3046022100e4e87c417196c6e5cd63f93e94929ccda6d04fc0a7446922baf3070' +
             'e854ec4f4022100a1ecd098008329de9bc93fb2ded6aaceecc921f7183d6b3cfc673b3ef8af219e'),
            (0x3e2e630c5a44fbfbc597d2b0144b3d71085f04cf4d6f2c50307a9ba96907ff91,
             0xb449b366639e08e9dd915a57940f7bc715262a7ea790000cd2cbc335a9aed837,
             '304502203e2e630c5a44fbfbc597d2b0144b3d71085f04cf4d6f2c50307a9ba96' +
             '907ff91022100b449b366639e08e9dd915a57940f7bc715262a7ea790000cd2cbc335a9aed837')
        ]:
            with self.subTest("Test der format"):
                self.assertEqual(expected_der, ECDSASignature(r, s, 0).to_der().hex())
