"""06-04-2022 Leetcode 51. N-Queens"""

# 1:1, 2:2, 3:0?, 4:2, 5:? I found one arangement that has no symetry, so 8? AND has a corner used
# Ok, so n is only up til 9, relatively small. Obviously combinations on
# a 9X9 board are fucking huge, but it narrows stupid quick too.
# Every placed queen eliminates a MASSIVE chunk of possibilities.
# The starting choice though is 81 possibilites, and placing a queen
# eliminates somewhere beteween 32 and 17 choices. Is simulating this with
# random choice possible? I mean... I could put the coordinates in a stack, then
# recursively call all possibilities in the stack. Its only 9 calls deep at worst
# and most terminate very early. The widest call is 81 in round 1, but it narrows soo
# stupid fast maybe its fine. Brute Force Baby. Try in VSC first and check timing.

# Strongly suspect its in powers of two depending on what sort of symetries in solution

import itertools


class Solution:
    def solveNQueens(self, n: int):  # -> List[List[str]]:
        grid = [["0" for _ in range(n)] for _ in range(n)]
        stck = set(itertools.product(range(n), range(n)))
        placed_queens = 0
        self.recurseQueens(grid, stck, placed_queens)
        return grid

    def recurseQueens(self, grid, stck, placed_queens):
        if not stck and placed_queens < len(grid):
            return 0, 0, 0  # no space for remaining queens

        for pos in stck:
            new_grid, new_stack, new_placed_queens = self.placeQueen(
                grid, stck, pos, placed_queens
            )
            if new_placed_queens == 0:
                stck.discard(pos)
                continue
            if new_placed_queens == len(grid):
                return new_grid  # just turn this into a return?
            self.recurseQueens(new_grid, new_stack, new_placed_queens)

    def placeQueen(self, grid, stck, pos, placed_queens):
        pos_x, pos_y = pos[1], pos[0]  # why not *pos ?
        n = len(grid)
        for x in range(n):
            grid[pos_y][x] = "."
            stck.discard((pos_y, x))
        for y in range(n):
            grid[y][pos_x] = "."
            stck.discard((y, pos_x))
        for diag in range(1, n):
            if pos_x + diag < n and pos_y + diag < n:
                grid[pos_y + diag][pos_x + diag] = "."
                stck.discard((pos_y + diag, pos_x + diag))
            if pos_x + diag < n and pos_y - diag >= 0:
                grid[pos_y - diag][pos_x + diag] = "."
                stck.discard((pos_y - diag, pos_x + diag))
            if pos_x - diag >= 0 and pos_y + diag < n:
                grid[pos_y + diag][pos_x - diag] = "."
                stck.discard((pos_y + diag, pos_x - diag))
            if pos_x - diag >= 0 and pos_y - diag >= 0:
                grid[pos_y - diag][pos_x - diag] = "."
                stck.discard((pos_y - diag, pos_x - diag))

        grid[pos_y][pos_x] = "Q"
        return grid, stck, placed_queens + 1


tested = Solution()
print(tested.solveNQueens(2))


# import itertools


# class Solution:
#     def solveNQueens(self, n: int):  # -> List[List[str]]:
#         grid = [["0" for _ in range(n)] for _ in range(n)]
#         stck = set(itertools.product(range(n), range(n)))
#         placed_queens = 0
#         self.recurseQueens(grid, stck, placed_queens)
#         return grid

#     def recurseQueens(self, grid, stck, placed_queens):
#         if not stck and placed_queens < len(grid):
#             return _, _, 0  # no space for remaining queens

#         for pos in stck:
#             grid, stck = self.placeQueen(grid, stck, pos)


#     def placeQueen(self, grid, stck, pos):
#         pos_x, pos_y = pos[1], pos[0]  # why not *pos ?
#         n = len(grid)
#         for x in range(n):
#             grid[pos_y][x] = "."
#             stck.discard((pos_y, x))
#         for y in range(n):
#             grid[y][pos_x] = "."
#             stck.discard((y, pos_x))
#         for diag in range(1, n):
#             if pos_x + diag < n and pos_y + diag < n:
#                 grid[pos_y + diag][pos_x + diag] = "."
#                 stck.discard((pos_x + diag, pos_y + diag))
#             if pos_x + diag < n and pos_y - diag >= 0:
#                 grid[pos_y - diag][pos_x + diag] = "."
#                 stck.discard((pos_x + diag, pos_y - diag))
#             if pos_x - diag >= 0 and pos_y + diag < n:
#                 grid[pos_y + diag][pos_x - diag] = "."
#                 stck.discard((pos_x - diag, pos_y + diag))
#             if pos_x - diag >= 0 and pos_y - diag >= 0:
#                 grid[pos_y - diag][pos_x - diag] = "."
#                 stck.discard((pos_x - diag, pos_y - diag))

#         grid[pos_y][pos_x] = "Q"
#         return grid, stck


# tested = Solution()
# print(tested.solveNQueens(5))
