BOARD_POSITIONS = [['', '', ''], 
                   ['', '', ''], 
                   ['', '', '']]


def draw_board(board: list[list[str]]) -> None:
    pass

def make_move(piece: str, board: list[list[str]]) -> None:
    pass

def find_winner(piece: str, board: list[list[str]]) -> str:
    # Determine if a winning move occurred in a diagonal
    if board[0][0] == board[1][1] == board[2][2] == piece or \
       board[0][2] == board[1][1] == board[2][0] == piece or \
       board[0][0] == board[0][1] == board[0][2] == piece or \
       board[1][0] == board[1][1] == board[1][2] == piece or \
       board[2][0] == board[2][1] == board[2][2] == piece or \
       board[0][0] == board[1][0] == board[2][0] == piece or \
       board[0][1] == board[1][1] == board[2][1] == piece or \
       board[0][2] == board[1][2] == board[2][2] == piece:
        return f"Player {piece} is the winner"
    elif all(not element for row in board for col in row):
        return