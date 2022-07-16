'''
Each round at this Lotto game costs 3ILS, insert how much money do you have.
The player's numbers will contain 6 different numbers.
If you guess (per round): 6 numbers= won 1M ILS , 5 numbers=5k ILS , 4 numbers=100 ILS,
3 numbers=10 ILS
'''

from time import sleep
from random import randint
from copy import deepcopy


def lottery(money,player_numbers):

    if money<3:
        return 'No enough money even for a single round'
    else:
        rounds = money // 3
        print(f'You have enough money for {rounds} rounds\n')
        print("The player's numbers: ", player_numbers, '\n')

    money_earn = 0
    while rounds>=1:
        temp = deepcopy(player_numbers)            # will do some changes at player_numbers
        lotted_numbers = [randint(1,37) for _ in range(6)]
        lotted_numbers.sort()
        print(f'The lotted 6 numbers (1 to 37): {lotted_numbers}')
        guesses = 0
        for i in lotted_numbers:
            if i in temp:
                print(i)
                guesses+=1
                temp.remove(i)
                continue
        print(f'The number of guesses at this round: {guesses}')
        if guesses==6:
            print('You won 1M ILS')
            money_earn+=1000000
        elif guesses==5:
            print('You won 5K ILS')
            money_earn += 5000
        elif guesses==4:
            print('You won 100 ILS')
            money_earn += 100
        elif guesses==3:
            print('You won 10 ILS')
            money_earn += 10
        else:
            print('No money for this round')
        print()
        #sleep(3)
        rounds -= 1

    return f'Game over, Total money you earned: {money_earn} '

money=int(input('Each round costs 3 ILS, how much do you have? '))
player_numbers=[10,20,30,1,17,26]               # It's optional to take input from the player
player_numbers.sort()
print( lottery(money,player_numbers) )

sleep(5)

