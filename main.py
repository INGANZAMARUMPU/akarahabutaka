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
    print(cube)
    
    # print("Saisissez la face 1:")
    # colors = askLine()

    # print("Saisissez la face 2:")
    # colors = askLine()
    # print(cube.face(2))

    # print("Saisissez la face 3:")
    # colors = askLine()

    # print(cube.face(3))

    # print("Saisissez la face 4:")
    # colors = askLine()

    # print(cube.face(4))

    # print("Saisissez la face 5:")
    # colors = askLine()

    # print(cube.face(5))

    # print("Saisissez la face 6:")
    # colors = askLine()


build()
