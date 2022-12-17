# One way:

def robot_move(moves: str):
    available_moves = ['U', 'R', 'D', 'L']
    origin = [0, 0]
    for move in moves.upper():
        match move:
            case 'U':
                origin[0] += 1
            case 'D':
                origin[0] -= 1
            case 'R':
                origin[1] += 1
            case 'L':
                origin[1] -= 1
            case _:
                raise TypeError(f'Unknown move detected: {move}, available moves: {available_moves}')
    if origin == [0, 0]:
        return True
    else:
        return False


# Second way:

def robot_move_2(moves: str):
    available_moves = ['U', 'R', 'D', 'L']
    move_mapping = {
        'U': (1, 0),
        'D': (-1, 0),
        'R': (0, 1),
        'L': (0, -1),
    }
    origin = [0, 0]
    for move in moves.upper():
        if move not in available_moves:
            raise TypeError(f'Unknown move detected: {move}, available moves: {available_moves}')
        origin[0] += move_mapping[move][0]
        origin[1] += move_mapping[move][1]
    if origin == [0, 0]:
        return True
    else:
        return False
