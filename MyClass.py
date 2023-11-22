import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class World:
    def __init__(self, width = 10, height = 10):
        self.width = width
        self.height = height
        self.board = [[Cell(0) for i in range(width)] for j in range(height)]
        
    def make_alive(self, locations = [(int,int)]):
        """!
        @param locations: a list of tuples of the form (x,y) where 0 <= x < width and 0 <= y < height
        """
        for location in locations:
            try:
                self.board[location[0]][location[1]].status = 1
            except:
                raise ValueError(f"Invalid location, note that the board is of size {self.width} * {self.height}, please pass in a valid location of the form (x,y) where 0 <= x < {self.width} and 0 <= y < {self.height}")
    
    def get_neighbour_loc(self, i: int, j:int) -> list((int,int)): 

        left = ((i+self.width-1)%self.width, j)
        right = ((i+1)%self.width, j)
        up = (i, (j+self.height-1)%self.height)
        down = (i, (j+1)%self.height)
        left_up = ((i+self.width-1)%self.width, (j+self.height-1)%self.height)
        left_down = ((i+self.width-1)%self.width, (j+1)%self.height)
        right_up = ((i+1)%self.width, (j+self.height-1)%self.height)
        right_down = ((i+1)%self.width, (j+1)%self.height)

        return [left, right, up, down, left_up, left_down, right_up, right_down]
    
    def evolve(self):

        for i in range(self.height):
            for j in range(self.width):
                neighbours = [self.board[x[0]][x[1]] for x in self.get_neighbour_loc(i,j)]
                self.board[i][j].evolve(neighbours)
        
        for i in range(self.height):
            for j in range(self.width):
                self.board[i][j].status = self.board[i][j].next_status

    def print(self):
        for i in range(self.height):
            for j in range(self.width):
                print(self.board[i][j].status, end = " ")
            print("\n")

    def update(self,frame):
        self.ax.clear()
        print ("Frame:",frame)
        self.draw_chessboard(frame)
        self.evolve()
        
        
    def draw_chessboard(self,frame):
        colors = ['white', 'black']
        for i in range(self.height):
            for j in range(self.width):
                color = colors[self.board[i][j].status]
                rect = plt.Rectangle((i,j), 1, 1, facecolor = color, edgecolor='black')
                self.ax.add_patch(rect)
                # self.legend = plt.text(0, 0, f"Frame: {frame}", ha="left", va="bottom", color="black", fontsize=12)
    
    def animation(self):
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim(0, self.width)
        self.ax.set_ylim(0, self.height)
        self.ax.set_aspect('equal', 'box')
        animation = FuncAnimation(self.fig, self.update, frames = np.arange(1,39), interval = 100, repeat = False)
        animation.save('animated_chessboard.gif', writer='ffmpeg') 
        # plt.show()


class Cell:
    def __init__(self, status):
        self.status = status
        if status not in [0, 1]:
            raise ValueError("Invalid status, please pass in 0 or 1")
        self.next_status = status
    
    def evolve(self, neighbours: ["Cell"]):
        total_neighbours_status = sum(x.status for x in neighbours)
        if total_neighbours_status < 2 and self.status == 1:
            # Case 1: Underpopulation
            self.next_status = 0
        elif total_neighbours_status > 3 and self.status == 1:
            # Case 2: Overpopulation
            self.next_status = 0
        elif total_neighbours_status == 3 and self.status == 0:
            # Case 3: Reproduction
            self.next_status = 1
        else:
            # Case 4: Survival
            self.next_status = self.status


