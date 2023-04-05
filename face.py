
from enum import Enum

class color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "BLUE"
    ORANGE = "ORANGE"
    YELLOW = "YELLOW"
    WHITE = "WHITE"

class Node:
    def __init__(self, c_1, c_2, c_3, c_4, c_5, c_6):
        self.c_1 = c_1
        self.c_2 = c_2
        self.c_3 = c_3
        self.c_4 = c_4
        self.c_5 = c_5
        self.c_6 = c_6
    
    def a_gauche(self):
        pass

    def a_droite(self):
        pass

    def devant(self):
        pass

    def derriere(self):
        pass