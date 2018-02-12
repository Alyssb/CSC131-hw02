"""
CSC131 - Homework #2
Missouri State University, Spring 2018
File: hw02.py
Due Date: 24:59 Friday 16 February 2018
"""


def jump_it(board: list) -> int:
    """
    Calculate the lowest cost of the given board while playing "jump it."
    :param board: list representing playing board
    :return: The cheapest cost to play the game is returned.
    """
    # TODO: Implement me correctly.
    return 0


def read_boards_from_file(file_name: str) -> list:
    """
    Read a list of boards from the given input file.
    :param file_name: the name of the file containing board data
    :return: A list of game boards is returned.
    """
    # TODO: Implement me correctly. Notice you'll be returning a list of boards, i.e., a 2D-list.
    return [[]]


def main() -> int:
    boards = read_boards_from_file("./input.txt")
    for board in boards:
        print(jump_it(board))
    return 0


if __name__ == '__main__':
    main()
