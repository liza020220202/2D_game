from players import Sprit


class Concrete(Sprit):
    def __init__(self, startx, starty):
        super().__init__('wood.png', startx, starty)