from typing import Tuple

def extended_euclid(prev_r: int, r: int) -> Tuple[int, int, int, int, int]:
    assert prev_r >= r
    prev_s, s = 1, 0
    prev_t, t = 0, 1
    while (r != 0):
        quotient = prev_r // r
        prev_r, r = r, prev_r - quotient * r
        prev_s, s = s, prev_s - quotient * s
        prev_t, t = t, prev_t - quotient * t
    return (prev_r, abs(t), abs(s), prev_t, prev_s)
