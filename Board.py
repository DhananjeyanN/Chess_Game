from Bishop import Bishop
from King import King
from Knight import Knight
from Queen import Queen
from Square import Square
from Pawn import Pawn
from Rook import Rook

class Board():
    def __init__(self):
        self.board = []
        for i in range(1,9):
            row = []
            for j in range(1,9):
                if j% 2 == 0 and i%2 != 0:
                    square = Square()
                    square.color = "B"
                    row.append(square)
                elif j% 2 != 0 and i%2 == 0:
                    square = Square()
                    square.color = "B"
                    row.append(square)
                else:
                    square = Square()
                    square.color = "W"
                    row.append(square)
            self.board.append(row)

    def initial_pos(self):
        for i in range(8):
            for j in range(8):
                if i == 0 and (j == 0 or j == 7):
                    rook = Rook("black")
                    self.board[i][j] = rook
                elif i == 7 and (j == 0 or j == 7):
                    rook = Rook("white")
                    self.board[i][j] = rook
                elif i == 0 and (j == 1 or j == 6):
                    knight = Knight("black")
                    self.board[i][j] = knight
                elif i == 7 and (j == 1 or j == 6):
                    knight = Knight("white")
                    self.board[i][j] = knight
                elif i == 0 and (j == 2 or j == 5):
                    bishop = Bishop("black")
                    self.board[i][j] = bishop
                elif i == 7 and (j == 2 or j == 5):
                    bishop = Bishop("white")
                    self.board[i][j] = bishop
                elif i == 0 and j == 3:
                    king = King("black")
                    self.board[i][j] = king
                elif i == 7 and j == 4:
                    king = King("white")
                    self.board[i][j] = king
                elif i == 0 and j == 4:
                    queen = Queen("black")
                    self.board[i][j] = queen
                elif i == 7 and j == 3:
                    queen = Queen("white")
                    self.board[i][j] = queen
                elif i == 1:
                    pawn = Pawn("black")
                    self.board[i][j] = pawn
                elif i == 6:
                    pawn = Pawn("white")
                    self.board[i][j] = pawn











