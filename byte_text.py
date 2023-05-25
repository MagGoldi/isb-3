import logging

logger = logging.getLogger()
logger.setLevel('INFO')


def byte_read_text(file_name: str) -> bytes:
    """
    This function reads text in byte form from txt file.

    :param file_name: name of txt file.
    :return: text in byte form.
    """
    try:
        with open(file_name, mode='rb') as text_file:
            text = text_file.read()
        logging.info(f' Text was successfully read from file {file_name}')
    except OSError as err:
        logging.warning(f' Text was not read from file {file_name}\n{err}')
    return text


def byte_write_text(text: bytes, file_name: str) -> None:
    """
    This function writes text in byte form to txt file.

    :param text: text for writing
    :param file_name: name of txt file.
    :return: None
    """
    try:
        with open(file_name, mode='wb') as text_file:
            text_file.write(text)
        logging.info(f' Text was successfully written to file {file_name}')
    except OSError as err:
        logging.warning(f' Text was not written to file {file_name}\n{err}')