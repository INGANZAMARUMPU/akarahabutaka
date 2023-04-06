import copy
from .face import Node, color

class SpeedCube:
    def __init__(self):
        self._11:Node = Node(color.RED, None, None, color.WHITE, color.BLUE, None)
        self._12:Node = Node(color.RED, None, None, None, color.GREEN, None)
        self._13:Node = Node(color.YELLOW, color.RED, None, None, color.GREEN, None)
        self._14:Node = Node(color.GREEN, None, None, color.WHITE, None, None)
        self._15:Node = Node(color.ORANGE, None, None, None, None, None)
        self._16:Node = Node(color.WHITE, color.BLUE, None, None, None, None)
        self._17:Node = Node(color.RED, None, None, color.YELLOW, None, color.BLUE)
        self._18:Node = Node(color.ORANGE, None, None, None, None, color.GREEN)
        self._19:Node = Node(color.WHITE, color.ORANGE, None, None, None, color.BLUE)

        self._21:Node = Node(None, None, None, color.ORANGE, color.WHITE, None)
        self._22:Node = Node(None, None, None, None, color.WHITE, None)
        self._23:Node = Node(None, color.RED, None, None, color.WHITE, None)
        self._24:Node = Node(None, color.GREEN, None, None, None, None)
        self._25:Node = Node(None, None, None, None, None, None)
        self._26:Node = Node(None, color.RED, None, None, None, None)
        self._27:Node = Node(None, None, None, color.BLUE, None, color.YELLOW)
        self._28:Node = Node(None, None, None, None, None, color.YELLOW)
        self._29:Node = Node(None, color.RED, None, None, None, color.YELLOW)

        self._31:Node = Node(None, None, color.ORANGE, color.GREEN, color.WHITE)
        self._32:Node = Node(None, None, color.ORANGE, None, color.BLUE,None)
        self._33:Node = Node(None, color.GREEN, color.RED, None, color.WHITE, None)
        self._34:Node = Node(None, None, color.YELLOW, color.ORANGE, None, None)
        self._35:Node = Node(None, None, color.BLUE, None, None, None)
        self._36:Node = Node(None, color.YELLOW, color.GREEN, None, None, None)
        self._37:Node = Node(None, None, color.YELLOW, color.BLUE, None, color.ORANGE)
        self._38:Node = Node(None, None, color.RED, None, None, color.BLUE)
        self._39:Node = Node(None, color.GREEN, color.YELLOW, None, None, color.ORANGE)

    @property
    def faces(self)->list:
        return [
            self._11.c1+self._12.c1+self._13.c1+self._14.c1+self._15.c1+self._16.c1+self._17.c1+self._18.c1+self._19.c1,
            self._21.c2+self._22.c2+self._23.c2+self._24.c2+self._25.c2+self._26.c2+self._27.c2+self._28.c2+self._29.c2,
            self._31.c3+self._32.c3+self._33.c3+self._34.c3+self._35.c3+self._36.c3+self._37.c3+self._38.c3+self._39.c3,
            self._41.c4+self._42.c4+self._43.c4+self._44.c4+self._45.c4+self._46.c4+self._47.c4+self._48.c4+self._49.c4,
            self._51.c5+self._52.c5+self._53.c5+self._54.c5+self._55.c5+self._56.c5+self._57.c5+self._58.c5+self._59.c5,
            self._61.c6+self._62.c6+self._63.c6+self._64.c6+self._65.c6+self._66.c6+self._67.c6+self._68.c6+self._69.c6
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

        new_s_c._41.move_4to1()
        new_s_c._42.move_4to1()
        new_s_c._43.move_4to1()

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

        new_s_c._44.move_4to1()
        new_s_c._45.move_4to1()
        new_s_c._46.move_4to1()

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

        new_s_c._47.move_4to1()
        new_s_c._48.move_4to1()
        new_s_c._49.move_4to1()
        
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

        new_s_c._41.move_1to4()
        new_s_c._42.move_1to4()
        new_s_c._43.move_1to4()

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

        new_s_c._44.move_1to4()
        new_s_c._45.move_1to4()
        new_s_c._46.move_1to4()

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

        new_s_c._47.move_1to4()
        new_s_c._48.move_1to4()
        new_s_c._49.move_1to4()
        
        return new_s_c

    def move_6to1_1(self) -> "SpeedCube":
        new_s_c = copy.deepcopy(self)

        new_s_c._11.move_6to1()
        new_s_c._41.move_6to1()
        new_s_c._71.move_6to1()

        new_s_c._16.move_6to1()
        new_s_c._46.move_6to1()
        new_s_c._76.move_6to1()

        new_s_c._13.move_6to1()
        new_s_c._43.move_6to1()
        new_s_c._73.move_6to1()

        new_s_c._15.move_6to1()
        new_s_c._45.move_6to1()
        new_s_c._75.move_6to1()

        return new_s_c

    def move_6to1_2(self) -> "SpeedCube":
        new_s_c = copy.deepcopy(self)

        new_s_c._21.move_6to1()
        new_s_c._51.move_6to1()
        new_s_c._81.move_6to1()

        new_s_c._26.move_6to1()
        new_s_c._56.move_6to1()
        new_s_c._86.move_6to1()

        new_s_c._23.move_6to1()
        new_s_c._53.move_6to1()
        new_s_c._83.move_6to1()

        new_s_c._25.move_6to1()
        new_s_c._55.move_6to1()
        new_s_c._85.move_6to1()

        return new_s_c

    def move_6to1_3(self) -> "SpeedCube":
        new_s_c = copy.deepcopy(self)

        new_s_c._31.move_6to1()
        new_s_c._61.move_6to1()
        new_s_c._91.move_6to1()

        new_s_c._36.move_6to1()
        new_s_c._66.move_6to1()
        new_s_c._96.move_6to1()

        new_s_c._33.move_6to1()
        new_s_c._63.move_6to1()
        new_s_c._93.move_6to1()

        new_s_c._35.move_6to1()
        new_s_c._65.move_6to1()
        new_s_c._95.move_6to1()

        return new_s_c

    def move_1to6_1(self) -> "SpeedCube":
        new_s_c = copy.deepcopy(self)

        new_s_c._11.move_1to6()
        new_s_c._41.move_1to6()
        new_s_c._71.move_1to6()

        new_s_c._16.move_1to6()
        new_s_c._46.move_1to6()
        new_s_c._76.move_1to6()

        new_s_c._13.move_1to6()
        new_s_c._43.move_1to6()
        new_s_c._73.move_1to6()

        new_s_c._15.move_1to6()
        new_s_c._45.move_1to6()
        new_s_c._75.move_1to6()

        return new_s_c

    def move_1to6_2(self) -> "SpeedCube":
        new_s_c = copy.deepcopy(self)

        new_s_c._21.move_1to6()
        new_s_c._51.move_1to6()
        new_s_c._81.move_1to6()

        new_s_c._26.move_1to6()
        new_s_c._56.move_1to6()
        new_s_c._86.move_1to6()

        new_s_c._23.move_1to6()
        new_s_c._53.move_1to6()
        new_s_c._83.move_1to6()

        new_s_c._25.move_1to6()
        new_s_c._55.move_1to6()
        new_s_c._85.move_1to6()

        return new_s_c

    def move_1to6_3(self) -> "SpeedCube":
        new_s_c = copy.deepcopy(self)

        new_s_c._31.move_1to6()
        new_s_c._61.move_1to6()
        new_s_c._91.move_1to6()

        new_s_c._36.move_1to6()
        new_s_c._66.move_1to6()
        new_s_c._96.move_1to6()

        new_s_c._33.move_1to6()
        new_s_c._63.move_1to6()
        new_s_c._93.move_1to6()

        new_s_c._35.move_1to6()
        new_s_c._65.move_1to6()
        new_s_c._95.move_1to6()

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
        new_s_c._51.move_6to4()
        new_s_c._81.move_6to4()

        new_s_c._26.move_6to4()
        new_s_c._56.move_6to4()
        new_s_c._86.move_6to4()

        new_s_c._23.move_6to4()
        new_s_c._53.move_6to4()
        new_s_c._83.move_6to4()

        new_s_c._25.move_6to4()
        new_s_c._55.move_6to4()
        new_s_c._85.move_6to4()

        return new_s_c

    def move_6to4_3(self) -> "SpeedCube":
        new_s_c = copy.deepcopy(self)

        new_s_c._31.move_6to4()
        new_s_c._61.move_6to4()
        new_s_c._91.move_6to4()

        new_s_c._36.move_6to4()
        new_s_c._66.move_6to4()
        new_s_c._96.move_6to4()

        new_s_c._33.move_6to4()
        new_s_c._63.move_6to4()
        new_s_c._93.move_6to4()

        new_s_c._35.move_6to4()
        new_s_c._65.move_6to4()
        new_s_c._95.move_6to4()

        return new_s_c