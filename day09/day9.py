from math import copysign

class Pos:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y

BOX_SIZE = 20
DIRS = {"U": (1, 0), "D": (-1, 0), "L": (0, -1), "R": (0, 1)}
sgn = lambda x: 0 if x == 0 else copysign(1, x)

class Solution:
    def __init__(self, fname):
        self.data = self.parse_file(fname)
        
        print(f'Part 1: {self.part1()}')
        print(f'Part 2: {self.part2()}')

    def parse_file(self, fname):
        with open(fname) as f:
            moves = [move.split() for move in f.read().strip().split('\n')]
            return [(dir, int(step)) for dir, step in moves]

    def move_rope(self, rope_len):
        visited = set()
        ropes = [Pos() for _ in range(rope_len)]
        for dir, step in self.data:
            dx, dy = DIRS[dir]
            for _ in range(step):
                ropes[0].x += dx
                ropes[0].y += dy
                for r in range(1, len(ropes)):
                    if abs(ropes[r-1].x - ropes[r].x) > 1:
                        ropes[r].x += sgn(ropes[r-1].x - ropes[r].x)
                        if ropes[r-1].y != ropes[r].y: ropes[r].y += sgn(ropes[r-1].y - ropes[r].y)
                    elif abs(ropes[r-1].y - ropes[r].y) > 1:
                        ropes[r].y += sgn(ropes[r-1].y - ropes[r].y)
                        if ropes[r-1].x != ropes[r].x: ropes[r].x += sgn(ropes[r-1].x - ropes[r].x)
                visited.add((ropes[-1].x, ropes[-1].y))
        return len(visited)

    def part1(self):
        return self.move_rope(2)

    def part2(self):
        return self.move_rope(10)

    def print_rope(self, ropes):
        for x in range(BOX_SIZE, BOX_SIZE, -1):
            for y in range(BOX_SIZE, BOX_SIZE):
                for i, rope in enumerate(ropes):
                    if rope.x == x and rope.y == y:
                        print(i, end='')
                        break
                else: print('s' if x == 0 and y == 0 else '.', end='')
            print()
        print('===================')

    def print_visited(self, visited):
        for x in range(BOX_SIZE, -BOX_SIZE, -1):
            for y in range(-BOX_SIZE, BOX_SIZE):
                print('#' if (x,y) in visited else '.', end='')
            print()

if __name__ == "__main__":
    import sys
    filename = 'input.txt' if len(sys.argv) <= 1 else sys.argv[1] 
    Solution(filename)