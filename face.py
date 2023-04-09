
from enum import Enum

class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"
    ORANGE = "orange"
    YELLOW = "yellow"
    WHITE = "white"

    def __lt__(self, other):
        return self.value < other.value

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
        self.c1, self.c6, self.c3, self.c5, self.c2, self.c4

    def __str__(self):
        null = " "*6

        c1 = self.c1.value if self.c1 else "xxxxxx"
        c2 = self.c2.value if self.c2 else "xxxxxx"
        c3 = self.c3.value if self.c3 else "xxxxxx"
        c4 = self.c4.value if self.c4 else "xxxxxx"
        c5 = self.c5.value if self.c5 else "xxxxxx"
        c6 = self.c6.value if self.c6 else "xxxxxx"

        return f"{null} {c5:6} {null*2}\n{c4:6} {c1:6} {c2:6} {c3:6}\n{null} {c6:6}"
