def cswap(bit, R, S):
    dummy = bit * (R - S) # 0 or (R - S)
    R = R  - dummy # R = R - 0 or R - (R - S) = S
    S = S  + dummy # S = S + 0 or S + (R - S) = R
    return (R, S)
