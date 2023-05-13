from elliptic.crypto.field import Field


def has_sqrt(a, p):
    return (a ** ((p-1)//2)) % p == 1

def find_pow2_divisor(q_1):
    assert q_1 > 0, "a must be positive"
    s = 0
    while (q_1 & 1) == 0:
        q_1 >>= 1
        s += 1
    return (s, q_1)

def tonelli_shanks_sqrt(el: Field):
    p = el.order
    a = el.value
    (s, t) = find_pow2_divisor(p - 1)
    w = el ** ((t - 1) // 2)
    a0 = ((w*w*a) ** (2 ** (s - 1)))
    if a0 == Field(-1, p):
        return None
    return "Not yet implemented"

