from Square import Square


class Piece(Square):
    def __init__(self, color = None):
        self.__color = None
        self.__symbol = None
        self.pos = None
        self.color = color

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_symbol(self):
        return self.__symbol

    def set_symbol(self, symbol):
        self.__symbol = symbol

    def __str__(self):
        return self.get_symbol()