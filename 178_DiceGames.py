from random import randint

def roll_dice():
    return randint(1, 6)

def entry(a, b):
    dues = 0
    prev, curr = None, None
    while prev != a or curr != b:
        dues += 1
        if not curr:
            curr = roll_dice()
        else:
            prev, curr = curr, roll_dice()
    return dues

def five_six_prob(experiments=100000):
    tot = 0
    for _ in range(experiments):
        tot += entry(5, 6)
    return tot / experiments

def five_five_prob(experiments=100000):
    tot = 0
    for _ in range(experiments):
        tot += entry(5, 5)
    return tot / experiments

# Which game should Alice play?
def choose_game():
    fs = five_six_prob()
    ff = five_five_prob()

    print(f'Average dues of the Five-Six Game: {fs}')
    print(f'Average dues of the Five-Five Game: {ff}')

    if fs < ff:
        game = 'Six'
    else:
        game = 'Five'

    print(f'Since {min(fs, ff)} is less than {max(fs, ff)}, Alice should play the Five-{game} Game.')

choose_game()

# The result of choose_game() is surprisingly the Five-Six Game.
# I would have expected the average dues for both games to be around the same value.