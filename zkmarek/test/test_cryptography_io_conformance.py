import hashlib
import unittest

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric.utils import decode_dss_signature

from zkmarek.crypto.ec_affine import ECAffine
from zkmarek.crypto.ecdsa import ECDSASignature
from zkmarek.crypto.standard import Secp256

TEST_ROUNDS = 100


class TestCryptographyIoConformance(unittest.TestCase):

    def test_sign_with_random_k_and_verify(self):
        standard = Secp256
        for i in range(TEST_ROUNDS):
            sk: int = standard.generate_secret_key()
            pk: ECAffine = standard.generate_public_key(sk)
            message: bytes = b'abc'
            sig: bytes = ECDSASignature.sign(standard, sk, message).to_der()

            vk = ec.EllipticCurvePublicNumbers(pk.x.value, pk.y.value, curve=ec.SECP256K1()).public_key()
            vk.verify(sig, message, ec.ECDSA(hashes.SHA256()))

    def test_verify(self):
        for i in range(TEST_ROUNDS):
            private_key = ec.generate_private_key(ec.SECP256K1())
            public_key = private_key.public_key()
            msg = b'abc'
            signature = private_key.sign(msg, ec.ECDSA(hashes.SHA256()))
            r, s = decode_dss_signature(signature)

            msg_hash = hashlib.sha256(msg).digest()
            z = int.from_bytes(msg_hash, 'big')
            standard = Secp256
            result = standard.verify(z, r, s, ECAffine(
                public_key.public_numbers().x,
                public_key.public_numbers().y,
                standard.curve
            ))
            self.assertTrue(result)
