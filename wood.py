from players import Sprit


class Box(Sprit):
    def __init__(self, startx, starty):
        super().__init__('wood.png', startx, starty)