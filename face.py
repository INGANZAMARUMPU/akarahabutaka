
from enum import Enum

class color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"
    ORANGE = "orange"
    YELLOW = "yellow"
    WHITE = "white"

class Node:
    def __init__(self, c1:color, c2:color, c3:color, c4:color, c5:color, c6:color):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.c4 = c4
        self.c5 = c5
        self.c6 = c6
    
    def move_1to4(self):
        self.c1, self.c2, self.c3, self.c4, self.c5, self.c6 = self.c4, self.c1, self.c2, self.c3, self.c5, self.c6

    def move_4to1(self):
        self.c1, self.c2, self.c3, self.c4, self.c5, self.c6 = self.c2, self.c3, self.c4, self.c1, self.c5, self.c6

    def move_1to6(self):
        self.c1, self.c2, self.c3, self.c4, self.c5, self.c6 = self.c6, self.c2, self.c5, self.c4, self.c1, self.c3

    def move_6to1(self):
        self.c1, self.c2, self.c3, self.c4, self.c5, self.c6 = self.c5, self.c2, self.c6, self.c4, self.c3, self.c1

    def move_6to4(self):
        self.c1, self.c2, self.c3, self.c4, self.c5, self.c6 = self.c1, self.c6, self.c3, self.c5, self.c2, self.c4

    def move_4to6(self):
        self.c1, self.c2, self.c3, self.c4, self.c5, self.c6 = self.c1, self.c5, self.c3, self.c4, self.c6, self.c2
