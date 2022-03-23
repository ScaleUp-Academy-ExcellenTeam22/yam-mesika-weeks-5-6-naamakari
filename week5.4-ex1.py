import itertools


def interleave(*iterables) -> list:
    """
    The function pass all over the iterables and mixed all of them to one list
    :param iterables: the str,string,list etc.
    :return: list of the mixed iterables
    """
    return [item2 for item1 in itertools.zip_longest(*iterables) for item2 in item1 if item2]


def generator_interleave(*iterables):
    """
     A generator version of the function 'interleave'
    :param iterables: the str,string,list etc.
    :return: every play of the function return one item of the mixed iterables
    """
    for item1 in itertools.zip_longest(*iterables):
        for item2 in item1:
            if item2:
                yield item2


if __name__ == '__main__':
    print(interleave('abc', [1, 2, 3, 4], ('!', '@', '#')))
    generator = generator_interleave('abc', [1, 2, 3, 4], ('!', '@', '#'))
    print(list(generator))
