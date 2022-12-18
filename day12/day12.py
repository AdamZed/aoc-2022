from copy import copy
from curses import can_change_color

DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

class Solution:

    def __init__(self, fname):
        self.data = self.parse_file(fname)
        for x, r in enumerate(self.data):
            for y, ch in enumerate(r):
                if ch == 'S': self.S = (x, y)
        self.MX = len(self.data)
        self.MY = len(self.data[0])

        print(f'Part 1: {self.part1()}')
        print(f'Part 2: {self.part2()}')

    def parse_file(self, fname):
        with open(fname) as f:
            return f.read().strip().split('\n')
            
    def can_step(self, x1, y1, x2, y2):
        if x2 < 0 or x2 >= self.MX: return False
        if y2 < 0 or y2 >= self.MY: return False
        
        c1, c2 = self.data[x1][y1], self.data[x2][y2]
        if c1 == 'S' and c2 == 'a': return True
        if c2 == 'E' and c1 == 'z': return True
        return ord(self.data[x2][y2]) - ord(self.data[x1][y1]) <= 1

    def part1(self):
        q = [[self.S]]
        seen = set()
        while q:
            path = q.pop(0)
            x, y = path[-1]
            if (x, y) in seen: continue
            seen.add((x, y))
            for (dx, dy) in DIRS:
                nx, ny = x+dx, y+dy
                if (nx, ny) in path: continue
                if self.can_step(x, y, nx, ny):
                    if self.data[nx][ny] == 'E': return len(path)
                    _path = copy(path)
                    _path.append((nx, ny))
                    q.append(_path)
                
    def part2(self):
        q = [[self.S]] + \
            [[(x, y)] for x in range(self.MX) for y in range(self.MY) if self.data[x][y] == 'a']
        seen = set()
        while q:
            path = q.pop(0)
            x, y = path[-1]
            if (x, y) in seen: continue
            seen.add((x, y))
            for (dx, dy) in DIRS:
                nx, ny = x+dx, y+dy
                if (nx, ny) in path: continue
                if self.can_step(x, y, nx, ny):
                    if self.data[nx][ny] == 'E': return len(path)
                    _path = copy(path)
                    _path.append((nx, ny))
                    q.append(_path)

if __name__ == "__main__":
    import sys
    filename = 'input.txt' if len(sys.argv) <= 1 else sys.argv[1] 
    Solution(filename)