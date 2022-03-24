import os


def files_start_with(directory_path):
    """ Return list of the files, in the directory at the end of the path, start with deep"""
    files = os.listdir(directory_path)  # get all the files in the directory in the end of the path
    files_list = [file for file in files if file.startswith("deep")]
    return files_list


def main():
    path = input("Enter a path please:\n")
    print(files_starts_with(path))


if __name__ == '__main__':
    main()

