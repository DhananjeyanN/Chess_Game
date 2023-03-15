from Piece import Piece


class Pawn(Piece):
    def __init__(self, color):
        super().__init__()
        self.color = color
        if self.color == "white":
            self.set_symbol("♟")
            self.move = 1
        else:
            self.set_symbol("♙")
            self.move = 0

    def is_legit_move(self, current, target):
        x1, y1 = current[1], current[0]
        x2, y2 = target[1], target[0]
        print(x1,y1,x2,y2)
        difference_x = abs(x1 - x2)
        difference_y = abs(y1 - y2)
        if self.color == "white" and difference_x == 0 and (difference_y == 2 or difference_y == 1) and self.move == 1:
            return True
        elif self.color == "black" and difference_x == 0 and (difference_y == -2 or difference_y == -1) and self.move == 0:
            return True
        elif self.color == "white" and difference_x == 0 and difference_y == 1 and self.move > 1:
            return True
        elif self.color == "black" and difference_x == 0 and difference_y == -1 and self.move > 0:
            return True
        else:
            return False

    def move(self, target):
        self.pos = target




