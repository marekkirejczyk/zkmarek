import hashlib
import hmac
from dataclasses import dataclass

from Crypto.Hash import keccak

from zkmarek.crypto.ec_affine import ECAffine
from zkmarek.crypto.ecdsa import ECDSASignature
from zkmarek.crypto.ethereum import hash_message
from zkmarek.crypto.standard import Secp256, Standard


@dataclass(frozen=True)
class Wallet:
    secret_key: int
    standard: Standard = Secp256

    def get_address(self) -> str:
        public_key: ECAffine = Secp256.generate_public_key(self.secret_key)
        hash_input = public_key.serialize_uncompressed()
        k = keccak.new(digest_bits=256)
        k.update(bytes.fromhex(hash_input))
        return '0x' + k.hexdigest()[-40:]

    def sign(self, message: str) -> ECDSASignature:
        msg_hash = int(hash_message(message), 16)
        k = Wallet.deterministic_generate_k(msg_hash.to_bytes(32, 'big'), self.secret_key.to_bytes(32, 'big'))
        r, s, v = self.standard.sign(self.secret_key, msg_hash, k)
        return ECDSASignature(r, s, v)

    # This implementation of generating k parameter is a copy-paste (with minor adjustments) from
    # https://github.com/ethereum/eth-keys/blob/master/eth_keys/backends/native/ecdsa.py#L93
    @staticmethod
    def deterministic_generate_k(msg_hash: bytes, private_key_bytes: bytes) -> int:
        digest_fn = hashlib.sha256

        v_0 = b'\x01' * 32
        k_0 = b'\x00' * 32

        k_1 = hmac.new(k_0, v_0 + b'\x00' + private_key_bytes + msg_hash, digest_fn).digest()
        v_1 = hmac.new(k_1, v_0, digest_fn).digest()
        k_2 = hmac.new(k_1, v_1 + b'\x01' + private_key_bytes + msg_hash, digest_fn).digest()
        v_2 = hmac.new(k_2, v_1, digest_fn).digest()

        kb = hmac.new(k_2, v_2, digest_fn).digest()
        k = int.from_bytes(kb, "big")
        return k
