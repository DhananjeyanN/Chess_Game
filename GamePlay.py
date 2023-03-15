from Board import Board
from Bishop import Bishop
from King import King
from Knight import Knight
from Pawn import Pawn
from Queen import Queen
from Rook import Rook


class GamePlay():
    def __init__(self):
        self.player1 = input("Enter Player 1: ")
        self.player2 = input("Enter Player 2: ")
        self.board_obj = Board()
        self.board = self.board_obj.board
        self.board_obj.initial_pos()

    def game_loop(self):
        choice = True
        turn = "white"
        while choice == True:
            for row in self.board:
                for i in row:
                    print(i, end="\t")
                print()
            piece = input(f"{self.player1} Pick Your Piece: ")
            px, py = piece.split(",")
            pieceo = self.board[int(px)][int(py)]
            print(pieceo)
            move = input(f"Enter where you would like to move")
            mx, my = move.split(",")
            piece = (int(px), int(py))
            move = (int(mx), int(my))
            if pieceo.is_legit_move(piece, move) and self.in_path(piece, move):
                self.board.board[int(mx)][int(my)] = pieceo
            else:
                print("False move")
                continue
            if turn == "white":
                turn = "black"
            elif turn == "black":
                turn = "white"

    def in_path(self, current, target):
        x1, y1 = current
        x2, y2 = target
        for i in range(x1, x2):
            for j in range(y1, y2):
                if j[0].has_piece == False:
                    continue
                else:
                    return False
        return True
