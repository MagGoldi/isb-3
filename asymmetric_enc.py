import logging

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

logger = logging.getLogger()
logger.setLevel('INFO')


def gen_private_public_key() -> tuple:
    """
    This function generates an asymmetric key for asymmetric encryption algorithm.

    :return: asymmetric key.
    """
    keys = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    private_key = keys
    public_key = keys.public_key()
    logging.info(f' Asymmetric keys successfully generated')
    return private_key, public_key


def asymmetric_encrypt(public_key, text: bytes) -> bytes:
    """
    This function encrypts an input text using public key.

    :param public_key: public key of asymmetric encryption algorithm.
    :param text: text for encryption.
    :return: encrypted text.
    """
    cipher_text = public_key.encrypt(text,
                                     padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                  algorithm=hashes.SHA256(), label=None))
    logging.info(' Asymmetric encryption was successful')
    return cipher_text


def asymmetric_decrypt(private_key, cipher_text: bytes) -> bytes:
    """
    This function decrypts an asymmetrical ciphertext using private key.

    :param private_key: private key of asymmetric encryption algorithm.
    :param cipher_text: ciphertext.
    :return: decrypted text.
    """
    text = private_key.decrypt(cipher_text,
                               padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                            algorithm=hashes.SHA256(),
                                            label=None))
    logging.info(' Asymmetric decryption was successful')
    return text
