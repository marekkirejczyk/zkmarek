from dataclasses import dataclass


@dataclass(frozen=True)
class ECDSASignature:
    r: int
    s: int

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
