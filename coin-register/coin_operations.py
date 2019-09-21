def num_coins(cents):

    ''' 
        num_coins(33) == 5
        33 => 1 quarter, 1 nickel, 3 pennies => 5 coins
    '''

    if cents <= 0:
        return 0
    remaning_coins = cents
    number_of_coins = 0
    for _ in range(cents):
        if remaning_coins >= 50:
            number_of_coins += 1
            remaning_coins -= 50

        elif remaning_coins >= 25:
            number_of_coins += 1
            remaning_coins -= 25

        elif remaning_coins >= 10:
            number_of_coins += 1
            remaning_coins -= 10
        
        elif remaning_coins >= 5:
            number_of_coins += 1
            remaning_coins -= 5
        
        elif remaning_coins >= 1:
            number_of_coins += 1
            remaning_coins -= 1
         

    return number_of_coins
