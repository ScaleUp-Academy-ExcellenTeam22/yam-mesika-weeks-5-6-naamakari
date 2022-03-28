from typing import Iterable
from typing import List
from functools import reduce
from itertools import chain
from itertools import zip_longest


def append_list(item, separator):
    return item, separator


def join(*lists: Iterable, separator: str = '-') -> list:
    """
    Join all the lists to long list with separate sign between every two lists.
    :param lists: Between 0 to unknown numbers of lists.
    :param separator: A string to separate between every 2 lists, the default is '-'.
    :return: The newly created list.
    """
    # If there is no list at all.
    if not lists:
        return []
    # Create list of lists of the separator.
    separator_list = [[separator] for _ in range(len(lists))]
    union_list = [item+separator for item, separator in zip_longest(lists, separator_list)]
    return list(chain.from_iterable(union_list))[:-1]


if __name__ == '__main__':
    print(join([1, 2], [8], [9, 5, 6], separator='@'))
    print(join([1, 2], [8], [9, 5, 6]))
    print(join([1]))
    print(join())
