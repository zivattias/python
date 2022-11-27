from enum import Enum


class Turn(Enum):
    player1 = "p1"
    player2 = "p2"


class Shape(Enum):
    x = "X"
    o = "O"


def toggle_turn(player: str) -> str:
    return Turn.player2.value if player == Turn.player1.value else Turn.player1.value


def toggle_shape(shape: str) -> str:
    return Shape.x.value if shape == Shape.o.value else Shape.o.value


def display_turn_prompt(curr_turn: Enum) -> None:
    player = "Player 1" if curr_turn == "p1" else "Player 2"
    print(f"CURRENT TURN: {player}")
    print("Please enter cell coordinates to make your move (ex. B2)")
    return


def get_user_turn(size: int) -> tuple[int, int]:
    while True:
        move_in_cell = input('>>> ').upper()
        if len(move_in_cell) != 2:
            print('> ERROR: Coordinates should have at least 2 characters.')
            continue
        if not move_in_cell[0].isalpha():
            print('> ERROR: First coordinate character should be a letter.')
            continue
        if not move_in_cell[1].isdigit():
            print("> ERROR: Second coordinate character should be a digit.")
            continue
        if not ("A" <= move_in_cell[0] <= chr(65 + size - 1)):
            print("> ERROR: Letter coordinate out of bounds.")
            continue
        if not ("1" <= move_in_cell[1] <= str(size)):
            print("> ERROR: Digit coordinate out of bounds.")
            continue
        break

    row = ord(move_in_cell[0]) - ord("A")
    col = int(move_in_cell[1]) - 1

    return row, col


def update_board_with_turn(board: list[list[str | None]], row: int, col: int, shape: Enum) -> None:
    board[row][col] = shape
    return