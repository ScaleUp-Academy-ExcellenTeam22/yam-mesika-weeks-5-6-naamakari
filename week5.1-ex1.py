import os


def files_start_with(directory_path: str) -> list:
    """
    Return list of the files, in the directory at the end of the path, start with 'deep'.
    :param directory_path: The directory path where we want to go through the files and check them.
    :return: The list of the files starts with 'deep'.
    """
    return [file for file in os.listdir(directory_path) if file.startswith("deep")]


def main():
    path = input("Enter a path please:\n")
    print(files_start_with(path))


if __name__ == '__main__':
    main()

