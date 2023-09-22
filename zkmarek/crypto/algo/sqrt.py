from typing import Optional

from zkmarek.crypto.field_element import FieldElement


def has_sqrt(a: int, p: int):
    exp = (p - 1) // 2
    r = FieldElement(a, p) ** exp
    return r.value == 1


def find_pow2_divisor(q_1: int):
    assert q_1 > 0, "a must be positive"
    s = 0
    while (q_1 & 1) == 0:
        q_1 >>= 1
        s += 1
    return (s, q_1)


def find_two_pow_order(t: FieldElement, m: int):
    i = 1
    pow = 2
    while i < m:
        if t**pow == FieldElement(1, t.order):
            return i
        pow *= 2
        i += 1
    return i


def find_non_residue(p: int):
    zero = FieldElement(0, p)
    while True:
        z = FieldElement.random(p)
        if z != zero and not has_sqrt(z.value, p):
            return z


def tonelli_shanks_sqrt(el: FieldElement) -> Optional[FieldElement]:
    p = el.order
    (s, q) = find_pow2_divisor(p - 1)
    w = el ** ((q - 1) // 2)
    a0 = (w * w * el.value) ** (2 ** (s - 1))
    if a0 == FieldElement(-1, p):
        return None
    z = find_non_residue(p)
    m = s
    c = z**q
    t = el**q
    r = el ** ((q + 1) // 2)
    while True:
        if t == FieldElement(0, p):
            return FieldElement(0, p)
        elif t == FieldElement(1, p):
            return r
        i = find_two_pow_order(t, m)
        b = c ** (2 ** (m - i - 1))
        m = i
        c = b * b
        t = t * c
        r = r * b
