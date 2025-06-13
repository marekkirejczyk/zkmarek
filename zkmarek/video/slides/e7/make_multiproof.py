from typing import List, Callable

from typing import NamedTuple

class ECPoint(NamedTuple):
    x: int
    y: int
x = 5

def hash(*args):
    return sum(hash(str(a)) for a in args) % (2**256)

def commit(polynomial_expr):
    return f"commit({polynomial_expr})"

def open(commitment, point, value):
    return f"proof_at_{point}_for_{value}"

class MultiProof:
    def __init__(self, pi, c0, c1):
        self.pi = pi
        self.c0 = c0
        self.c1 = c1

def generateMultiProof(x_i, a_i, c2, pathCommitments: List[ECPoint], polynomials: List[Callable]):
    c0, c1 = pathCommitments
    r = hash(c2, c1, c0, a_i, hash(c0), hash(c1))

    opening_indices = [x_i, c0.index, c1.index]      
    opening_values = [a_i, hash(c0), hash(c1)]      

    g = 0
    for i in range(3):
        xi = opening_indices[i]
        vi = opening_values[i]
        p_i = polynomials[i]  
        g += (r**i) * (p_i(x) - vi) / (x - xi)

    D = commit(g)

    s = hash(D, c0, c1, c2, a_i, hash(c0), hash(c1))
    value = g.subs(x, s)

    pi = open(D, s, value)

    return MultiProof(pi, c0, c1)
