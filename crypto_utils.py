from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def encrypt_message(message, key):

    cipher = AES.new(key, AES.MODE_EAX)

    ciphertext, tag = cipher.encrypt_and_digest(
        message.encode()
    )

    return (
        cipher.nonce.hex(),
        tag.hex(),
        ciphertext.hex()
    )


def decrypt_message(
    nonce,
    tag,
    ciphertext,
    key
):

    nonce = bytes.fromhex(nonce)
    tag = bytes.fromhex(tag)
    ciphertext = bytes.fromhex(ciphertext)

    cipher = AES.new(
        key,
        AES.MODE_EAX,
        nonce=nonce
    )

    plaintext = cipher.decrypt_and_verify(
        ciphertext,
        tag
    )

    return plaintext.decode()