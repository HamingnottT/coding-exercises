class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]    #used single list to represent 3x3 board
        self.current_winner = None              #score keeping