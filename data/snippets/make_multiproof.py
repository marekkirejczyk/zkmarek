def generateMultiProof(x_i, a_i, c2, VerklePath: List[ECPoint], polynomials: List[polynomial]) -> Tuple:
    c0, c1 = VerklePath
    r = hash(c2, c1, c0, a_i, hash(c0), hash(c1))

    opening_indices = [x_i, c0.index, c1.index]      
    opening_values = [a_i, hash(c0), hash(c1)]      

    g = polynomial.zero()
    
    for i in range(3):
        xi = opening_indices[i]
        vi = opening_values[i]
        p_i = polynomials[i]  
        g += (r ** i) * (p_i(x) - vi) / (x - xi)

    D = commit(g)

    s = hash(D, c0, c1, c2, a_i, hash(c0), hash(c1))
    value = g.evaluate(x, s)

    pi = generate_proof(D, s, value)

    return (pi, c0, c1)
