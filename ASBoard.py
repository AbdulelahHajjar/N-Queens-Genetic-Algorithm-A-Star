class ASBoard():
    def __init__(self, board=None):
        self.board = board
        self.gn = 0
        self.hn = 0

    def fn(self):
        return self.gn + self.hn

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.board == other.board
        else:
            return False

    def __lt__(self, other):
        return self.fn() < other.fn()
