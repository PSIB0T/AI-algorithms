from puzzle import Puzzle
from os import system, name
import time

# class Tree:
#     def __init__(self, content, left=None, right=None):
#         self.content = content
#         self.left = left
#         self.right = right
    
#     def get_children(self):
#         children = []
#         if self.left != None:
#             children.append(self.left)
#         if self.right != None:
#             children.append(self.right)
#         return children

# def dfs(src, target):
#     if src.content == target:
#         return True
#     for node in src.get_children():
#         if dfs(node, target) == True:
#             return True
#     return False

# tree = Tree(43)
# tree_left = Tree(69)
# tree_right = Tree(24)
# tree.left = tree_left
# tree23 = Tree(23)
# tree.right = tree_right
# # tree_left.left = tree23

# print(dfs(tree, 23))

def clear(command):
    system(command)

class IterativeDeepening:
    def __init__(self, puzzle, command="clear"):
        self.puzzle = puzzle
        self.command = command
        print(self.puzzle.state)

    def dfs(self, src, target, limit, state_list):
        # print("New state")
        # clear(self.command)
        # print(src.puzzle)
        if src.state == target:
            return True, src, list()
        if limit <= 0:
            return False, None, list()   
        # print(state_list)
        moves, move_names = src.get_moves()
        for move, move_name in zip(moves, move_names):
            if move.state not in state_list:
                state_list.append(move.state)
                isFinal, source, move_list = self.dfs(move, target, limit - 1, state_list)
                if isFinal == True:
                    move_list.append(Puzzle.move_no_to_name(move_name))
                    return True, source, move_list
        return False, None, list()

    def idfs(self, max_depth=50):
        start_time = time.time()
        for i in range(max_depth):
            print("Limit =", i)
            state_list = []
            state_list.append(self.puzzle.state)
            isFinal, source, move_list = self.dfs(self.puzzle, self.puzzle.target_state, i, state_list)
            if isFinal == True:
                move_list.reverse()
                return i, source, move_list
            print("Ellapsed time = %s seconds" %(time.time() - start_time))
        return max_depth, None, move_list

if __name__ == "__main__":

    if name == "nt":
        command = "cls"
    else:
        command = "clear"
    
    puzzle = Puzzle(4)
    print(puzzle.puzzle)
    print("Target state is ", puzzle.target_state)
    id = IterativeDeepening(puzzle, command)

    depth, source, move_list = id.idfs()
    print("Depth is", depth)
    if source != None:
        print(source.puzzle)
        print(move_list)
    else:
        print("No solution found")

