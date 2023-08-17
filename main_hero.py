from players import Sprit


class Hero(Sprit):
    def __init__(self, startx, starty):
        super().__init__('hero1.png', startx, starty)