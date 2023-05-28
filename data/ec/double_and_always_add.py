def double_and_always_add(self, k: int):
    tmp = self
    result = self.infinity()
    for bit in bits_lsb(k, pad_to=256):
        result = result.double()
        tmp = result + self
        one = result * (1-bit)
        two = tmp * bit
        result =  one + two
    return result
