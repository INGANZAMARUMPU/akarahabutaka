import copy
from cube import SpeedCube

MOVEMENTS = [
    "move_4to1_1", "move_4to1_3", "move_6to1_1", "move_6to1_3", "move_4to6_1", "move_4to6_3"
]
ITERATIONS = 5

cube = SpeedCube()
print("======= move_4to1_3 ========")
cube.move_4to1_3()
print(cube.face(1))
print(cube.face(2))
print(cube.face(3))
print(cube.face(4))
print(cube.face(5))
print(cube.face(6))

# founds = { cube }
# done = False

# for i in range(ITERATIONS):
#     print(f"{i+1}/{ITERATIONS} on {len(founds)} iterations\r")
#     cubes = set(founds)
#     for current_cube in cubes:
#         new_cube = copy.deepcopy(current_cube)
#         for movement in MOVEMENTS:
#             performed = new_cube.perform(movement)
#             if new_cube.current_level == 6:
#                 cube = new_cube
#                 done = True
#                 break
#             if performed and new_cube not in founds:
#                 founds.add(new_cube)
#         if done: break
#     if done: break

# for found in founds:
#     if found.current_level > cube.current_level:
#         cube = found

# print(cube.steps)
