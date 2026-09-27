def clear_screen():
    print("\033c", end = "")

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
            clear_screen()
            print("Invalid selection\n")

def make_move(piece: str, position: int, board: list[list[str]]) -> bool:
    row = (position - 1)  // 3
    col = (position - 1) % 3
    if board[row][col] == " ":
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
        clear_screen()
        draw_board(board)
        print(f"\nPlayer {piece} is the winner")
        return True
    
    if all(element != " " for row in board for element in row):
        print("The game is a tie")
        return False
    return False

def play_game():
    board_positions = [[' ', ' ', ' '], 
                       [' ', ' ', ' '], 
                       [' ', ' ', ' ']]
    
    piece = "O"
    while True:
        clear_screen()
        draw_board(board_positions)
        piece = "X" if piece == "O" else "O"
        print(f"It is {piece}'s turn\n")
        location = get_number_input()
        while not make_move(piece, location, board_positions):
            clear_screen()
            print("The board already has a piece in that location.\n")
            location = get_number_input()
        if find_winner(piece, board_positions):
            break

if __name__ == "__main__":
    play_game()
        