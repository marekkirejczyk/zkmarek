def generate_key_pair() -> (secret_key, public_key)


def sing(message, secret_key) -> signature


def verify(message, signature, public_key) -> bool


def recover(message, signature) -> public_key
