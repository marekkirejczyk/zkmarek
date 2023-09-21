import hashlib
import secrets
from dataclasses import dataclass

from zkmarek.crypto.standard import Standard


@dataclass(frozen=True)
class ECDSASignature:
    r: int
    s: int
    v: int

    @staticmethod
    def sign(standard: Standard, secret_key: int, msg: bytes) -> 'ECDSASignature':
        msg_hash = hashlib.sha256(msg).digest()
        r = 0
        s = 0
        v = 0
        while r == 0 or s == 0:
            k = secrets.randbits(256)
            r, s, v = standard.sign(secret_key, int.from_bytes(msg_hash, 'big'), k)
        return ECDSASignature(r, s, v)

    # https://en.bitcoin.it/wiki/BIP_0062#DER_encoding
    def to_der(self) -> bytes:

        def encode_int(n: int) -> bytes:
            hex_n = hex(n)[2:]
            if len(hex_n) % 2 == 1:
                hex_n = '0' + hex_n
            bytes_n = bytes.fromhex(hex_n)
            if bytes_n[0] >= 0x80:
                bytes_n = b'\x00' + bytes_n
            return b'\x02' + len(bytes_n).to_bytes(1, 'big') + bytes_n

        remaining = encode_int(self.r) + encode_int(self.s)

        return b'\x30' + len(remaining).to_bytes(1, 'big') + remaining

    def to_hex_encoding(self) -> str:
        return f'{self.r:x}{self.s:x}{self.v:x}'
