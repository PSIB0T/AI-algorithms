import numpy as np

class Puzzle:

    # Constants that define puzzle movements
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

    def __init__(self, size):
        self.size = size
        self._generate_puzzle()
    
    # Generates size X size puzzle
    def _generate_puzzle(self):
        self.puzzle = np.arange(self.size * self.size)
        np.random.shuffle(self.puzzle)
        self.puzzle = self.puzzle.reshape(self.size, self.size)
        #  Stores the location of blank tile
        self.blank = tuple([x[0] for x in np.where(self.puzzle == 0)])
    
    def move(self, direction):
        if direction == self.UP:
            if self.blank[0] != 0:
                self.puzzle[self.blank], self.puzzle[self.blank[0] - 1, self.blank[1]] = self.puzzle[self.blank[0] - 1, self.blank[1]], self.puzzle[self.blank]
                self.blank = (self.blank[0] - 1, self.blank[1])

        if direction == self.DOWN:
            if self.blank[0] != self.size - 1:
                self.puzzle[self.blank], self.puzzle[self.blank[0] + 1, self.blank[1]] = self.puzzle[self.blank[0] + 1, self.blank[1]], self.puzzle[self.blank]
                self.blank = (self.blank[0] + 1, self.blank[1])

        if direction == self.RIGHT:
            if self.blank[1] != self.size - 1:
                self.puzzle[self.blank], self.puzzle[self.blank[0], self.blank[1] + 1] = self.puzzle[self.blank[0], self.blank[1] + 1], self.puzzle[self.blank]
                self.blank = (self.blank[0], self.blank[1] + 1)

        if direction == self.LEFT:
            if self.blank[1] != 0:
                self.puzzle[self.blank], self.puzzle[self.blank[0], self.blank[1] - 1] = self.puzzle[self.blank[0], self.blank[1] - 1], self.puzzle[self.blank]
                self.blank = (self.blank[0], self.blank[1] - 1)


if __name__ == "__main__":
    p = Puzzle(4)
    print(p.puzzle)
    p.move(p.UP)
    print(p.puzzle)
    p.move(p.RIGHT)
    print(p.puzzle)