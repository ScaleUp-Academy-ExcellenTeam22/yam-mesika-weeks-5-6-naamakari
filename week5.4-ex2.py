import os
import re

BOOK_PATH = r'C:\Users\97252\python\Notebooks\week05\resources\potter2'


def change_chapter_name(number: str, new_name: str, old_name: str):
    """
    The function rename the name of the file to the new name
    :param number: the new number of the current chapter
    :param new_name: the new name of the current chapter
    :param old_name: the old name of the file, to know which file to rename
    :return: nothing
    """
    number = number.zfill(3)  # making the number of the number of 3 digits
    # replace the ':' in the name of the chapter because it can't be in the name of the file
    new_name = new_name.replace(':', "-")
    new_name = number + ' ' + new_name
    new_name = BOOK_PATH+'\\'+new_name+'.html'
    old_name = BOOK_PATH+'\\'+old_name
    try:
        os.rename(old_name,  new_name)
    except FileNotFoundError:
        print(f"FileNotFoundError: The system cannot find the file specified: '{old_name}' -> '{new_name}'")
    except OSError as error:
        print(error)


def extract_number_and_name_of_chapter(title: str) -> (str, str):
    """
    The function extracts the real name and number of the chapter from the HTML file
    :param title: The line where the real name and number of the chapter are
    :return: the number and the name that were found
    """
    title_name = re.search('<title>(.+?)</title>', title)
    if title_name:
        new_title_name = title_name.group(1)
        chapter_number = new_title_name[new_title_name.find('Chapter')+8:new_title_name.find(':'):]
        chapter_name = new_title_name[new_title_name.find(':')+2:]
        return chapter_number, chapter_name
    return None, None


def open_html_files(file: str) -> list:
    """
    The function opens the file and reads from it
    :param file: the name of the file
    :return: The contents of the file whose name we received as an argument
    """
    with open(BOOK_PATH + '\\' + file, 'r', encoding='utf-8') as chapter:
        return chapter.readlines()


def main():
    """
    The main function pass all over the files and rename the names of the files
    :return: nothing
    """
    for file in os.listdir(BOOK_PATH):
        context_chapter = open_html_files(file)
        for line in context_chapter:
            if line.startswith('<title>'):
                number, new_name = extract_number_and_name_of_chapter(line)
                if number and new_name:
                    change_chapter_name(number, new_name, file)

    print("well done")


if __name__ == '__main__':
    main()

