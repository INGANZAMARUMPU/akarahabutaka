
from enum import Enum

class color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"
    ORANGE = "orange"
    YELLOW = "yellow"
    WHITE = "white"

class Node:
    def __init__(self, c_1:color, c_2:color, c_3:color, c_4:color, c_5:color, c_6:color):
        self.c_1 = c_1
        self.c_2 = c_2
        self.c_3 = c_3
        self.c_4 = c_4
        self.c_5 = c_5
        self.c_6 = c_6
    
    def a_gauche(self):
        self.c_1, self.c_2, self.c_3, self.c_4, self.c_5, self.c_6 = self.c_4, self.c_1, self.c_2, self.c_3, self.c_5, self.c_6

    def a_droite(self):
        self.c_1, self.c_2, self.c_3, self.c_4, self.c_5, self.c_6 = self.c_2, self.c_3, self.c_4, self.c_1, self.c_5, self.c_6

    def en_haut(self):
        self.c_1, self.c_2, self.c_3, self.c_4, self.c_5, self.c_6 = self.c_6, self.c_2, self.c_5, self.c_4, self.c_1, self.c_3

    def en_bas(self):
        self.c_1, self.c_2, self.c_3, self.c_4, self.c_5, self.c_6 = self.c_5, self.c_2, self.c_6, self.c_4, self.c_3, self.c_1
