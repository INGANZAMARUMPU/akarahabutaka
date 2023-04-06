import copy
from .face import Node, color

class SpeedCube:
    def __init__(self):
        _11:Node = Node(color.RED, None, None, color.WHITE, color.BLUE, None)
        _12:Node = Node(color.RED, None, None, None, color.GREEN, None)
        _13:Node = Node(color.YELLOW, color.RED, None, None, color.GREEN, None)
        _14:Node = Node(color.GREEN, None, None, color.WHITE, None, None)
        _15:Node = Node(color.ORANGE, None, None, None, None, None)
        _16:Node = Node(color.WHITE, color.BLUE, None, None, None, None)
        _17:Node = Node(color.RED, None, None, color.YELLOW, None, color.BLUE)
        _18:Node = Node(color.ORANGE, None, None, None, None, color.GREEN)
        _19:Node = Node(color.WHITE, color.ORANGE, None, None, None, color.BLUE)

        _21:Node = Node(None, None, None, color.ORANGE, color.WHITE, None)
        _22:Node = Node(None, None, None, None, color.WHITE, None)
        _23:Node = Node(None, color.RED, None, None, color.WHITE, None)
        _24:Node = Node(None, color.GREEN, None, None, None, None)
        _25:Node = Node(None, None, None, None, None, None)
        _26:Node = Node(None, color.RED, None, None, None, None)
        _27:Node = Node(None, None, None, color.BLUE, None, color.YELLOW)
        _28:Node = Node(None, None, None, None, None, color.YELLOW)
        _29:Node = Node(None, color.RED, None, None, None, color.YELLOW)

        _31:Node = Node(None, None, color.ORANGE, color.GREEN, color.WHITE)
        _32:Node = Node(None, None, color.ORANGE, None, color.BLUE,None)
        _33:Node = Node(None, color.GREEN, color.RED, None, color.WHITE, None)
        _34:Node = Node(None, None, color.YELLOW, color.ORANGE, None, None)
        _35:Node = Node(None, None, color.BLUE, None, None, None)
        _36:Node = Node(None, color.YELLOW, color.GREEN, None, None, None)
        _37:Node = Node(None, None, color.YELLOW, color.BLUE, None, color.ORANGE)
        _38:Node = Node(None, None, color.RED, None, None, color.BLUE)
        _39:Node = Node(None, color.GREEN, color.YELLOW, None, None, color.ORANGE)

    @property
    def faces(self)->list:
        return [
            self._11.c1+self._12.c1+self._13.c1+self._14.c1+self._15.c1+self._16.c1+self._17.c1+self._18.c1+self._19.c1,
            self._13.c2+self._23.c2+self._33.c2+self._16.c2+self._26.c2+self._36.c2+ self._19.c2+self._29.c2+self._39.c2,
            self._33.c3+self._32.c3+self._31.c3+self._36.c3+self._35.c3+self._34.c3+self._39.c3+self._38.c3+self._37.c3,
            self
            self
            self
        ]
    
    @property
    def is_done(self):
        return self._11.c1==self._12.c1==self._13.c1==self._14.c1==self._15.c1==self._16.c1==self._17.c1==self._18.c1==self._19.c1

    def __str__(self) -> str:
        return "".join(sorted(self.faces))

    def __eq__(self, cube:"SpeedCube") -> bool:
        return str(self) == str(cube)
    
    def __hash__(self) -> int:
        return hash(str(self))

    def right_1(self) -> "SpeedCube":
        new_speed_cube = copy.deepcopy(self)
        return new_speed_cube

    def right_2(self) -> "SpeedCube":
        new_speed_cube = copy.deepcopy(self)
        return new_speed_cube

    def right_3(self) -> "SpeedCube":
        new_speed_cube = copy.deepcopy(self)
        return new_speed_cube

    def left_1(self) -> "SpeedCube":
        new_speed_cube = copy.deepcopy(self)
        return new_speed_cube

    def left_2(self) -> "SpeedCube":
        new_speed_cube = copy.deepcopy(self)
        return new_speed_cube

    def left_3(self) -> "SpeedCube":
        new_speed_cube = copy.deepcopy(self)
        return new_speed_cube

    def up_1(self) -> "SpeedCube":
        new_speed_cube = copy.deepcopy(self)
        return new_speed_cube

    def up_2(self) -> "SpeedCube":
        new_speed_cube = copy.deepcopy(self)
        return new_speed_cube

    def up_3(self) -> "SpeedCube":
        new_speed_cube = copy.deepcopy(self)
        return new_speed_cube

    def down_1(self) -> "SpeedCube":
        new_speed_cube = copy.deepcopy(self)
        return new_speed_cube

    def down_2(self) -> "SpeedCube":
        new_speed_cube = copy.deepcopy(self)
        return new_speed_cube

    def down_3(self) -> "SpeedCube":
        new_speed_cube = copy.deepcopy(self)
        return new_speed_cube