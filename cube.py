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

        self.steps = []
        self.actions = {
            "move_4to1_1": self.move_4to1_1,
            "move_4to1_3": self.move_4to1_3,
            "move_1to6_1": self.move_1to6_1,
            "move_1to6_3": self.move_1to6_3,
            "move_4to6_1": self.move_4to6_1,
            "move_4to6_3": self.move_4to6_3
        }

    @property
    def faces(self)->List[List[Color]]:
        return [
            [
                self._11.c1, self._12.c1, self._13.c1,
                self._14.c1, self._15.c1, self._16.c1,
                self._17.c1, self._18.c1, self._19.c1
            ],
            [
                self._13.c2, self._23.c2, self._33.c2,
                self._16.c2, self._26.c2, self._36.c2,
                self._19.c2, self._29.c2, self._39.c2
            ],
            [
                self._33.c3, self._32.c3, self._31.c3,
                self._36.c3, self._35.c3, self._34.c3,
                self._39.c3, self._38.c3, self._37.c3
            ],
            [
                self._31.c4, self._34.c4, self._37.c4,
                self._21.c4, self._24.c4, self._27.c4,
                self._11.c4, self._14.c4, self._17.c4
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
    def current_level(self) -> bool:
        level = 0
        if self._11.c1==self._12.c1==self._13.c1==self._14.c1==self._15.c1==self._16.c1==self._17.c1==self._18.c1==self._19.c1:
            level += 1
        if self._13.c2==self._16.c2==self._19.c2==self._23.c2==self._26.c2==self._29.c2==self._33.c2==self._36.c2==self._39.c2:
            level += 1
        if self._31.c3==self._32.c3==self._33.c3==self._34.c3==self._35.c3==self._36.c3==self._37.c3==self._38.c3==self._39.c3:
            level += 1
        if self._11.c4==self._14.c4==self._17.c4==self._21.c4==self._24.c4==self._27.c4==self._31.c4==self._34.c4==self._37.c4:
            level += 1
        if self._11.c5==self._12.c5==self._13.c5==self._21.c5==self._22.c5==self._23.c5==self._31.c5==self._32.c5==self._33.c5:
            level += 1
        if self._17.c6==self._18.c6==self._19.c6==self._27.c6==self._28.c6==self._29.c6==self._37.c6==self._38.c6==self._39.c6:
            level += 1
        return level
    
    def __eq__(self, cube:"SpeedCube") -> bool:
        return str(self.faces) == str(cube.faces)
    
    def __hash__(self) -> int:
        str_faces_list = []
        for face in self.faces:
            str_face = ""
            for color in face:
                str_face += color.value if color else "_"
            str_faces_list.append(str_face)
        return hash("".join(str_faces_list))
    
    def step_excuded(self, step) -> bool:
        if(len(self.steps) == 0):
            return False
        if self.steps[-1] == step:
            return True
        if len(self.steps) < 3: return False

        if self.steps[-1] == self.steps[-2] == self.steps[-3] == step:
            return True
    
    def face(self, number) -> str:
        if number < 1 or number > 6: return "[ERREUR] seul les faces [1 - 6] sont valides"
        face = f"Face Numero {number}\n"
        for i, f in enumerate(self.faces[number-1]):
            if(i%3 == 2):
                face += (f"{f.value:6}" if f else "XXX   ") + "\n"
            else:
                face += (f"{f.value:6}" if f else "XXX   ") +" "
        return face

    def move_4to1_1(self):
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

    def move_4to1_3(self):
        self._17.move_1to4()
        self._18.move_1to4()
        self._19.move_1to4()

        self._27.move_1to4()
        self._28.move_1to4()
        self._29.move_1to4()
        
        self._37.move_1to4()
        self._38.move_1to4()
        self._39.move_1to4()

        self._17, self._18, self._19, self._27, self._28, self._29, self._37, self._38, self._39 =\
        self._37, self._27, self._17, self._38, self._28, self._18, self._39, self._28, self._19

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
        
        self._11, self._14, self._17, self._21, self._24, self._27, self._31, self._34, self._37 =\
        self._17, self._27, self._37, self._14, self._24, self._34, self._11, self._21, self._31

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
        
        self._13, self._16, self._19, self._23, self._26, self._29, self._33, self._36, self._39 =\
        self._19, self._29, self._39, self._16, self._26, self._36, self._13, self._23, self._33
        

    def move_4to6_1(self):
        self._11.move_4to6()
        self._12.move_4to6()
        self._13.move_4to6()
        self._14.move_4to6()
        self._15.move_4to6()
        self._16.move_4to6()
        self._17.move_4to6()
        self._18.move_4to6()
        self._19.move_4to6()
        
        self._11, self._12, self._13, self._14, self._15, self._16, self._17, self._18, self._19 =\
        self._13, self._16, self._19, self._12, self._15, self._18, self._11, self._14, self._17

    def move_4to6_3(self):
        self._31.move_4to6()
        self._32.move_4to6()
        self._33.move_4to6()
        self._34.move_4to6()
        self._35.move_4to6()
        self._36.move_4to6()
        self._37.move_4to6()
        self._38.move_4to6()
        self._39.move_4to6()
        
        self._31, self._32, self._33, self._34, self._35, self._36, self._37, self._38, self._39 =\
        self._33, self._36, self._39, self._32, self._35, self._38, self._31, self._34, self._37

    def perform(self, action) -> bool:
        if not self.step_excuded(action):
            self.actions[action]()
            self.steps.append(action)
            return True
        return False