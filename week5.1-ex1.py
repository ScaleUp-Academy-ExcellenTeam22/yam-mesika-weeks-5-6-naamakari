import os


def path_fun(path):
    lst_files = []
    files = os.listdir(path)  # get all the files in the directory in the end of the path
    for file in files:
        if file.startswith("deep"):
            lst_files.append(file)
    return lst_files


def main():
    path = input("Enter path please:\n")
    path_fun(path)


if __name__ == '__main__':
    main()

