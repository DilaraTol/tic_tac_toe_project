"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    board = [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
    return board

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_X=0
    count_O=0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == X:
                count_X+=1
            elif board[i][j] == O:
                count_O+=1   
    if count_X == count_O:
        return X
    elif count_X > count_O:
        return O

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions=[]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                possible_actions.append((i,j))
    return possible_actions        

    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    copy_board= copy.deepcopy(board)
    i, j = action
    if copy_board[i][j] != EMPTY:
        raise Exception("Invalid move")
    copy_board[i][j] = player(board)
    return copy_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in [0,1,2]:
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
    for j in [0,1,2]:
        if board[0][j] == board[1][j] == board[2][j] != EMPTY:
            return board[0][j]

    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return None

    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    for i in range(len(board)):
        for j in board[i]:
            if j == EMPTY:
                return False
    return True



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)

    if current_player == X:
        best_value = -float('inf')
        best_move = None
        for action in actions(board):
            value = min_value(result(board, action))
            if value > best_value:
                best_value = value
                best_move = action
        return best_move

    else:
        best_value = float('inf')
        best_move = None
        for action in actions(board):
            value = max_value(result(board, action))
            if value < best_value:
                best_value = value
                best_move = action
        return best_move


def min_value(board):
    if terminal(board):
        return utility(board)
    v = float('inf')
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


def max_value(board):
    if terminal(board):
        return utility(board)
    v = -float('inf')
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

