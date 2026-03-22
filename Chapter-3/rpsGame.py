import random, sys

print('ROCK,PAPER,SCISSORS')

# track score
wins = 0 
losses = 0
ties = 0

while True: # Main loop
    print('%s Wins, %s Losses, %s Ties' % (wins,losses,ties))
    while True: # Player loop
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        player_move = input('> ')
        if player_move == 'q':
            sys.exit() # Exit
        if player_move == 'r' or player_move == 'p' or player_move == 's':
            break
        print('type one of r, p, s, or q')

    if player_move == 'r':
        print('ROCK versus..')
    elif player_move == 'p':
        print('PAPER versus..')
    elif player_move == 's':
        print('SCISSORS versus..')

    # Display Computer Choice

    move_number = random.randint(1,3)
    if move_number == 1:
        computer_move = 'r'
        print('ROCK')
    elif move_number == 2:
        computer_move = 'p'
        print('PAPER')
    elif move_number == 3:
        computer_move = 's'
        print('SCISSORS')

    # Display and Record

    if player_move == computer_move:
        print('Tie')
        ties += 1
    elif player_move == 'r' and computer_move == 's':
        print('You win')
        wins += 1
    elif player_move == 'p' and computer_move == 'r':
        print('You win')
        wins += 1
    elif player_move == 's' and computer_move == 'p':
        print('You win')
        wins += 1
    elif player_move == 'r' and computer_move == 'p':
        print('You lose')
        losses += 1
    elif player_move == 'p' and computer_move == 's':
        print('You lose')
        losses += 1
    elif player_move == 's' and computer_move == 'r':
        print('You lose')
        losses += 1
