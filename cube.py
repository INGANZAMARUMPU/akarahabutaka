import copy
from .face import Node, color

class SpeedCube:
    def __init__(self):
        self._11:Node = Node(color.RED, None, None, color.BLUE, color.YELLOW, None)
        self._12:Node = Node(color.RED, None, None, color.YELLOW, None)
        self._13:Node = Node(color.RED, color.GREEN, None, color.YELLOW, None)
        self._14:Node = Node(color.RED, None, None, color.BLUE, None, None)
        self._15:Node = Node(color.RED, None, None, None, None)
        self._16:Node = Node(color.RED, color.GREEN, None, None, None)
        self._17:Node = Node(color.RED, None, None, color.BLUE, None, color.WHITE)
        self._18:Node = Node(color.RED, None, None, None, color.WHITE)
        self._19:Node = Node(color.RED, color.GREEN, None, None, color.WHITE)

        self._21:Node = Node( None, None, None, None, color.BLUE, color.YELLOW, None)
        self._22:Node = Node( None, None, None, None, color.YELLOW, None)
        self._23:Node = Node( None, color.GREEN, None, None, color.YELLOW, None)
        self._24:Node = Node( None, None, None, None, color.BLUE, None, None)
        self._25:Node = Node( None, None, None, None, None, None)
        self._26:Node = Node( None, color.GREEN, None, None, None, None)
        self._27:Node = Node( None, None, None, None, color.BLUE, None, color.WHITE)
        self._28:Node = Node( None, None, None, None, None, color.WHITE)
        self._29:Node = Node( None, color.GREEN, None, None, None, color.WHITE)

        self._31:Node = Node(None, None, color.ORANGE, color.BLUE, color.YELLOW, None)
        self._32:Node = Node(None, None, color.ORANGE, None, color.YELLOW, None)
        self._33:Node = Node(None, color.GREEN, color.ORANGE, None, color.YELLOW, None)
        self._34:Node = Node(None, None, color.ORANGE, color.BLUE, None, None)
        self._35:Node = Node(None, None, color.ORANGE, None, None, None)
        self._36:Node = Node(None, color.GREEN, color.ORANGE, None, None, None)
        self._37:Node = Node(None, None, color.ORANGE, color.BLUE, None, color.WHITE)
        self._38:Node = Node(None, None, color.ORANGE, None, None, color.WHITE)
        self._39:Node = Node(None, color.GREEN, color.ORANGE, None, None, color.WHITE)

    @property
    def faces(self)->list:
        return [
            self._11.c1+self._12.c1+self._13.c1+self._14.c1+self._15.c1+self._16.c1+self._17.c1+self._18.c1+self._19.c1,
            self._13.c2+self._16.c2+self._19.c2+self._23.c2+self._26.c2+self._29.c2+self._33.c2+self._36.c2+self._39.c2,
            self._31.c3+self._32.c3+self._33.c3+self._34.c3+self._35.c3+self._36.c3+self._37.c3+self._38.c3+self._39.c3,
            self._11.c4+self._14.c4+self._17.c4+self._21.c4+self._24.c4+self._27.c4+self._31.c4+self._34.c4+self._37.c4,
            self._11.c5+self._12.c5+self._13.c5+self._21.c5+self._22.c5+self._23.c5+self._31.c5+self._32.c5+self._33.c5,
            self._17.c6+self._18.c6+self._19.c6+self._27.c6+self._28.c6+self._29.c6+self._37.c6+self._38.c6+self._39.c6,
        ]
    
    @property
    def is_done(self):
        return (
            self._11.c1==self._12.c1==self._13.c1==self._14.c1==self._15.c1==self._16.c1==self._17.c1==self._18.c1==self._19.c1 and
            self._13.c2==self._16.c2==self._19.c2==self._23.c2==self._26.c2==self._29.c2==self._33.c2==self._36.c2==self._39.c2 and
            self._31.c3==self._32.c3==self._33.c3==self._34.c3==self._35.c3==self._36.c3==self._37.c3==self._38.c3==self._39.c3 and
            self._11.c4==self._14.c4==self._17.c4==self._21.c4==self._24.c4==self._27.c4==self._31.c4==self._34.c4==self._37.c4 and
            self._11.c5==self._12.c5==self._13.c5==self._21.c5==self._22.c5==self._23.c5==self._31.c5==self._32.c5==self._33.c5 and
            self._17.c6==self._18.c6==self._19.c6==self._27.c6==self._28.c6==self._29.c6==self._37.c6==self._38.c6==self._39.c6
        )

    def __str__(self) -> str:
        return "".join(sorted(self.faces))

    def __eq__(self, cube:"SpeedCube") -> bool:
        return str(self) == str(cube)
    
    def __hash__(self) -> int:
        return hash(str(self))

    def move_4to1_1(self) -> "SpeedCube":
        new_s_c:SpeedCube = copy.deepcopy(self)

        new_s_c._11.move_4to1()
        new_s_c._12.move_4to1()
        new_s_c._13.move_4to1()

        new_s_c._21.move_4to1()
        new_s_c._22.move_4to1()
        new_s_c._23.move_4to1()
        
        new_s_c._31.move_4to1()
        new_s_c._32.move_4to1()
        new_s_c._33.move_4to1()

        return new_s_c

    def move_4to1_2(self) -> "SpeedCube":
        new_s_c = copy.deepcopy(self)

        new_s_c._14.move_4to1()
        new_s_c._15.move_4to1()
        new_s_c._16.move_4to1()

        new_s_c._24.move_4to1()
        new_s_c._25.move_4to1()
        new_s_c._26.move_4to1()
        
        new_s_c._34.move_4to1()
        new_s_c._35.move_4to1()
        new_s_c._36.move_4to1()

        return new_s_c

    def move_4to1_3(self) -> "SpeedCube":
        new_s_c = copy.deepcopy(self)

        new_s_c._17.move_4to1()
        new_s_c._18.move_4to1()
        new_s_c._19.move_4to1()

        new_s_c._27.move_4to1()
        new_s_c._28.move_4to1()
        new_s_c._29.move_4to1()
        
        new_s_c._37.move_4to1()
        new_s_c._38.move_4to1()
        new_s_c._39.move_4to1()
        
        return new_s_c

    def move_1to4_1(self) -> "SpeedCube":
        new_s_c:SpeedCube = copy.deepcopy(self)

        new_s_c._11.move_1to4()
        new_s_c._12.move_1to4()
        new_s_c._13.move_1to4()

        new_s_c._21.move_1to4()
        new_s_c._22.move_1to4()
        new_s_c._23.move_1to4()
        
        new_s_c._31.move_1to4()
        new_s_c._32.move_1to4()
        new_s_c._33.move_1to4()

        return new_s_c

    def move_1to4_2(self) -> "SpeedCube":
        new_s_c = copy.deepcopy(self)

        new_s_c._14.move_1to4()
        new_s_c._15.move_1to4()
        new_s_c._16.move_1to4()

        new_s_c._24.move_1to4()
        new_s_c._25.move_1to4()
        new_s_c._26.move_1to4()
        
        new_s_c._34.move_1to4()
        new_s_c._35.move_1to4()
        new_s_c._36.move_1to4()

        return new_s_c

    def move_1to4_3(self) -> "SpeedCube":
        new_s_c = copy.deepcopy(self)

        new_s_c._17.move_1to4()
        new_s_c._18.move_1to4()
        new_s_c._19.move_1to4()

        new_s_c._27.move_1to4()
        new_s_c._28.move_1to4()
        new_s_c._29.move_1to4()
        
        new_s_c._37.move_1to4()
        new_s_c._38.move_1to4()
        new_s_c._39.move_1to4()
        
        return new_s_c

    def move_6to1_1(self) -> "SpeedCube":
        new_s_c = copy.deepcopy(self)

        new_s_c._11.move_6to1()
        new_s_c._14.move_6to1()
        new_s_c._17.move_6to1()

        new_s_c._21.move_6to1()
        new_s_c._24.move_6to1()
        new_s_c._27.move_6to1()

        new_s_c._31.move_6to1()
        new_s_c._34.move_6to1()
        new_s_c._37.move_6to1()

        return new_s_c

    def move_6to1_2(self) -> "SpeedCube":
        new_s_c = copy.deepcopy(self)

        new_s_c._12.move_6to1()
        new_s_c._15.move_6to1()
        new_s_c._18.move_6to1()

        new_s_c._22.move_6to1()
        new_s_c._25.move_6to1()
        new_s_c._28.move_6to1()

        new_s_c._33.move_6to1()
        new_s_c._36.move_6to1()
        new_s_c._39.move_6to1()

        return new_s_c

    def move_6to1_3(self) -> "SpeedCube":
        new_s_c = copy.deepcopy(self)

        new_s_c._13.move_6to1()
        new_s_c._16.move_6to1()
        new_s_c._19.move_6to1()

        new_s_c._23.move_6to1()
        new_s_c._26.move_6to1()
        new_s_c._29.move_6to1()

        new_s_c._33.move_6to1()
        new_s_c._36.move_6to1()
        new_s_c._39.move_6to1()

        return new_s_c

    def move_1to6_1(self) -> "SpeedCube":
        new_s_c = copy.deepcopy(self)

        new_s_c._11.move_1to6()
        new_s_c._14.move_1to6()
        new_s_c._17.move_1to6()

        new_s_c._21.move_1to6()
        new_s_c._24.move_1to6()
        new_s_c._27.move_1to6()

        new_s_c._31.move_1to6()
        new_s_c._34.move_1to6()
        new_s_c._37.move_1to6()

        return new_s_c

    def move_1to6_2(self) -> "SpeedCube":
        new_s_c = copy.deepcopy(self)

        new_s_c._12.move_1to6()
        new_s_c._15.move_1to6()
        new_s_c._18.move_1to6()

        new_s_c._22.move_1to6()
        new_s_c._25.move_1to6()
        new_s_c._28.move_1to6()

        new_s_c._33.move_1to6()
        new_s_c._36.move_1to6()
        new_s_c._39.move_1to6()

        return new_s_c

    def move_1to6_3(self) -> "SpeedCube":
        new_s_c = copy.deepcopy(self)

        new_s_c._13.move_1to6()
        new_s_c._16.move_1to6()
        new_s_c._19.move_1to6()

        new_s_c._23.move_1to6()
        new_s_c._26.move_1to6()
        new_s_c._29.move_1to6()

        new_s_c._33.move_1to6()
        new_s_c._36.move_1to6()
        new_s_c._39.move_1to6()

        return new_s_c

    def move_6to4_1(self) -> "SpeedCube":
        new_s_c = copy.deepcopy(self)

        new_s_c._11.move_6to4()
        new_s_c._12.move_6to4()
        new_s_c._13.move_6to4()

        new_s_c._14.move_6to4()
        new_s_c._15.move_6to4()
        new_s_c._16.move_6to4()

        new_s_c._17.move_6to4()
        new_s_c._18.move_6to4()
        new_s_c._19.move_6to4()

        return new_s_c

    def move_6to4_2(self) -> "SpeedCube":
        new_s_c = copy.deepcopy(self)

        new_s_c._21.move_6to4()
        new_s_c._22.move_6to4()
        new_s_c._23.move_6to4()

        new_s_c._24.move_6to4()
        new_s_c._25.move_6to4()
        new_s_c._26.move_6to4()

        new_s_c._27.move_6to4()
        new_s_c._28.move_6to4()
        new_s_c._29.move_6to4()

        return new_s_c

    def move_6to4_3(self) -> "SpeedCube":
        new_s_c = copy.deepcopy(self)

        new_s_c._31.move_6to4()
        new_s_c._32.move_6to4()
        new_s_c._33.move_6to4()

        new_s_c._34.move_6to4()
        new_s_c._35.move_6to4()
        new_s_c._36.move_6to4()

        new_s_c._37.move_6to4()
        new_s_c._38.move_6to4()
        new_s_c._39.move_6to4()

        return new_s_c

    def move_4_1to6(self) -> "SpeedCube":
        new_s_c = copy.deepcopy(self)

        new_s_c._11.move_4to6()
        new_s_c._12.move_4to6()
        new_s_c._13.move_4to6()

        new_s_c._14.move_4to6()
        new_s_c._15.move_4to6()
        new_s_c._16.move_4to6()

        new_s_c._17.move_4to6()
        new_s_c._18.move_4to6()
        new_s_c._19.move_4to6()

        return new_s_c

    def move_4_2to6(self) -> "SpeedCube":
        new_s_c = copy.deepcopy(self)

        new_s_c._21.move_4to6()
        new_s_c._22.move_4to6()
        new_s_c._23.move_4to6()

        new_s_c._24.move_4to6()
        new_s_c._25.move_4to6()
        new_s_c._26.move_4to6()

        new_s_c._27.move_4to6()
        new_s_c._28.move_4to6()
        new_s_c._29.move_4to6()

        return new_s_c

    def move_4_3to6(self) -> "SpeedCube":
        new_s_c = copy.deepcopy(self)

        new_s_c._31.move_4to6()
        new_s_c._32.move_4to6()
        new_s_c._33.move_4to6()

        new_s_c._34.move_4to6()
        new_s_c._35.move_4to6()
        new_s_c._36.move_4to6()

        new_s_c._37.move_4to6()
        new_s_c._38.move_4to6()
        new_s_c._39.move_4to6()

        return new_s_c