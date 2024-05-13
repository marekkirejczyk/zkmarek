def generate_key_pair() -> (secret_key, public_key)


def ec_sign(message, secret_key) -> signature


def ec_verify(message, signature, public_key) -> bool


def ec_recover(message, signature) -> public_key
