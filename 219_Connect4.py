# Implemetation for Player vs. Bot
# For future reference: Implement Player vs. Player
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

from random import randint
from time import sleep


"""ENTITIES"""

class Entity:
    marker = '#'

    def take_turn(self):
        pass

    def place_marker(self, bo, c, marker):
        r = 1
        while r < len(bo.contents) and bo.contents[r][c] == '-':
            r += 1
        bo.contents[r-1][c] = marker

    def remove_marker(self, bo, c):
        r = 0
        while bo.contents[r][c] == '-':
            r += 1
        bo.contents[r][c] = '-'

class Player(Entity):
    def __init__(self, game, marker):
        self.game = game

        self.marker = marker

    def take_turn(self):
        bo = self.game.bo

        valid_input = False
        while not valid_input:
            print('Type in any number between 1 and 8 (column numbers from left to right):')
            c = input()
            try:
                c = int(c)
                if c < 1 or c > 8:
                    print('Invalid column number. Please try again.')
                    sleep(0.5)
                elif bo.column_full(c - 1):
                    print(f'Column {c} is full. Please try again.')
                    sleep(0.5)
                else:
                    sleep(0.5)
                    valid_input = True
            except:
                print('Invalid type for input. Please try again.')
                sleep(0.5)

        print(f'Player chooses column {c}!')

        c -= 1
        self.place_marker(bo, c, self.marker)

class Bot(Entity):
    # Change Bot difficulty here
    def __init__(self, game, marker, enemy_marker, difficulty='brainbig'):
        self.game = game

        # We need to keep track of both markers for simulating the game (minimax)
        self.marker = marker
        self.enemy_marker = enemy_marker
        self.name = self.generate_name()
        self.difficulty = difficulty

    def generate_name(self):
        names = [
            'Rowland Cotton',
            'Iram Earle',
            'Jerrit Charlton',
            'Laramie Hamet',
            'Allon Smith',
            'Jahn Twynam',
            'Alkwin Kelsey',
            'Heriberto Sweete',
            'Edwardson Rudges',
            'Lindon Eastoft'
        ]

        n = len(names)
        rand_ind = randint(0, n - 1)
        return names[rand_ind]

    def choose_random(self):
        bo = self.game.bo
        c = randint(0, bo.n - 1)
        while bo.column_full(c):
            c = randint(0, bo.n - 1)

        print(f'Bot {self.name} chooses column {c + 1}!')
        self.place_marker(bo, c, self.marker)

    def choose_minimax(self):
        bo = self.game.bo

        # Change foresight (number of moves Bot can "see" ahead) here
        def minimax(game, foresight=3, alpha=float('-inf'), beta=float('inf'), is_max=True):
            state = game.is_winner()
            if state == 'P1':
                return (None, -100)
            elif state == 'P2':
                return (None, 100)
            elif state == 'T':
                return (None, 0)
            elif foresight == 0:
                return (None, eval_pos(self.marker, self.enemy_marker))

            if is_max:
                move, max_res = -1, float('-inf')
                for c in range(0, bo.n - 1):
                    if not bo.column_full(c):
                        self.place_marker(bo, c, self.marker)
                        _, res = minimax(game, foresight - 1, alpha, beta, False)
                        if res > max_res:
                            move, max_res = c, res
                        self.remove_marker(bo, c)

                        alpha = max(alpha, res)
                        if beta <= alpha:
                            break
                return move, max_res
            else:
                move, min_res = -1, float('inf')
                for c in range(0, bo.n - 1):
                    if not bo.column_full(c):
                        self.place_marker(bo, c, self.enemy_marker)
                        _, res = minimax(game, foresight, alpha, beta, True)
                        if res < min_res:
                            move, min_res = c, res
                        self.remove_marker(bo, c)

                        beta = min(beta, res)
                        if beta <= alpha:
                            break
                return move, min_res

        # Base stats derived from Keith Galli
        def eval_pos(marker, enemy_marker):
            m, n = len(bo.contents), len(bo.contents[0])

            def eval_window(window, marker, enemy_marker):
                res = 0

                if window.count(marker) == 3 and window.count('-') == 1:
                    res += 5
                elif window.count(marker) == 2 and window.count('-') == 2:
                    res += 2
                elif window.count(marker) == 1 and window.count('-') == 3:
                    res += 1
                
                if window.count(enemy_marker) == 3 and window.count('-') == 1:
                    res -= 5
                elif window.count(enemy_marker) == 2 and window.count('-') == 2:
                    res -= 2

                return res

            res = 0

            # Prioritize center col
            center_l, center_r = n // 2, n // 2 - 1
            center_l_col, center_r_col = [r[center_l] for r in bo.contents], [r[center_r] for r in bo.contents]
            center_cnt = max(center_l_col.count(marker), center_r_col.count(marker))
            res += center_cnt * 3

            # Eval upper diags
            for r in range(3, m):
                for c in range(n - 3):
                    window = [bo.contents[r][c], bo.contents[r - 1][c + 1], bo.contents[r - 2][c + 2], bo.contents[r - 3][c + 3]]
                    res += eval_window(window, marker, enemy_marker)

            # Eval lower diags
            for r in range(m - 3):
                for c in range(n - 3):
                    window = [bo.contents[r][c], bo.contents[r + 1][c + 1], bo.contents[r + 2][c + 2], bo.contents[r + 3][c + 3]]
                    res += eval_window(window, marker, enemy_marker)

            # Eval rows
            for r in range(m):
                for c in range(n - 3):
                    window = [bo.contents[r][c], bo.contents[r][c + 1], bo.contents[r][c + 2], bo.contents[r][c + 3]]
                    res += eval_window(window, marker, enemy_marker)

            # Eval cols
            for r in range(m - 3):
                for c in range(n):
                    window = [bo.contents[r][c], bo.contents[r + 1][c], bo.contents[r + 2][c], bo.contents[r + 3][c]]
                    res += eval_window(window, marker, enemy_marker)

            return res

        c, _ = minimax(self.game)

        print(f'Bot {self.name} chooses column {c + 1}!')
        self.place_marker(bo, c, self.marker)

    def take_turn(self):
        print(f'Bot {self.name} is choosing...')

        sleep(1.0)

        if self.difficulty == 'braindead':
            self.choose_random()
        elif self.difficulty == 'brainbig':
            self.choose_minimax()


