def make_multiproof(transcript: Transcript, queries: List[ProverQuery]):

    for query in queries:
        transcript.append_point(query.C, b"C")
        transcript.append_scalar(query.x_i, b"x_i")
        transcript.append_scalar(query.a_i, b"a_i")

    r = transcript.challenge_scalar(b"r")

    g = [Fr.zero() for _ in range(query.C.size())]
    power_of_r = Fr.one()

    for query in queries:
        p = query.p
        index = query.x_i
        a_i = p[index]

        q = compute_quotient(p, index, a_i)

        for i in range(query.C.size()):
            g[i] += power_of_r * q[i]

        power_of_r *= r

    D = commit(g)
    transcript.append_point(D, b"D")

    t = transcript.challenge_scalar(b"t")

    ipa_commitment = D 

    ipa_query = IPAProverQuery(g, ipa_commitment, t)
    ipa_proof = make_ipa_proof(transcript, ipa_query)

    return Proof(ipa_proof, D)
