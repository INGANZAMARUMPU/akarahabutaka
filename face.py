
from enum import Enum

class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"
    ORANGE = "orange"
    YELLOW = "yellow"
    WHITE = "white"

class Node:
    def __init__(self, c1:Color, c2:Color, c3:Color, c4:Color, c5:Color, c6:Color):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.c4 = c4
        self.c5 = c5
        self.c6 = c6
    
    def move_1to4(self):
        self.c1, self.c2, self.c3, self.c4, self.c5, self.c6 =\
        self.c4, self.c1, self.c2, self.c3, self.c5, self.c6

    def move_1to6(self):
        self.c1, self.c2, self.c3, self.c4, self.c5, self.c6 =\
        self.c6, self.c2, self.c5, self.c4, self.c1, self.c3

    def move_4to6(self):
        self.c1, self.c2, self.c3, self.c4, self.c5, self.c6 =\
        self.c1, self.c5, self.c3, self.c4, self.c6, self.c2
