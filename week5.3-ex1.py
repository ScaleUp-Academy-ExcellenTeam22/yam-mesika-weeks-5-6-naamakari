START_PATH = r"C:\Users\97252\python\Notebooks\week05\\"
PATH = r"resources\logo.jpg"


def open_and_read_from_file():
    """
    This generator open binary file according the path up
    :return: 1024 bytes from the file every yield
    """
    try:
        with open(START_PATH+PATH, 'rb') as input_file:
            for binary_text in iter(lambda: input_file.read(1024), b''):
                yield binary_text
    except IOError:
        print("Error: can't open the file")


def is_secret_message(text: bytes) -> (bool, str):
    """
    This function get text and checks if it is end with just lower characters, at least 5
    :param text: the text is bytes, so we will do casting to str
    :return: bool- if is just lower characters and at least 5. And if so, return this text- str
    """
    str_text = str(text)
    message = []
    for item in str_text[:-1][::-1]:  # reverse the text to check from the end, and cut the last char, that is "
        if item.islower():
            message.insert(0, item)
        elif len(message) >= 5:
            return True, "".join(message)
        else:
            return False, None
    if len(message) >= 5:
        return True, "".join(message)
    else:
        return False, None


def main():
    """
    The main function is play the generator and the check function
    :return: nothing. Prints the secret messages the function found
    """
    generator_iterator = open_and_read_from_file()  # create the generator
    for element in generator_iterator:  # pass over the elements in the generator
        if b'!' in element:
            texts_end_with_exclamation_mark = element.split(b'!')
            # the last element is the rest of the split and not end with '!'
            for text in texts_end_with_exclamation_mark[:-1]:
                is_secret, secret_message = is_secret_message(text)
                if is_secret:
                    print(f"This is the secret message: {secret_message}")


if __name__ == "__main__":
    main()
