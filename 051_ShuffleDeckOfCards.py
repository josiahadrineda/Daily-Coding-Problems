import random

def generate_rand(k):
    return random.randint(1, k)

def shuffle(card_len):
    cards = [i for i in range(1, card_len+1)]
    for i in range(card_len):
        rand_ind = generate_rand(card_len-i)
        cards[-i-1], cards[rand_ind] = cards[rand_ind], cards[-i-1]
    return cards

print(shuffle(52))