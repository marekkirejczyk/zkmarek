def generate_key_pair() -> (secret_key: Scalar, public_key: ECPoint)


def ecsing(message: Scalar, secret_key: Point) -> signature: (r: Scalar, s: Scalar, v: ?)


def ecverify(message: Scalar, signature: (r: Scalar, s: Scalar, v: ?), public_key: ECPoint) -> bool


def ecrecover(message: Scalar, signature: (r: Scalar, s: Scalar, v: ?),) -> public_key: ECPoint
