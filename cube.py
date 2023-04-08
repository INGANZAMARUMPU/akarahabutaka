from typing import List
from face import Node, Color

class SpeedCube:
    def __init__(self):
        self._11:Node = Node(Color.RED, None, None, Color.BLUE, Color.YELLOW, None)
        self._12:Node = Node(Color.RED, None, None, None, Color.YELLOW, None)
        self._13:Node = Node(Color.RED, Color.GREEN, None, None, Color.YELLOW, None)
        self._14:Node = Node(Color.RED, None, None, Color.BLUE, None, None)
        self._15:Node = Node(Color.RED, None, None, None, None, None)
        self._16:Node = Node(Color.RED, Color.GREEN, None, None, None, None)
        self._17:Node = Node(Color.RED, None, None, Color.BLUE, None, Color.WHITE)
        self._18:Node = Node(Color.RED, None, None, None, None, Color.WHITE)
        self._19:Node = Node(Color.RED, Color.GREEN, None, None, None, Color.WHITE)

        self._21:Node = Node( None, None, None, Color.BLUE, Color.YELLOW, None)
        self._22:Node = Node( None, None, None, None, Color.YELLOW, None)
        self._23:Node = Node( None, Color.GREEN, None, None, Color.YELLOW, None)
        self._24:Node = Node( None, None, None, Color.BLUE, None, None)
        self._25:Node = Node( None, None, None, None, None, None)
        self._26:Node = Node( None, Color.GREEN, None, None, None, None)
        self._27:Node = Node( None, None, None,  Color.BLUE, None, Color.WHITE)
        self._28:Node = Node( None, None, None, None, None, Color.WHITE)
        self._29:Node = Node( None, Color.GREEN, None, None, None, Color.WHITE)

        self._31:Node = Node(None, None, Color.ORANGE, Color.BLUE, Color.YELLOW, None)
        self._32:Node = Node(None, None, Color.ORANGE, None, Color.YELLOW, None)
        self._33:Node = Node(None, Color.GREEN, Color.ORANGE, None, Color.YELLOW, None)
        self._34:Node = Node(None, None, Color.ORANGE, Color.BLUE, None, None)
        self._35:Node = Node(None, None, Color.ORANGE, None, None, None)
        self._36:Node = Node(None, Color.GREEN, Color.ORANGE, None, None, None)
        self._37:Node = Node(None, None, Color.ORANGE, Color.BLUE, None, Color.WHITE)
        self._38:Node = Node(None, None, Color.ORANGE, None, None, Color.WHITE)
        self._39:Node = Node(None, Color.GREEN, Color.ORANGE, None, None, Color.WHITE)

    @property
    def faces(self)->List[List[Color]]:
        return [
            [
                self._11.c1, self._12.c1, self._13.c1,
                self._14.c1, self._15.c1, self._16.c1,
                self._17.c1, self._18.c1, self._19.c1
            ],
            [
                self._13.c2, self._16.c2, self._19.c2,
                self._23.c2, self._26.c2, self._29.c2,
                self._33.c2, self._36.c2, self._39.c2
            ],
            [
                self._31.c3, self._32.c3, self._33.c3,
                self._34.c3, self._35.c3, self._36.c3,
                self._37.c3, self._38.c3, self._39.c3
            ],
            [
                self._11.c4, self._14.c4, self._17.c4,
                self._21.c4, self._24.c4, self._27.c4,
                self._31.c4, self._34.c4, self._37.c4
            ],
            [
                self._11.c5, self._12.c5, self._13.c5,
                self._21.c5, self._22.c5, self._23.c5,
                self._31.c5, self._32.c5, self._33.c5
            ],
            [
                self._17.c6, self._18.c6, self._19.c6,
                self._27.c6, self._28.c6, self._29.c6,
                self._37.c6, self._38.c6, self._39.c6
            ],
        ]
    
    @property
    def is_done(self) -> bool:
        return (
            self._11.c1==self._12.c1==self._13.c1==self._14.c1==self._15.c1==self._16.c1==self._17.c1==self._18.c1==self._19.c1 and
            self._13.c2==self._16.c2==self._19.c2==self._23.c2==self._26.c2==self._29.c2==self._33.c2==self._36.c2==self._39.c2 and
            self._31.c3==self._32.c3==self._33.c3==self._34.c3==self._35.c3==self._36.c3==self._37.c3==self._38.c3==self._39.c3 and
            self._11.c4==self._14.c4==self._17.c4==self._21.c4==self._24.c4==self._27.c4==self._31.c4==self._34.c4==self._37.c4 and
            self._11.c5==self._12.c5==self._13.c5==self._21.c5==self._22.c5==self._23.c5==self._31.c5==self._32.c5==self._33.c5 and
            self._17.c6==self._18.c6==self._19.c6==self._27.c6==self._28.c6==self._29.c6==self._37.c6==self._38.c6==self._39.c6
        )
    
    def face(self, number) -> str:
        if number < 1 or number > 6: return "[ERREUR] seul les faces [1 - 6] sont valides"
        face = f"Face Numero {number}\n"
        for i, f in enumerate(self.faces[number-1]):
            if(i%3 == 2):
                face += (f"{f.value:6}" if f else "XXX   ") + "\n"
            else:
                face += (f"{f.value:6}" if f else "XXX   ") +" "
        return face
    
    def __eq__(self, cube:"SpeedCube") -> bool:
        return str(self.faces) == str(cube.faces)
    
    def __hash__(self) -> int:
        return hash(str(self))

    def move_4to1_1(self):
        self._11.move_4to1()
        self._12.move_4to1()
        self._13.move_4to1()

        self._21.move_4to1()
        self._22.move_4to1()
        self._23.move_4to1()
        
        self._31.move_4to1()
        self._32.move_4to1()
        self._33.move_4to1()

    def move_4to1_2(self):
        self._14.move_4to1()
        self._15.move_4to1()
        self._16.move_4to1()

        self._24.move_4to1()
        self._25.move_4to1()
        self._26.move_4to1()
        
        self._34.move_4to1()
        self._35.move_4to1()
        self._36.move_4to1()

    def move_4to1_3(self):
        self._17.move_4to1()
        self._18.move_4to1()
        self._19.move_4to1()

        self._27.move_4to1()
        self._28.move_4to1()
        self._29.move_4to1()
        
        self._37.move_4to1()
        self._38.move_4to1()
        self._39.move_4to1()

    def move_1to4_1(self):
        self._11.move_1to4()
        self._12.move_1to4()
        self._13.move_1to4()

        self._21.move_1to4()
        self._22.move_1to4()
        self._23.move_1to4()
        
        self._31.move_1to4()
        self._32.move_1to4()
        self._33.move_1to4()
        
        self._11, self._12, self._13, self._21, self._22, self._23, self._31, self._32, self._33 =\
        self._31, self._21, self._11, self._32, self._22, self._12, self._33, self._23, self._13

    def move_1to4_2(self):
        self._14.move_1to4()
        self._15.move_1to4()
        self._16.move_1to4()

        self._24.move_1to4()
        self._25.move_1to4()
        self._26.move_1to4()
        
        self._34.move_1to4()
        self._35.move_1to4()
        self._36.move_1to4()

    def move_1to4_3(self):
        self._17.move_1to4()
        self._18.move_1to4()
        self._19.move_1to4()

        self._27.move_1to4()
        self._28.move_1to4()
        self._29.move_1to4()
        
        self._37.move_1to4()
        self._38.move_1to4()
        self._39.move_1to4()

    def move_6to1_1(self):
        self._11.move_6to1()
        self._14.move_6to1()
        self._17.move_6to1()

        self._21.move_6to1()
        self._24.move_6to1()
        self._27.move_6to1()

        self._31.move_6to1()
        self._34.move_6to1()
        self._37.move_6to1()

    def move_6to1_2(self):
        self._12.move_6to1()
        self._15.move_6to1()
        self._18.move_6to1()

        self._22.move_6to1()
        self._25.move_6to1()
        self._28.move_6to1()

        self._33.move_6to1()
        self._36.move_6to1()
        self._39.move_6to1()

    def move_6to1_3(self):
        self._13.move_6to1()
        self._16.move_6to1()
        self._19.move_6to1()

        self._23.move_6to1()
        self._26.move_6to1()
        self._29.move_6to1()

        self._33.move_6to1()
        self._36.move_6to1()
        self._39.move_6to1()

    def move_1to6_1(self):
        self._11.move_1to6()
        self._14.move_1to6()
        self._17.move_1to6()

        self._21.move_1to6()
        self._24.move_1to6()
        self._27.move_1to6()

        self._31.move_1to6()
        self._34.move_1to6()
        self._37.move_1to6()

    def move_1to6_2(self):
        self._12.move_1to6()
        self._15.move_1to6()
        self._18.move_1to6()

        self._22.move_1to6()
        self._25.move_1to6()
        self._28.move_1to6()

        self._33.move_1to6()
        self._36.move_1to6()
        self._39.move_1to6()

    def move_1to6_3(self):
        self._13.move_1to6()
        self._16.move_1to6()
        self._19.move_1to6()

        self._23.move_1to6()
        self._26.move_1to6()
        self._29.move_1to6()

        self._33.move_1to6()
        self._36.move_1to6()
        self._39.move_1to6()

    def move_6to4_1(self):
        self._11.move_6to4()
        self._12.move_6to4()
        self._13.move_6to4()

        self._14.move_6to4()
        self._15.move_6to4()
        self._16.move_6to4()

        self._17.move_6to4()
        self._18.move_6to4()
        self._19.move_6to4()

    def move_6to4_2(self):
        self._21.move_6to4()
        self._22.move_6to4()
        self._23.move_6to4()

        self._24.move_6to4()
        self._25.move_6to4()
        self._26.move_6to4()

        self._27.move_6to4()
        self._28.move_6to4()
        self._29.move_6to4()

    def move_6to4_3(self):
        self._31.move_6to4()
        self._32.move_6to4()
        self._33.move_6to4()

        self._34.move_6to4()
        self._35.move_6to4()
        self._36.move_6to4()

        self._37.move_6to4()
        self._38.move_6to4()
        self._39.move_6to4()

    def move_4_1to6(self):
        self._11.move_4to6()
        self._12.move_4to6()
        self._13.move_4to6()

        self._14.move_4to6()
        self._15.move_4to6()
        self._16.move_4to6()

        self._17.move_4to6()
        self._18.move_4to6()
        self._19.move_4to6()

    def move_4_2to6(self):
        self._21.move_4to6()
        self._22.move_4to6()
        self._23.move_4to6()

        self._24.move_4to6()
        self._25.move_4to6()
        self._26.move_4to6()

        self._27.move_4to6()
        self._28.move_4to6()
        self._29.move_4to6()

    def move_4_3to6(self):
        self._31.move_4to6()
        self._32.move_4to6()
        self._33.move_4to6()

        self._34.move_4to6()
        self._35.move_4to6()
        self._36.move_4to6()

        self._37.move_4to6()
        self._38.move_4to6()
        self._39.move_4to6()