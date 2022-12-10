class Pos:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y

DIRS = {"U": (1, 0), "D": (-1, 0), "L": (0, -1), "R": (0, 1)}

class Solution:
    def __init__(self, fname):
        self.data = self.parse_file(fname)
        
        print(f'Part 1: {self.part1()}')
        print(f'Part 2: {self.part2()}')

    def parse_file(self, fname):
        with open(fname) as f:
            lines = f.read().strip().split('\n')
            moves = []
            for move in lines:
                dir, step = (move.split())
                moves.append((dir, int(step)))
            return moves

    def part1(self):
        visited = set()
        t_pos, h_pos = Pos(), Pos()
        for dir, step in self.data:
            dx, dy = DIRS[dir]
            for _ in range(step):
                h_pos.x += dx
                h_pos.y += dy
                if abs(h_pos.x - t_pos.x) > 1:
                    t_pos.x += (h_pos.x - t_pos.x)/2
                    if h_pos.y != t_pos.y: t_pos.y += h_pos.y - t_pos.y
                elif abs(h_pos.y - t_pos.y) > 1:
                    t_pos.y += (h_pos.y - t_pos.y)/2
                    if h_pos.x != t_pos.x: t_pos.x += h_pos.x - t_pos.x
                visited.add((t_pos.x, t_pos.y))
        return len(visited)

    def part2(self):
        pass

if __name__ == "__main__":
    import sys
    filename = 'input.txt' if len(sys.argv) <= 1 else sys.argv[1] 
    Solution(filename)