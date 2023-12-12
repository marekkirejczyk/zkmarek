# n = group_order
# R = group_generator * k
def sign(secret_key: int, msg_hash: int, k: int) -> tuple[int, int, int]:
    r: int = R.x.value % n
    s = (pow(k, -1, n) * (msg_hash + (r * int(hex(secret_key), 16)))) % n
    v = R.y.value % 2

    if s * 2 >= n:
        s = n - s
        v ^= 1

    return r, s, 27 + v
