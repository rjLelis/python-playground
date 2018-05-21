
def game(guess, number):
    '''
    A simple comparition function for the guess game
    '''
    if guess < number:
        return -1 # guessed lower
    elif guess > number:
        return 1 # guessed higher
    else:
        return 0 # guessed correctly
