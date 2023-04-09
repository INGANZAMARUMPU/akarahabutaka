import copy
import sys
from cube import SpeedCube

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

def askLine():
    print("les couleurs: (R)ed (G)reen (B)lue (O)range (Y)ellow (W)hite")
    colors = []
    for y in range(3):
        ligne = []
        for x in range(3):
            value = input(f"ligne {y+1} couleur {x+1}")
            ligne.append(value)
        colors.append(ligne)

def build():

