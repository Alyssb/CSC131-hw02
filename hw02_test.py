import unittest
from hw02 import jump_it
from hw02 import read_boards_from_file

board1 = [0, 3, 80, 6, 57, 10]
board2 = [0, 98, 7, 44, 25, 3, 5, 85, 46, 4]
board3 = [0, 57, 59, 83, 9, 42, 70]
board4 = [0, 20, 49, 96, 53, 7, 43, 77]
board5 = [0, 24, 17, 15, 61, 49, 61, 8, 65, 43, 26, 99, 7, 57, 97, 50, 93, 6, 82, 52]
test_file1 = "./test_input1.txt"
test_file2 = "./test_input2.txt"
test_file3 = "./test_input3.txt"
test_file4 = "./test_input4.txt"
test_file5 = "./test_input5.txt"


class MyTestCase(unittest.TestCase):
    def test_jump_it_board1(self):
        expected_result = 19
        actual_result = jump_it(board1)
        self.assertEqual(expected_result, actual_result)

    def test_jump_it_board2(self):
        expected_result = 87
        actual_result = jump_it(board2)
        self.assertEqual(expected_result, actual_result)

    def test_jump_it_board3(self):
        expected_result = 138
        actual_result = jump_it(board3)
        self.assertEqual(expected_result, actual_result)

    def test_jump_it_board4(self):
        expected_result = 186
        actual_result = jump_it(board4)
        self.assertEqual(expected_result, actual_result)

    def test_jump_it_board5(self):
        expected_result = 330
        actual_result = jump_it(board5)
        self.assertEqual(expected_result, actual_result)

    def test_read_boards_from_file1(self):
        """
        Validate that reading an empty file returns an empty list.
        :return: None
        """
        expected_result = []
        actual_result = read_boards_from_file(test_file1)
        self.assertListEqual(expected_result, actual_result)

    def test_read_boards_from_file2(self):
        """
        Validate that reading a single board is still returns a list of boards.
        :return: None
        """
        expected_result = [board2]
        actual_result = read_boards_from_file(test_file2)
        self.assertListEqual(expected_result, actual_result)

    def test_read_boards_from_file3(self):
        """
        Validate that reading an input file without a new line at the end of the last line is not problematic.
        :return:
        """
        expected_result = [[0, 3, 80, 6, 57, 10],
                           [0, 98, 7, 44, 25, 3, 5, 85, 46, 4],
                           [0, 57, 59, 83, 9, 42, 70],
                           [0, 20, 49, 96, 53, 7, 43, 77],
                           [0, 24, 17, 15, 61, 49, 61, 8, 65, 43, 26, 99, 7, 57, 97, 50, 93, 6, 82, 52]]
        actual_result = read_boards_from_file(test_file3)
        self.assertListEqual(expected_result, actual_result)

    def test_read_boards_from_file4(self):
        """
        Validates that new line at the end of the data file doesn't generate an empty board.
        :return: None
        """
        expected_result = [[0, 3, 80, 6, 57, 10],
                           [0, 98, 7, 44, 25, 3, 5, 85, 46, 4],
                           [0, 57, 59, 83, 9, 42, 70],
                           [0, 20, 49, 96, 53, 7, 43, 77],
                           [0, 24, 17, 15, 61, 49, 61, 8, 65, 43, 26, 99, 7, 57, 97, 50, 93, 6, 82, 52]]
        actual_result = read_boards_from_file(test_file4)
        self.assertListEqual(expected_result, actual_result)

    def test_read_boards_from_file5(self):
        """
        Validates that blank lines aren't converted into empty board games.
        :return: None
        """
        expected_result = [[0, 3, 80, 6, 57, 10],
                           [0, 98, 7, 44, 25, 3, 5, 85, 46, 4],
                           [0, 57, 59, 83, 9, 42, 70],
                           [0, 20, 49, 96, 53, 7, 43, 77],
                           [0, 24, 17, 15, 61, 49, 61, 8, 65, 43, 26, 99, 7, 57, 97, 50, 93, 6, 82, 52]]
        actual_result = read_boards_from_file(test_file5)
        self.assertListEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
