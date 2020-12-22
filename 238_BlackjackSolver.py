import random

class Card:
    def __init__(self, name):
        self.name = name
        if self.name.isnumeric():
            self.val = int(name)
        elif self.name == 'Ace':
            self.val = 1
        else:
            self.val = 10

class Deck:
    def __init__(self):
        self.deck = []
        for i in range(2, 11):
            self.deck.extend([Card(str(i)) for _ in range(4)])
        self.deck.extend([Card('Ace') for _ in range(4)])
        self.deck.extend([Card('Jack') for _ in range(4)])
        self.deck.extend([Card('Queen') for _ in range(4)])
        self.deck.extend([Card('King') for _ in range(4)])

    def peek(self):
        if not self.is_empty():
            return self.deck[-1]

    def draw(self):
        if not self.is_empty():
            return self.deck.pop(0)

    def _reverse(self, card):
        self.deck.insert(0, card)

    def shuffle(self):
        random.shuffle(self.deck)

    def is_empty(self):
        return not self.deck

# This reduces the number of games for some reason, so it technically doesn't work.
# But I don't really feel like working on this anymore tbh...
def blackjack(deck):
    """Given full knowledge of the sequence of cards in DECK beforehand, maximizes
    the player's score (wins - losses) in the game Blackjack.
    """

    def play(scores=[0, 0], player_turn=True, player_fold=False, dealer_fold=False):
        if not scores[0] and not scores[1]:
            for _ in range(2):
                if deck.is_empty(): return 0
                c = deck.draw()
                scores[0] += c.val
            for _ in range(2):
                if deck.is_empty(): return 0
                c = deck.draw()
                scores[1] += c.val
            return play(scores, True, False, False)
        elif scores[1] > 21:
            return 1 + play([0, 0], True, False, False)
        elif scores[0] > 21:
            return -1 + play([0, 0], True, False, False)
        elif dealer_fold and scores[0] > scores[1]:
            return 1 + play([0, 0], True, False, False)
        elif player_fold and scores[1] > scores[0]:
            return -1 + play([0, 0], True, False, False)
        elif player_fold and dealer_fold and scores[0] == scores[1]:
            return play([0, 0], True, False, False)
        elif deck.is_empty():
            return 0
        else:
            if player_turn and not player_fold:
                c = deck.draw()
                win_loss_draw = play([scores[0] + c.val, scores[1]], False, False, False)
                deck._reverse(c)
                win_loss_fold = play(scores, False, True, False)
                print(win_loss_draw, win_loss_fold)
                return max(win_loss_draw, win_loss_fold)
            else:
                if scores[1] > 16:
                    return play(scores, True, player_fold, True)
                else:
                    c = deck.draw()
                    return play([scores[0], scores[1] + c.val], True, player_fold, False)

    return play()