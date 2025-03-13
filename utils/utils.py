def line_to_dict(line, key_words):
    """
    This a method that takes a line and divides it into words.
    Each word is actually a key that goes into the dictionary
    and the value is the number of occurrences of the word.
    
    :param line:
    :param key_words:
    :return:
    """
    split_line = line.split(" ")
    for item in split_line:
        if item.capitalize():
            item = item.lower()
        if item[-1:] in (",", ".", "!", "\n", '"'):
            item = item[:-1]
        if item[0:1] == '"':
            item = item[1:]
        if item not in key_words.keys():
            key_words[item] = 1
        else:
            key_words[item] = key_words[item] + 1
    return key_words


def get_most_frequent_word(key_words: dict) -> tuple:
    """
     This method found the most frequent ket/value in dict
    :param key_words:
    :return: max_key, max_value
    """
    max_key = None
    max_value = 0

    for key, value in key_words.items():
        if value > max_value:
            max_value = value
            max_key = key

    #print(f"The most frequent word in the text is '{max_key} ', count: {max_value}")
    return max_key, max_value


def read_file(path):
    """
    open file to read
    :param path:
    :return:
    """
    try:
        f = open(path)
        lines = f.readlines()
        print(type(lines))
        print(lines)
        f.close()
        return lines
    except:
        print(f'Error occurred when opening {path} to read')


def write_line_to_file(path: str, new_line: str) -> None:
    """
          open file to write

    :param path:
    :param new_line:
    :return:
    """

    try:
        with open(path, 'w') as f:
            f.write(new_line + '\n')

        f.close()
    except:
        print(f'Error occurred when opening {path} to write')


def append_line_to_file(path: str, new_lines: str) -> None:
    """
    open file to add a new file
    :param path:
    :param new_lines:
    :return:
    """
    try:
        with open(path, 'a') as f:
            f.write(new_lines + '\n')
        f.close()
    except:
        print(f'Error occurred when opening {path} to append')
