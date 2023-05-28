def bits(k: int):
    binary_string = bin(k)[2:]
    return [int(bit) for bit in binary_string][::-1]

def bits_lsb(k: int):
    binary_string = bin(k)[2:]
    return [int(bit) for bit in binary_string]
