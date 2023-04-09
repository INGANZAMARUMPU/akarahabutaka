import copy
from cube import SpeedCube

movements = [
    "move_4to1_1", "move_4to1_3", "move_1to6_1", "move_1to6_3", "move_4to6_1", "move_4to6_3"
]

cube = SpeedCube()

founds = { cube }

for i in range(40):
    cubes = set(founds)
    for cube in cubes:
        new_cube = copy.deepcopy(cube)
        for movement in movements:
            performed = new_cube.perform(movement)
            if performed and new_cube not in founds:
                founds.add(new_cube)

for found in founds:
    if found.current_level > cube.current_level:
        cube = found

print(cube.steps)
