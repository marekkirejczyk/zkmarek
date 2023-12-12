def generate_key_pair(security_param, randomness) ->
    (secret_key, public_key)


def ecsing(message, secret_key) -> signature


def ecverify(message, signature, public_key) -> bool


def ecrecover(message, signature) -> public_key
