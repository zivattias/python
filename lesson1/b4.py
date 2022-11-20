player1 = input("Player 1 turn: ")  # scissors, paper, stone
if player1 != 'paper' and player1 != 'scissors' and player1 != 'stone':
    print("Invalid turn.")
else:
    player2 = input("Player 2 turn: ")
    if player2 != 'paper' and player2 != 'scissors' and player2 != 'stone':
        if player1 == player2:
            print("Tie")
        else:
            # At this point, we're sure both inputs are valid & it's not a tie.
            if player1 == 'paper':
                if player2 == 'scissors':
                    print("Player 2 wins.")
                else:
                    # Player 2 has stone.
                    print("Player 1 wins.")