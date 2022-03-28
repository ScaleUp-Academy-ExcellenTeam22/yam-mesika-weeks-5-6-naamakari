import os
import re
from typing import Tuple

BOOK_PATH = r'C:\Users\97252\python\Notebooks\week05\resources\potter3'


def change_chapter_name(number: str, new_name: str, old_name: str):
    """
    The function rename the name of the file to the new name.
    :param number: The new number of the current chapter.
    :param new_name: The new name of the current chapter.
    :param old_name: The old name of the file, to know which file to rename.
    """
    # The replace function replace the ':' in the name of the chapter because it can't be in the name of the file.
    new_name = BOOK_PATH + "\\" + number.zfill(3) + " " + new_name.replace(":", "-") + ".html"
    old_name = BOOK_PATH + "\\" + old_name
    try:
        os.rename(old_name,  new_name)
    except FileNotFoundError as exception:
        raise FileNotFoundError(exception)
    except OSError as exception:
        raise OSError(exception)


def extract_number_and_name_of_chapter(title: str) -> Tuple[str, str]:
    """
    The function extracts the real name and number of the chapter from the HTML file.
    :param title: The line where the real name and number of the chapter are.
    :return: The number and the name that were found.
    """
    title_name = re.search('<title>(.+?)</title>', title)
    if title_name:
        new_title_name = title_name.group(1)
        # Slicing the number of the chapter from the title line, the number is after the word 'Chapter'
        chapter_number = new_title_name[new_title_name.find("C") + 8:new_title_name.find(":"):]
        chapter_name = new_title_name[new_title_name.find(":") + 2:]
        return chapter_number, chapter_name
    # If the title variable does not have the appropriate regex
    return "", ""


def open_html_files(file: str) -> list:
    """
    The function opens the file and reads from it.
    :param file: The name of the file.
    :return: The contents of the file whose name we received as an argument.
    """
    with open(BOOK_PATH + "\\" + file, "r", encoding="utf-8") as chapter:
        return chapter.readlines()


def main():
    """
    The main function pass all over the files and rename the names of the files.
    """
    for file in os.listdir(BOOK_PATH):
        context_chapter = open_html_files(file)
        for line in context_chapter:
            if line.startswith("<title>"):
                number, new_name = extract_number_and_name_of_chapter(line)
                if number and new_name:
                    try:
                        change_chapter_name(number, new_name, file)
                    except FileNotFoundError as error:
                        print(error)
                    except OSError as error:
                        print(error)
    print("well done")


if __name__ == '__main__':
    main()


