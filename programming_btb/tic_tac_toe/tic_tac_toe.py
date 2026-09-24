def draw_board(board: list[list[str]]) -> None:
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]} ")
    print("---|---|---")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]} ")
    print("---|---|---")
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]} ")
    print("\n")

def get_number_input() -> int:
    while True:
        board_options = [['1', '2', '3'], 
                         ['4', '5', '6'], 
                         ['7', '8', '9']]
        draw_board(board_options)
        selection = input("Please enter a position (1-9): ")
        if selection.isdigit() and 0 < int(selection) < 10:
            return int(selection)
        else:
            print("\033c", end = "")
            print("Invalid selection\n")

def make_move(piece: str, board: list[list[str]]) -> None:
    while True:    
        position = get_number_input() 
        row = position // 3
        col = position % 3
        if board[row][col] == " ":
            board[row][col] = piece
            break

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
    
    if all(element != " " for row in board for element in row):
        print("The game is a tie")
        return False
    return False

def play_game():
    board_positions = [[' ', ' ', ' '], 
                       [' ', ' ', ' '], 
                       [' ', ' ', ' ']]

    while True:
        print("\033c", end = "")
        piece = "O" if "X" else "X"
        print(f"It is {piece}'s turn")
        location = get_number_input()

