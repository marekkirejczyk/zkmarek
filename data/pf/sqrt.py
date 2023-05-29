def tonelli_shanks_sqrt(el: Field) -> Optional[Field]:
    p = el.order
    (s, q) = find_pow2_divisor(p - 1)
    w = el ** ((q - 1) // 2)
    a0 = (w * w * el.value) ** (2 ** (s - 1))
    if a0 == Field(-1, p):
        return None
    z = find_non_residue(p)
    m = s
    c = z**q
    t = el**q
    r = el ** ((q + 1) // 2)
    while True:
        if t == Field(0, p):
            return Field(0, p)
        elif t == Field(1, p):
            return r
        i = find_two_pow_order(t, m)
        b = c ** (2 ** (m - i - 1))
        m = i
        c = b * b
        t = t * c
        r = r * b
