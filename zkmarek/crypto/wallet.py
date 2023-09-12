from Crypto.Hash import keccak

from zkmarek.crypto.ec_affine import ECAffine
from zkmarek.crypto.standard import Secp256


class Wallet:
    secret_key: str

    def __init__(self, secret_key: str):
        self.secret_key = secret_key

    def get_address(self) -> str:
        public_key: ECAffine = Secp256.generate_public_key(int(self.secret_key, 16))
        hash_input = public_key.serialize_uncompressed()
        k = keccak.new(digest_bits=256)
        k.update(bytes.fromhex(hash_input))
        return '0x' + k.hexdigest()[-40:]
