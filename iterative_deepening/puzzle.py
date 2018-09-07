import numpy as np
import random
import copy

class Puzzle:

    # Constants that define puzzle movements
    UP = 0
    DOWN = 2
    LEFT = 1
    RIGHT = 3

    def __init__(self, size):
        self.size = size
        self.puzzle = np.array([])
        self.blank = ()
        self.state = 0
        self.target_state = 0
        self._generate_puzzle()

    def get_moves(self):
        # All legal moves in the puzzle
        possible_moves = [self.UP, self.LEFT, self.DOWN, self.RIGHT]
        # Moves that can be made in the current situation
        right_moves = []
        for move in possible_moves:
            if self.move(move):
                right_moves.append(copy.deepcopy(self))
                self.move((move + 2) % 4)
        return right_moves
    
    # Generates size X size puzzle
    def _generate_puzzle(self):
        self.state = 0
        self.puzzle = np.arange(self.size * self.size)
        # np.random.shuffle(self.puzzle)
        self.puzzle = self.puzzle.reshape(self.size, self.size)
        #  Stores the location of blank tile
        self.blank = tuple([x[0] for x in np.where(self.puzzle == 0)])
        self.target_state = self._calc_state()
        self.shuffle(10)
    
    def _calc_state(self):
        return " ".join([str(i) for i in self.puzzle.ravel()])

    def shuffle(self, times):
        possible_moves = [self.UP, self.LEFT, self.DOWN, self.RIGHT]
        for i in range(times):
            self.move(random.choice(possible_moves))
    
    def _abs_cell_number(self, cell):
        return self.size * cell[0] + cell[1]

    def move(self, direction):
        isPossible = False
        if direction == self.DOWN:
            if self.blank[0] != 0:
                isPossible = True
                self.puzzle[self.blank], self.puzzle[self.blank[0] - 1, self.blank[1]] = self.puzzle[self.blank[0] - 1, self.blank[1]], self.puzzle[self.blank]
                self.blank = (self.blank[0] - 1, self.blank[1])

        if direction == self.UP:
            if self.blank[0] != self.size - 1:
                isPossible = True
                self.puzzle[self.blank], self.puzzle[self.blank[0] + 1, self.blank[1]] = self.puzzle[self.blank[0] + 1, self.blank[1]], self.puzzle[self.blank]
                self.blank = (self.blank[0] + 1, self.blank[1])

        if direction == self.LEFT:
            if self.blank[1] != self.size - 1:
                isPossible = True
                self.puzzle[self.blank], self.puzzle[self.blank[0], self.blank[1] + 1] = self.puzzle[self.blank[0], self.blank[1] + 1], self.puzzle[self.blank]
                self.blank = (self.blank[0], self.blank[1] + 1)

        if direction == self.RIGHT:
            if self.blank[1] != 0:
                isPossible = True
                self.puzzle[self.blank], self.puzzle[self.blank[0], self.blank[1] - 1] = self.puzzle[self.blank[0], self.blank[1] - 1], self.puzzle[self.blank]
                self.blank = (self.blank[0], self.blank[1] - 1)
        self.state = self._calc_state()
        return isPossible