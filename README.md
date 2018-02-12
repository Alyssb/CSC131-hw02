## HW\#2: Using Recursion in a Game

The game of "Jump It" consists of a board with n positive integers in a row except for the first column, which always contains zero. These numbers represent the cost to enter each column. Here is a sample game board where n is 6:

```text
+--------------------------+
| 0 | 3 | 80 | 6 | 57 | 10 |
+--------------------------+
```

The object of the game is to move from the first column to the last column in the lowest total cost. The number in each column represents the cost to enter that column. You always start the game in the first column and have two types of moves. You can either move to the adjacent column or jump over the adjacent column to land two columns over. The cost of a game is the sum of the costs of the visited columns.

In the board shown above, there are several ways to get to the end. Starting in the first column, our cost so far is 0. We could jump to 80, then jump to 57, then move to 10 for a total of 80 + 57 + 10 = 147. However, a cheaper path would be to move to 3, jump to 6, then jump to 10, for a total cost of 3 + 6 + 10 = 19.

Write a recursive solution to this problem that computes the cheapest cost of the game and outputs this value for an arbitrary large game board represented as a list. Because the program can take long time to run on large boards, you can assume that a board size is at most 50 columns. Your program doesn't have to output the actual sequence of moves, only compute the cheapest cost of this sequence. 

Your program must read input from a text file named `input.txt` and must send output to `stdout` (the computer's screen). This effectively, is accomplished by the `main()` function which is already written for you, i.e., _don't change_ `main()`.

### Tasks

You have two functions to implement:

1. `read_boards_from_file(file_name: str):` This function reads the data from the given input file and returns a list of boards specified in the given data file. Notice, a list of boards means it's a two-dimensional list.
1. `jump_it(board: list):` This function computes the cheapest cost for the given board. As such, this function simply returns an `int`, namely, the calculated cost. You'll implement this function using _recursion_.

The input file consists of a sequence of lines, where each line corresponds to a board. The numbers, separated by a space, on a line are the costs to enter the columns on the board. For example, the above board is represented in the input file as

```text
0 3 80 6 57 10
```

Sample input file is as follows:

```text
0 3 80 6 57 10 
0 98 7 44 25 3 5 85 46 4 
0 57 59 83 9 42 70 
0 20 49 96 53 7 43 77 
0 24 17 15 61 49 61 8 65 43 26 99 7 57 97 50 93 6 82 52
```

When the two functions you are responsible for implementing are implemented correctly, running `main()` will result in the corresponding output as follows:

```text
19
87
138
186
330
```

That is, 

```python
jump_it([0, 3, 80, 6, 57, 10]) == 19
jump_it([0, 98, 7, 44, 25, 3, 5, 85, 46, 4]) == 87
```

and so on and so forth.

### Submission Details

The usual assignment protocol is followed:

1. Accept this assignment using the URL found in the Blackboard assignment which creates your repository in your GitHub account.
1. Clone your repository and create a branch named `develop` within which to do your work.
1. Implement the code indicated by the `# TODO:` comments.
1. Minimally make commits after finishing each function; more commits are encouraged but not required.
1. Once all the unit tests pass, push your final commit to GitHub and create a pull request, requesting to merge your `develop` branch into your `master` branch.
1. After the pull request is created, copy the URL of the pull request and paste it into a Text Submission on Blackboard. You should make the URL a _working hyperlink_ that opens the pull request in a new browser window. NOTE: The assignment is officially submitted by the act of creating and submitting this Blackboard Text Submission and it is the timestamp of that activity that dictates when your assignment was actually submitted.

### Due Date

Your assignment must be submitted to Blackboard by **24:59 Friday 16 February 2018**.
