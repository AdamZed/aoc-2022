from functools import reduce
from operator import mul

class Solution:

    def __init__(self, fname):
        self.data = self.parse_file(fname)
        
        print(f'Part 1: {self.part1()}')
        print(f'Part 2: {self.part2()}')

    def parse_file(self, fname):
        with open(fname) as f:
            return [[[int(x), False] for x in line] for line in f.read().strip().split('\n')]
            
    def part1(self):
        def check_tree(tree, max_seen):
            h, _ = tree
            if h > max_seen:
                max_seen = h
                tree[1] = True
            return max_seen

        sz = len(self.data)
        for x in range(sz):
            max_seen_L, max_seen_R = -1, -1
            for y in range(sz):
                max_seen_L = check_tree(self.data[x][y], max_seen_L)
                max_seen_R = check_tree(self.data[x][sz-y-1], max_seen_R)
        for y in range(sz):
            max_seen_T, max_seen_B = -1, -1
            for x in range(sz):
                max_seen_T = check_tree(self.data[x][y], max_seen_T)
                max_seen_B = check_tree(self.data[sz-x-1][y], max_seen_B)

        return sum(1 for row in self.data for tree in row if tree[1])

    def part2(self):
        sz = len(self.data)
        def check_dir(x, y, h, dir):
            if x >= sz or y >= sz or x < 0 or y < 0: return 0
            tree_h = self.data[x][y][0]
            if tree_h >= h: return 1
            return 1 + check_dir(x+dir[0], y+dir[1], h, dir)
        
        DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        ans = 0
        for x in range(sz):
            for y in range(sz):
                score = reduce(mul, (check_dir(x+dir[0], y+dir[1], self.data[x][y][0], dir) for dir in DIRS))
                ans = max(ans, score)
        return ans


if __name__ == "__main__":
    import sys
    filename = 'input.txt' if len(sys.argv) <= 1 else sys.argv[1] 
    Solution(filename)