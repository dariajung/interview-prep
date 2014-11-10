

"""
0 | 1 | 2
---------
3 | 4 | 5
---------
6 | 7 | 8
"""

"""
[0: [0, 1, 2]
 1: [0, 1, 2]
 2: [0, 1, 2]
]
"""

"""
(0, 0) | (0, 1) | (0, 2)
------------------------
(1, 0) | (1, 1) | (1, 2)
------------------------
(2, 0) | (2, 1) | (2, 2)
"""


class Player():
    def __init__(self, mark):
        self.mark = mark
        self.moves = []

    def update_moves(self, x, y):
        self.moves.append((x, y))


def check_victory(player, board):
    ways_to_win = [
        [(0, 0), (0, 1), (0, 2)]
        , [(1, 0), (1, 1), (1, 2)]
        , [(2, 0), (2, 1), (2, 2)]
        , [(0, 0), (1, 0), (2, 0)]
        , [(0, 1), (1, 1), (2, 1)]
        , [(0, 2), (1, 2), (2, 2)]
        , [(0, 0), (1, 1), (2, 2)]
        , [(0, 2), (1, 1), (2, 0)]
    ]

    count = 0

    for win in ways_to_win:
        for spot in win:
            if spot in player.moves:
                count += 1

        if count == 3:
            break
        else:
            count = 0

    if count == 3:
        print "Player %s wins!\n" % player.mark
        return True

    moves = 0
    # also look for ties
    for x in range(0, 3):
        for y in range(0, 3):
            if board[x][y] != " ":
                moves += 1

    if moves == 9:
        print "Game over as a tie! No one wins\n"
        return True


def legal_move(x, y, board):
    if x > len(board) or x < 0 or y > len(board) or y < 0:
        return False
    if board[x][y] != " ":
        return False
    else:
        return True


def new_board():
    return [[" " for row in range(3)] for col in range(3)]


def draw(board):
    """Display game board on screen."""
    print "\n-----\n".join("|".join(row) for row in board)


def move(player, x, y, board):
    # if legal, update the board
    # and return it, also return
    # True to state the player completed his/her turn
    if legal_move(x, y, board):
        board[x][y] = player.mark
        player.moves.append((x, y))
        return (True, board)

    # not legal, so do not update the board and
    # return False to state the player needs to
    # make a new move
    else:
        print "Illegal move! That place is taken\n"
        return (False, board)


def ask_input():
    var_x = int(raw_input("Input x coordinate\n"))
    var_y = int(raw_input("Input y coordinate\n"))

    return (var_x, var_y)


def game(player1, player2, board):

    current_player = player1

    while not check_victory(current_player, board):
        print "Board:\n"
        print "Current Player: %s" % current_player.mark
        draw(board)
        turn_complete = False

        while not turn_complete:
            (x, y) = ask_input()
            (turn_complete, new_board) = move(current_player, x, y, board)

        board = new_board
        if current_player == player1:
            current_player = player2
        else:
            current_player = player1


if __name__ == "__main__":
    board = new_board()
    player1 = Player(" X ")
    player2 = Player(" O ")

    game(player1, player2, board)
