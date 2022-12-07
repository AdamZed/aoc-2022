class Solution:

    def __init__(self, fname):
        self.data = self.parse_file(fname)
        
        print(f'Part 1: {self.part1()}')
        print(f'Part 2: {self.part2()}')

    def parse_file(self, fname):
        with open(fname) as f:
            return f.read().strip()
            
    def solve(self, window_len):
        for i in range(window_len, len(self.data)):
            if len(set(self.data[i-window_len:i])) == window_len:
                return i

    def part1(self):
        return self.solve(4)

    def part2(self):
        return self.solve(14)


if __name__ == "__main__":
    import sys
    filename = 'input.txt' if len(sys.argv) <= 1 else sys.argv[1] 
    Solution(filename)