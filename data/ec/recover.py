def recover(z: int, r: int, s: int, v: int) -> Optional[ECAffine]:
    n = group_order
    R = ECAffine.from_x(r, v, curve)
    if R is None:
        return None
    else:
        r_inverse = pow(r, -1, n)
        u1 = -z * r_inverse % n
        u2 = s * r_inverse % n
        QA = generator * u1 + R * u2
        return QA