"""GAME MECHANICS"""

class Board:
    def __init__(self, n):
        self.n = n
        self.contents = self.create_board(self.n)

    def create_board(self, n):
        assert n >= 4, 'You cannot win a game of Connect 4 with less than 4 rows!'
        return [['-'] * n for _ in range(n)]

    def print_board(self):
        line = '-' + '--' * self.n
        print(line)
        for r in self.contents:
            row_contents = '|'.join(r)
            print('|' + row_contents + '|')
        print(line)

    def column_full(self, c):
        return self.contents[0][c] != '-'

class Game:
    # Change board size and player markers here
    def __init__(self, n=8, p1_marker='@', p2_marker='0'):
        self.bo = Board(n)
        
        self.player = Player(self, p1_marker)
        self.bot = Bot(self, p2_marker, p1_marker)

        self.win_or_tie_msg = {
            "P1": "Congratulations! You have won!",
            "P2": f"Unfortunately, you have lost to Bot {self.bot.name}...",
            "T": "OOF! Close call, but no winner!"
        }

    def is_winner(self):
        def check_winner(marker, contents):
            m, n = len(contents), len(contents[0])

            def upper_diag(r, c, marker, contents):
                if r - 3 >= 0 and c + 3 < n:
                    return contents[r - 1][c + 1] == marker and \
                        contents[r - 2][c + 2] == marker and \
                        contents[r - 3][c + 3] == marker
                return False
            def lower_diag(r, c, marker, contents):
                if r + 3 < m and c + 3 < n:
                    return contents[r + 1][c + 1] == marker and \
                        contents[r + 2][c + 2] == marker and \
                        contents[r + 3][c + 3] == marker
                return False
            def horiz(r, c, marker, contents):
                if c + 3 < n:
                    return contents[r][c + 1] == marker and \
                        contents[r][c + 2] == marker and \
                        contents[r][c + 3] == marker
                return False
            def vert(r, c, marker, contents):
                if r + 3 < m:
                    return contents[r + 1][c] == marker and \
                        contents[r + 2][c] == marker and \
                        contents[r + 3][c] == marker
                return False

            for r in range(m):
                for c in range(n):
                    if contents[r][c] == marker:
                        if upper_diag(r, c, marker, contents):
                            return True
                        elif lower_diag(r, c, marker, contents):
                            return True
                        elif horiz(r, c, marker, contents):
                            return True
                        elif vert(r, c, marker, contents):
                            return True
            return False

        def check_tie(contents):
            return all([all([cell != '-' for cell in row]) for row in contents])

        if check_winner(self.player.marker, self.bo.contents):
            return 'P1'
        elif check_winner(self.bot.marker, self.bo.contents):
            return 'P2'
        elif check_tie(self.bo.contents):
            return 'T'
        return ''

    def play(self):
        self.bo.print_board()

        while True:
            self.player.take_turn()
            self.bo.print_board()
            win_or_tie = self.is_winner()
            if win_or_tie:
                print(self.win_or_tie_msg[win_or_tie])
                return

            sleep(0.5)

            self.bot.take_turn()
            self.bo.print_board()
            win_or_tie = self.is_winner()
            if win_or_tie:
                print(self.win_or_tie_msg[win_or_tie])
                return

            sleep(0.5)


if __name__ == "__main__":
    game = Game()
    game.play()