class Solution:

    def __init__(self, fname):
        self.data = self.parse_file(fname)
        
        print(f'Part 1: {self.part1()}')
        print(f'Part 2: {self.part2()}')

    def parse_file(self, fname):
        with open(fname) as f:
            pairs = [x for x in f.read().strip().split('\n')]
            pair_assign = []
            for pair in pairs:
                assigns = pair.split(',')
                pair_assign.append([int(x) for p in assigns for x in p.split('-')])
            return pair_assign

    def part1(self):
        def full_overlap(pair):
            a, b, x, y = pair
            if a > x or (a == x and y-x > b-a):
                a, b, x, y = x, y, a, b
            return a <= x and b >= y

        return sum(1 for pair in self.data if full_overlap(pair))

    def part2(self):
        def overlap(pair):
            a, b, x, y = pair
            return b >= x if a < x else y >= a

        return sum(1 for pair in self.data if overlap(pair))


if __name__ == "__main__":
    import sys
    filename = 'input.txt' if len(sys.argv) <= 1 else sys.argv[1] 
    Solution(filename)
