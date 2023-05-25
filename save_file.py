import logging

from cryptography.hazmat.primitives import serialization

logger = logging.getLogger()
logger.setLevel('INFO')

def save_symmetric_key(key: bytes, file_name: str) -> None:
    """
    This function saves a symmetric key to txt file.

    :param key: symmetric key for symmetric encryption algorithm.
    :param file_name: name of txt file.
    :return: None.
    """
    try:
        with open(file_name, 'wb') as key_file:
            key_file.write(key)
        logging.info(f' Symmetric key successfully saved to {file_name}')
    except OSError as err:
        logging.warning(f' Symmetric key was not saved to file {file_name}\n{err}')


def save_asymmetric_keys(private_key, public_key, private_pem: str, public_pem: str) -> None:
    """
    This function saves a private key and a public key to pem files.

    :param private_key: private key for asymmetric encoding algorithm.
    :param public_key: public key for asymmetric encoding algorithm.
    :param private_pem: pem file for private key.
    :param public_pem: pem file for public key.
    :return: None
    """
    try:
        with open(private_pem, 'wb') as private_out:
            private_out.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                                        format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                        encryption_algorithm=serialization.NoEncryption()))
        logging.info(f' Private key successfully saved to {private_pem}')
    except OSError as err:
        logging.warning(f' Private key was not saved to file {private_pem}\n{err}')
    try:
        with open(public_pem, 'wb') as public_out:
            public_out.write(public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                                     format=serialization.PublicFormat.SubjectPublicKeyInfo))
        logging.info(f' Public key successfully saved to {public_pem}')
    except OSError as err:
        logging.warning(f' Public key was not saved to file {public_pem}\n{err}')