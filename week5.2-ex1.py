
def join(*lists, separator='-'):
    """Join all the lists to long list with separate sign between every list"""
    if not lists:  # if there is no list at all
        return None
    # join the first list and then add the separator and the rest of the lists in loop
    new_list = [element for element in lists[0]]
    for current_list in lists[1:]:
        new_list += separator
        new_list += [element for element in current_list]
    return new_list


if __name__ == '__main__':
    print(join([1, 2], [8], [9, 5, 6], separator='@'))
    print(join([1, 2], [8], [9, 5, 6]))
    print(join([1]))
    print(join())
