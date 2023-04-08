from cube import SpeedCube

cube = SpeedCube()
print(cube.face(1))
print(f"CUBE IS DONE" if cube.is_done else "CUBE IN ACTION")
cube.move_4to1_3()
print(cube.face(1))
print(cube.face(2))
print(cube._13)