import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from MyClass import World, Cell



world = World()
# world.make_alive([(1,1), (1,2), (1,3), (5,0)])
world.make_alive([(2,3), (2,4), (2,5), (3,5), (4,4)])
# world.evolve()
# print ("\n")
# world.print()
# print ("\n")
# world.draw_chessboard()
world.animation()