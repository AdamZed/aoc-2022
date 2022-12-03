POINTS = {"A":1,"B":2,"C":3,"X":1,"Y":2,"Z":3}

class Solution:

    def __init__(self, fname):
        self.data = self.parse_file(fname)

        print(f'Part 1: {self.part1()}')
        print(f'Part 2: {self.part2()}')

    def parse_file(self, fname):
        with open(fname) as f:
            return [round.split(' ') for round in f.read().strip().split('\n')]
            
    def part1(self):
        return sum(self.outcome(round) for round in self.data)

    def outcome(self, round):
        a, b = round
        if POINTS[a] == POINTS[b]: return POINTS[b] + 3
        if POINTS[b] - POINTS[a] == 1 or POINTS[b] - POINTS[a] == -2: return POINTS[b] + 6
        return POINTS[b]

    def part2(self):
        return sum(self.outcome2(round) for round in self.data)

    def outcome2(self, round):
        shape, des = round
        if des == "Y": return 3 + POINTS[shape]
        if des == "X":
            pts = POINTS[shape] - 1 
            return pts if pts > 0 else 3
        pts = POINTS[shape] + 1 
        return (pts if pts <= 3 else 1) + 6
        

if __name__ == "__main__":
    import sys
    filename = 'input.txt' if len(sys.argv) <= 1 else sys.argv[1] 
    Solution(filename)