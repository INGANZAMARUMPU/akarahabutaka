class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def __eq__(self, point:"Point") -> bool:
        return self.x == point.x
    
    def __hash__(self) -> int:
        return hash(self.x)


a = Point(2, 4)
b = Point(2, 5)

s = {a, b}
print(s)