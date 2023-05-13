def has_sqrt(a, p):
    return (a ** ((p-1)//2)) % p == 1

def find_pow2_divisor(q_1):
    assert q_1 > 0, "a must be positive"
    s = 0
    while (q_1 & 1) == 0:
        q_1 >>= 1
        s += 1
    return (s, q_1)

