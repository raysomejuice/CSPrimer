BOARD_POSITIONS = [['', '', ''], 
                   ['', '', ''], 
                   ['', '', '']]


def draw_board(board: list[list[str]]) -> None:
    pass

def make_move(piece: str, location: int, board: list[list[str]]) -> bool:
    row = location // 3
    col = location % 3
    if not board[row][col]:
        board[row][col] = piece
        return True

    return False

def find_winner(piece: str, board: list[list[str]]) -> str:
    # (location: int,) An input argument if using commented code
    # row = location // 3
    # prev_row = (row - 1) % 3
    # next_row = (row + 1) % 3
    # col = location % 3
    # prev_col = (col - 1) % 3
    # next_col = (col + 1) % 3
    # diagonal_desc = set([0, 4, 8])
    # diagonal_asc = set([2, 4, 6])

    # if board[row][prev_col] == board[row][col] == board[row][next_col] == piece or \
    #     board[prev_row][col] == board[row][col] == board[next_row][col] == piece:
    #         return f"Player {piece} is the winner"

    # if location in diagonal_asc and \
    #     board[prev_row][prev_col] == board[row][col] == board[next_row][next_col] == piece:
    #         return f"Player {piece} is the winner"

    # if location in diagonal_asc and \
    #     board[prev_row][next_col] == board[row][col] == board[next_row][prev_col] == piece:
    #         return f"Player {piece} is the winner"

    if board[0][0] == board[1][1] == board[2][2] == piece or \
       board[0][2] == board[1][1] == board[2][0] == piece or \
       board[0][0] == board[0][1] == board[0][2] == piece or \
       board[1][0] == board[1][1] == board[1][2] == piece or \
       board[2][0] == board[2][1] == board[2][2] == piece or \
       board[0][0] == board[1][0] == board[2][0] == piece or \
       board[0][1] == board[1][1] == board[2][1] == piece or \
       board[0][2] == board[1][2] == board[2][2] == piece:
        return f"Player {piece} is the winner"
    
    if all(not element for row in board for element in row):
        return "The game is a tie"
    return "Next move"