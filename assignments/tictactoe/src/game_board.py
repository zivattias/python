def get_board_size() -> int:
    while True:
        size = input('> X/O: Enter your board size (ex: 3 for 3 rows & 3 columns)\n'
                     '>>> ')
        if size.isdigit() is False:
            print('Use positive digits only.')
        else:
            size = int(size)
            if not (3 <= size <= 9):
                print('Enter a board size ranging from 3 to 9 (inclusive).')
            else:
                break
    return size


def initialize_board(size: int) -> list[list]:
    board: list[list[None]] = list()
    for row in range(size):
        board.append([])
        for col in range(size):
            board[row].append(None)
    return board


# For 3*3 - 7 rows, 13 chars
# For 1 row add - 2 rows, 4 chars
# For 1 col add, 0 rows, 4 chars
def pprint_board(board: list[list[str]]) -> str:
    board_str = ""
    len_board = len(board[0])
    print(" ", end="")
    for col in range(len_board):
        print(f"   {col + 1}", end="")
    print()

    # ascii for 'A'
    letter = 65
    for row in range(len_board):
        board_str += f'  {"-" * (len_board * 4 + 1)}\n'
        board_str += f"{chr(letter)} "
        letter += 1
        for col in range(len_board):
            shape = " " if board[row][col] is None else board[row][col]
            board_str += f"| {shape} "
        board_str += "|\n"
    board_str += f'  {"-" * (len_board * 4 + 1)}\n'
    return board_str


def display_current_board(board: list[list[str]]) -> None:
    print(pprint_board(board))
    return