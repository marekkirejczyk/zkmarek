def double_and_add(self, k: int):
    for bit in bits(k):
        if bit == 1:
            result = result + tmp
        tmp = tmp.double()
    return result
