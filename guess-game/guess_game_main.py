from random import randint
from guess_game import game


def main():
    guess = None
    guessed_times = 0
    number = randint(0, 10)
    not_finished = True
    while not_finished:
        try:
            guess = int(input('Guess the number between 0 and 10: '))
            returned = game(guess, number)
            if returned > 0:
                print('Guessed higher')
                guessed_times += 1
            elif returned < 0:
                print('Guessed lower')
                guessed_times += 1
            else:
                not_finished = False
        except ValueError:
            print(f"Your guess should be a number!")

    print(f'End of the game, the number was {number} and you guessed\
{guessed_times} times!')

if __name__ == '__main__':
    main()
