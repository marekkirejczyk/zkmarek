from Crypto.Hash import keccak

MESSAGE_PREFIX: str = "\x19Ethereum Signed Message:\n"

def hash_message(msg: str) -> str:
    prefix = MESSAGE_PREFIX.encode('utf-8')
    msg_len = str(len(msg)).encode('utf-8')
    message = msg.encode('utf-8')
    payload = b''.join([prefix, msg_len, message])
    k = keccak.new(digest_bits=256)
    k.update(payload)
    return k.hexdigest()
