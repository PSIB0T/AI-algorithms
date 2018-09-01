import numpy as np

class Puzzle:

    # Constants that define puzzle movements
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

    def __init__(self, size):
        self.size = size
        self.puzzle = np.array([])
        self.blank = ()
        self.state = 0
        self._generate_puzzle()
    
    # Generates size X size puzzle
    def _generate_puzzle(self):
        self.state = 0
        self.puzzle = np.arange(self.size * self.size)
        # np.random.shuffle(self.puzzle)
        self.puzzle = self.puzzle.reshape(self.size, self.size)
        #  Stores the location of blank tile
        self.blank = tuple([x[0] for x in np.where(self.puzzle == 0)])
        self._calc_state()
    
    def _calc_state(self):
        i = 0
        for row in self.puzzle:
            for col in row:
                self.state = self.state + col * i
                i += 1
        print(self.state)
    
    def _abs_cell_number(self, cell):
        return self.size * cell[0] + cell[1]
    
    def _update_state(self, blank_old):
        arg_new = self.puzzle[blank_old]
        print("New arg is " + str(arg_new))
        self.state = self.state - self._abs_cell_number(self.blank) * arg_new + self._abs_cell_number(blank_old) * arg_new

    def move(self, direction):
        blank_old = self.blank
        if direction == self.DOWN:
            if self.blank[0] != 0:
                self.puzzle[self.blank], self.puzzle[self.blank[0] - 1, self.blank[1]] = self.puzzle[self.blank[0] - 1, self.blank[1]], self.puzzle[self.blank]
                self.blank = (self.blank[0] - 1, self.blank[1])

        if direction == self.UP:
            if self.blank[0] != self.size - 1:
                self.puzzle[self.blank], self.puzzle[self.blank[0] + 1, self.blank[1]] = self.puzzle[self.blank[0] + 1, self.blank[1]], self.puzzle[self.blank]
                self.blank = (self.blank[0] + 1, self.blank[1])

        if direction == self.LEFT:
            if self.blank[1] != self.size - 1:
                self.puzzle[self.blank], self.puzzle[self.blank[0], self.blank[1] + 1] = self.puzzle[self.blank[0], self.blank[1] + 1], self.puzzle[self.blank]
                self.blank = (self.blank[0], self.blank[1] + 1)

        if direction == self.RIGHT:
            if self.blank[1] != 0:
                self.puzzle[self.blank], self.puzzle[self.blank[0], self.blank[1] - 1] = self.puzzle[self.blank[0], self.blank[1] - 1], self.puzzle[self.blank]
                self.blank = (self.blank[0], self.blank[1] - 1)
        self._update_state(blank_old)


if __name__ == "__main__":
    p = Puzzle(2)
    