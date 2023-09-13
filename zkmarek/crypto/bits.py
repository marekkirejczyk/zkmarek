def bits(k: int):
    binary_string = bin(k)[2:]
    return [int(bit) for bit in binary_string][::-1]


def bits_lsb(k: int):
    binary_string = bin(k)[2:]
    return [int(bit) for bit in binary_string]


def truncate_bits(n: str, number_of_bits_to_truncate: int) -> int:
    assert n.startswith('0b')
    assert int(n, 2), "Incorrect binary string"
    return int(n[2:][:number_of_bits_to_truncate], 2)
