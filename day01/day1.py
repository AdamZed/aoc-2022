class Solution:

    def __init__(self, fname):
        self.data = self.parse_file(fname)
        
        print(f'Part 1: {self.part1()}')
        print(f'Part 2: {self.part2()}')

    def parse_file(self, fname):
        with open(fname) as f:
            return [[int(cal) for cal in elf.split('\n')] for elf in f.read().strip().split('\n\n')]
            
    def part1(self):
        return max(sum(elf) for elf in self.data)

    def part2(self):
        return sum(sorted([sum(elf) for elf in self.data])[-3:])

if __name__ == "__main__":
    import sys
    filename = 'input.txt' if len(sys.argv) <= 1 else sys.argv[1] 
    Solution(filename)