"""
Tic Tac Toe Player
"""

import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    x_count = 0
    o_count = 0

    # Count number of X and O
    for row in board:
        for cell in row:
            if cell == X:
                x_count += 1
            elif cell == O:
                o_count += 1

    # Return X if X has less moves than O
    if x_count <= o_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    # Create a set of all possible actions
    possible_actions = set()

    # If the game is already over, return an empty set
    if terminal(board):
        return possible_actions

    # Iterate through the board
    for i in range(len(board)):
        print(board)
        print(i)
        for j in range(len(board[i])):
            print(board[i])
            print(j)
            # If the cell is empty, add the correcsponding (i, j) tuple to the set of possible actions
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    # If the action is not valid, raise an exception
    if action not in actions(board):
        raise ValueError("Invalid action")

    # Create a deep copy of the board to avoid modifying the original board
    new_board = copy.deepcopy(board)

    # Determine the current player
    current_player = player(board)

    # Update the new board with the action taken by the current player
    i, j = action
    new_board[i][j] = current_player

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # Check rows
    for row in board:
        if row[0] == row[1] == row[2]:
            return row[0]

    # Check columns
    for i in range(len(board)):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != None:
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != None:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != None:
        return board[0][2]

    # If no winner, return None
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # If the game is over, either because someone has won the game or because all cells have been filled without anyone winning, the function should return True.
    if winner(board) != None:
        return True

    # If the game is still in progress, the function should return False.
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False

    # If the board is filled and there is no winner, the game is over
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None

    def max_value(board):
        if terminal(board):
            return utility(board)

        value = -math.inf
        for action in actions(board):
            value = max(value, min_value(result(board, action)))
        return value

    def min_value(board):
        if terminal(board):
            return utility(board)

        value = math.inf
        for action in actions(board):
            value = min(value, max_value(result(board, action)))
        return value

    # Determine the current player
    current_player = player(board)

    # Determine the optimal action for the current player
    if current_player == X:
        optimal_action = max(
            actions(board), key=lambda action: min_value(result(board, action)))
    else:
        optimal_action = min(
            actions(board), key=lambda action: max_value(result(board, action)))

    return optimal_action
