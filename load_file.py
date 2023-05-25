import logging
import json

from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key

logger = logging.getLogger()
logger.setLevel('INFO')


def load_settings(settings_file: str) -> dict:
    """
    This function loads the settings from a file in JSON format

    :param settings_file: name of settings file.
    :return: setting after verification.
    """
    settings = None
    try:
        with open(settings_file) as json_file:
            settings = json.load(json_file)
        logging.info(f"Settings file successfully loaded from file {settings_file}")
    except OSError as err:
        logging.warning(f"Settings file was not loaded from file {settings_file}\n{err}")
    return settings

def load_symmetric_key(file_name: str) -> bytes:
    """
    This function loads  a symmetric key from txt file.

    :param file_name: name of txt file.
    :return: symmetric key for symmetric encoding algorithm.
    """
    try:
        with open(file_name, mode='rb') as key_file:
            key = key_file.read()
        logging.info(f' Symmetric key successfully loaded from {file_name}')
    except OSError as err:
        logging.warning(f' Symmetric key was not loaded from file {file_name}\n{err}')
    return key


def load_private_key(private_pem: str):
    """
    This function loads a private key from pem file.

    :param private_pem: name of pem file.
    :return: private key for asymmetric encoding algorithm.
    """
    private_key = None
    try:
        with open(private_pem, 'rb') as pem_in:
            private_bytes = pem_in.read()
        private_key = load_pem_private_key(private_bytes, password=None)
        logging.info(f' Private key successfully loaded from {private_pem}')
    except OSError as err:
        logging.warning(f' Private key was not loaded from file {private_pem}\n{err}')
    return private_key


def load_public_key(public_pem: str):
    """
    This function loads a public key from pem file.

    :param public_pem: name of pem file.
    :return: public key for asymmetric encoding algorithm.
    """
    public_key = None
    try:
        with open(public_pem, 'rb') as pem_in:
            public_bytes = pem_in.read()
        public_key = load_pem_public_key(public_bytes)
        logging.info(f' Public key successfully loaded from {public_pem}')
    except OSError as err:
        logging.warning(f' Public key was not loaded from file {public_pem}\n{err}')
    return public_key
