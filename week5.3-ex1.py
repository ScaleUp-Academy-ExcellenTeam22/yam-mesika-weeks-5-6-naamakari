import re

START_PATH = r"C:\Users\97252\python\Notebooks\week05\\"
PATH = r"resources\logo.jpg"


def open_and_read_file() -> bytes:
    """
    This generator open binary file according the path up.
    :return: 1024 bytes from the file every yield.
    """
    try:
        with open(START_PATH + PATH, 'rb') as input_file:
            for binary_text in iter(lambda: input_file.read(1024), b''):
                yield binary_text
    except IOError as exception:
        raise IOError(exception)


def is_secret_message(text: bytes) -> list:
    """
    This function gets text and checks if it is ends with at least 5 case characters and a '!'.
    :param text: The text is bytes, so we will do casting to str.
    :return: The text ,if it's ends with at least 5 case characters and a '!' . Else, return empty string.
    """
    return re.findall(r'[a-z]{5,}[!]', str(text))


def main():
    """
    The main function is play the generator for opening the file
    and the check function to check if the text contains secret massage
    """
    try:
        generator_iterator = open_and_read_file()
        for element in generator_iterator:
            if b'!' in element:
                # Split by the delimiter '!', but then add it to use it in the regex.
                texts_end_with_exclamation_mark = [item+b'!' for item in element.split(b'!')]
                # The last element is the rest of the split and not end with '!'.
                for text in texts_end_with_exclamation_mark[:-1]:
                    secret_message = is_secret_message(text)
                    if secret_message:
                        [print(f"The secret massage is: {item}") for item in secret_message]
    except IOError as error:
        print(error)


if __name__ == "__main__":
    main()
