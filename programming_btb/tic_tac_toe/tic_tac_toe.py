def draw_board(board: list[list[str]]) -> None:
    print("\033c", end = "")

    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]} ")
    print("---|---|---")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]} ")
    print("---|---|---")
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]} ")

def make_move(piece: str, location: int, board: list[list[str]]) -> bool:
    row = location // 3
    col = location % 3
    if not board[row][col]:
        board[row][col] = piece
        return True

    return False

def find_winner(piece: str, board: list[list[str]]) -> bool:
    if board[0][0] == board[1][1] == board[2][2] == piece or \
       board[0][2] == board[1][1] == board[2][0] == piece or \
       board[0][0] == board[0][1] == board[0][2] == piece or \
       board[1][0] == board[1][1] == board[1][2] == piece or \
       board[2][0] == board[2][1] == board[2][2] == piece or \
       board[0][0] == board[1][0] == board[2][0] == piece or \
       board[0][1] == board[1][1] == board[2][1] == piece or \
       board[0][2] == board[1][2] == board[2][2] == piece:
        print(f"Player {piece} is the winner")
        return True
    
    if all(not element for row in board for element in row):
        print("The game is a tie")
        return False
    print(f"It is {piece}'s turn")
    return False

def game():
    board_positions = [[' ', ' ', ' '], 
                       [' ', ' ', ' '], 
                       [' ', ' ', ' ']]

    piece = "X"
    while True:
        
