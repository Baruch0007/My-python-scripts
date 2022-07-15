def R_P_S(player1, player2):
    winner_score = 3
    player1_score = 0
    player2_score = 0

    while True:
        choice1 = input(f'{name1} choose R,P,S for next round\n').upper()
        print('\n' * 100)
        choice2 = input(f'{name2} choose R,P,S for next round\n').upper()
        print('\n' * 100)
        while choice1 not in 'RPS' or choice2 not in 'RPS':
            print('Invalid input, try again\n\n\n')
            choice1 = input(f'{name1} choose R,P,S:\n')
            print('\n' * 100)
            choice2 = input(f'{name2} choose R,P,S:\n')
            print('\n' * 100)

        if choice1 == 'R' and choice2 == 'P':
            player2_score += 1
        elif choice1 == 'P' and choice2 == 'R':
            player1_score += 1


        elif choice1 == 'R' and choice2 == 'S':
            player1_score += 1
        elif choice1 == 'S' and choice2 == 'R':
            player2_score += 1


        elif choice1 == 'P' and choice2 == 'S':
            player2_score += 1
        elif choice1 == 'S' and choice2 == 'P':
            player1_score += 1


        elif choice1 == 'R' and choice2 == 'R':
            print('You both choosed the same mark')

        print(
            f'{player1}:{choice1}    {player2}:{choice2}.  The current result is {player1_score} : {player2_score}\n\n')
        if player1_score == winner_score or player2_score == winner_score:
            return f'The winner is {name1 if player1_score > player2_score else name2}'

import time

name1 = 'Avi'  # input('Enter the first player name:\n')
name2 = 'Izik'  # input('Enter the second player name:\n')

print(R_P_S(name1, name2))
time.sleep(3)
