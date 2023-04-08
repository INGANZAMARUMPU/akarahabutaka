from cube import SpeedCube

cube = SpeedCube()
print(cube.face(2))
print(f"CUBE IS DONE" if cube.is_done else "CUBE IN ACTION")
cube.move_1to4_1()
print(cube.face(1))
print(cube.face(2))
print(cube.face(3))
print(f"CUBE IS DONE" if cube.is_done else "CUBE IN ACTION")