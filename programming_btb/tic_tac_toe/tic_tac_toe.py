BOARD_POSITIONS = [['', '', ''], 
                   ['', '', ''], 
                   ['', '', '']]


def draw_board(board: list[list[str]]) -> None:
    pass

def make_move(piece: str, location: int, board: list[list[str]]) -> None:
    row = location // 3
    col = location % 3
    if not board[row][col]:
        board[row][col] = piece

def find_winner(piece: str, location: int, board: list[list[str]]) -> str:
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
    if all(not element for row in board for element in row):
        return "The game is a tie"
    return "Next move"