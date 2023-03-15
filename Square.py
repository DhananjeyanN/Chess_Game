class Square():
    def __init__(self):
        self.has_piece = False
        self.piece = None
        self.color = None

    def __str__(self):
        return f"{self.color}"
