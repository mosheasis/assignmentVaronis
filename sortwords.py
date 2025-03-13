import argparse
from datetime import datetime
import os
from file_handling.files import File
from utils.utils import get_most_frequent_word, line_to_dict


def parse_args(argv: str | None = None) -> tuple:
    op_sort = ('sort-a', 'sort-d')
    parser = argparse.ArgumentParser(description="The program is to sort words from specific file", prog="prog")
    parser.add_argument('path', type=dir_path, help="path of input file")
    args = parser.parse_args(argv)

    while True:
        options = input("enter your options [sort-a,sort-d]:")
        if options == "" or options not in op_sort:
            print("No input provided")
        else:
            break
    return args, options


def dir_path(path: str) -> str:
    """
    This method performs input file path validation.
    :param path:
    :return:

    """

    if os.path.exists(path):
        return path
    else:
        raise argparse.ArgumentTypeError(f"readable_dir:{path} is not a valid path")


def options_sort_result(option: str) -> bool:
    """
    This method chooses the sort order.
    sort-a (assenting) --> a-z
    sort-d (descending) --> z-a
    :param option:(sort-a or sort-d)
    :return: reverse [bool]
    """

    reverse = False
    if option == "sort-d":
        reverse = True
    elif option == "sort-a":
        reverse = False
    return reverse


def main(argv: list[str] | None = None) -> None:
    key_words = {}
    # 1. input parameters
    args, options = parse_args(argv)
    print(f"File is {args.path} and sort type is {options} ")
    # 2. Define sort order
    reverse = options_sort_result(options)
    # 3. Read input file
    try:
        file_to_read = File(args.path)
        lines = file_to_read.read()
        # print(f"lines {lines}")
        # 4. convert words to key and count words
        for line in lines:
            key_words = line_to_dict(line, key_words)
        # print(key_words)
        # 5. get_most_frequent_word
        max_key, max_value = get_most_frequent_word(key_words)
        # 6. sort key word and join list to string
        new_line = ' '.join(sorted(key_words.keys(), key=str.lower, reverse=reverse))
        timestamp = datetime.now().timestamp()
        # 7. save results to file
        file_to_write = File(f"f2_{str(timestamp)}.txt")
        file_to_write.write(new_line)
        file_to_write.add_line(f"The most frequent word in the text is '{max_key}', count: {max_value}")
        print(f"The file f2_{str(timestamp)}.txt has been created.")
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")


if __name__ == "__main__":
    main()
