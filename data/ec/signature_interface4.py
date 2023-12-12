def generate_key_pair() -> (secret_key: Scalar, public_key: ECPoint)


def ec_sing(
        message: Scalar,
        secret_key: Scalar
) -> signature: (r: Scalar, s: Scalar, v: ?)


def ec_verify(
        message: Scalar,
        signature: (r: Scalar, s: Scalar, v: ?),
        public_key: ECPoint
) -> bool


def ec_recover(
        message: Scalar,
        signature: (r: Scalar, s: Scalar, v: ?)
) -> public_key: ECPoint
