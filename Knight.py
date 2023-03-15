from Piece import Piece


class Knight(Piece):
    def __init__(self, color):
        super().__init__()
        self.color = color
        if self.color == "white":
            self.set_symbol("♞")
        else:
            self.set_symbol("♘")

    def is_legit_move(self, current, target):
        x1, y1 = current
        x2, y2 = target
        difference_x = abs(x1 - x2)
        difference_y = abs(y1 - y2)
        if (difference_x == 2 and difference_y == 1) or (difference_x == 1 and difference_y == 2):
            return True
        else:
            return False

    def move(self, target):
        self.pos = target