import copy
import sys
from cube import SpeedCube
from face import Color

MOVEMENTS = [
    "move_4to1_1", "move_4to1_3", "move_6to1_1", "move_6to1_3", "move_4to6_1", "move_4to6_3"
]

ITERATIONS = 10

def solve(objective:SpeedCube):
    founds = {objective}
    done = False

    for i in range(ITERATIONS):
        sys.stdout.write("\033[K")
        print(f"ROUND {i+1}/{ITERATIONS}")
        cubes = set(founds)
        state = 0
        maxi = len(cubes) * len(MOVEMENTS)
        for movement in MOVEMENTS:
            for current_cube in cubes:
                new_cube = copy.deepcopy(current_cube)
                performed = new_cube.perform(movement)
                if performed:
                    if new_cube.current_level == 6:
                        objective = new_cube
                        done = True
                        sys.stdout.write("\033[K")
                        print("DONE")
                        break
                    founds.add(new_cube)
                state += 1
                print(f"{state}/{maxi} {movement}", end='\r')
            if done: break
        if done: break

    for found in founds:
        if found.current_level > objective.current_level:
            objective = found
    return objective.steps

def askLine() -> list:
    dict_color = {
        "R": Color.RED,
        "G": Color.GREEN,
        "B": Color.BLUE,
        "O": Color.ORANGE,
        "Y": Color.YELLOW,
        "W": Color.WHITE,
    }
    print("les couleurs: (R)ed (G)reen (B)lue (O)range (Y)ellow (W)hite")
    colors = []
    for y in range(3):
        ligne = []
        for x in range(3):
            value = input(f"ligne {y+1} couleur {x+1}: ")
            color:Color = dict_color[value.upper()]
            ligne.append(color)
        colors.append(ligne)
    return colors

def build() -> SpeedCube:
    cube = SpeedCube()
    null = " "*7
    print(f"{null}|FACE 5|{null*2}\n|FACE 4|FACE 1|FACE 2|FACE 3|\n{null}|FACE 6|")
    
    # print("Saisissez la face 1:")
    # colors = askLine()
    # cube._11.c1 = colors[0][0]
    # cube._12.c1 = colors[0][1]
    # cube._13.c1 = colors[0][2]
    # cube._14.c1 = colors[1][0]
    # cube._15.c1 = colors[1][1]
    # cube._16.c1 = colors[1][2]
    # cube._17.c1 = colors[2][0]
    # cube._18.c1 = colors[2][1]
    # cube._19.c1 = colors[2][2]
    # print(cube.face(1))

    # print("Saisissez la face 2:")
    # colors = askLine()
    # cube._13.c2 = colors[0][2]
    # cube._16.c2 = colors[0][1]
    # cube._19.c2 = colors[0][0]
    # cube._23.c2 = colors[1][2]
    # cube._26.c2 = colors[1][1]
    # cube._29.c2 = colors[1][0]
    # cube._33.c2 = colors[2][2]
    # cube._36.c2 = colors[2][1]
    # cube._39.c2 = colors[2][0]
    # print(cube.face(2))

    # print("Saisissez la face 3:")
    # colors = askLine()
    # cube._31.c3 = colors[2][0]
    # cube._32.c3 = colors[2][1]
    # cube._33.c3 = colors[2][2]
    # cube._34.c3 = colors[1][0]
    # cube._35.c3 = colors[1][1]
    # cube._36.c3 = colors[1][2]
    # cube._37.c3 = colors[0][0]
    # cube._38.c3 = colors[0][1]
    # cube._39.c3 = colors[0][2]
    # print(cube.face(3))

    # print("Saisissez la face 4:")
    # colors = askLine()
    # cube._11.c4 = colors[0][0]
    # cube._14.c4 = colors[0][1]
    # cube._17.c4 = colors[0][2]
    # cube._21.c4 = colors[1][0]
    # cube._24.c4 = colors[1][1]
    # cube._27.c4 = colors[1][2]
    # cube._31.c4 = colors[2][0]
    # cube._34.c4 = colors[2][1]
    # cube._37.c4 = colors[2][2]
    # print(cube.face(4))

    # print("Saisissez la face 5:")
    # colors = askLine()
    # cube._11.c5 = colors[2][0]
    # cube._12.c5 = colors[2][1]
    # cube._13.c5 = colors[2][2]
    # cube._21.c5 = colors[1][0]
    # cube._22.c5 = colors[1][1]
    # cube._23.c5 = colors[1][2]
    # cube._31.c5 = colors[0][0]
    # cube._32.c5 = colors[0][1]
    # cube._33.c5 = colors[0][2]
    # print(cube.face(5))

    print("Saisissez la face 6:")
    colors = askLine()
    cube._17.c6 = colors[0][0]
    cube._18.c6 = colors[0][1]
    cube._19.c6 = colors[0][2]
    cube._27.c6 = colors[1][0]
    cube._28.c6 = colors[1][1]
    cube._29.c6 = colors[1][2]
    cube._37.c6 = colors[2][0]
    cube._38.c6 = colors[2][1]
    cube._39.c6 = colors[2][2]
    print(cube.face(6))

    cube_2 = SpeedCube()
    cube_2.move_4to6_1()
    print(cube_2.face(6))

build()
