import math
import random

class Player:
    def __init__(self, letter):
        # letter
        self.letter = letter

    # want all players to get their next move given a game
    def get_move(self, game):
        pass

class RandomCPUPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        pass

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        pass
    


def tictactoe():
    pass

def main():
    pass

if __name__ == '__main__':
    main()