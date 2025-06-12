def verifyMultiProof(opening ai, root c2, MultiProof [pi, c0, c1]):

    r = hash(c2, c1, c0, ai, hash(c0), hash(c1))
    g(x) = 0
    for i in [0, 1, 2]:  # for c0, c1, c2
        xi = point_of_evaluation[i]
        vi = value_at_point[i]
        pi(x) = corresponding_polynomial_for(ci)
        g(x) += r^i * (pi(x) - vi) / (x - xi)

    D = commit(g)

    s = hash(D, c0, c1, c2, ai, hash(c0), hash(c1))
    expected_value = g(s)

    is_valid = verifyOpening(D, s, expected_value, pi) # true/false

    return is_valid