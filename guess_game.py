
def game(guess, number):
    if guess < number:
        return -1 # guessed lower
    elif guess > number:
        return 1 # guessed higher
    else:
        return 0 # guessed correctly
