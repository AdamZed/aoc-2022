class Solution:

    def __init__(self, fname):
        self.data = self.parse_file(fname)
        
        print(f'Part 1: {self.part1()}')
        print(f'Part 2: {self.part2()}')

    def parse_file(self, fname):
        with open(fname) as f:
            return [[*bin] for bin in f.read().strip().split('\n')]
            
    def part1(self):
        def inter(bin):
            hf1, hf2 = set(bin[:len(bin)//2]), set(bin[len(bin)//2:])
            return self.priority(hf1.intersection(hf2).pop())

        return sum(inter(bin) for bin in self.data)

    def part2(self):
        def inter(bins):
            bin1, bin2, bin3 = set(bins[0]), set(bins[1]), set(bins[2])
            return self.priority(bin1.intersection(bin2, bin3).pop())

        return sum([inter(self.data[i-3:i]) for i in range(3, len(self.data)+1, 3)])

    def priority(self, badge):
        return ord(badge.lower()) - 96 + (0 if ord(badge) > 96 else 26)
 
if __name__ == "__main__":
    import sys
    filename = 'input.txt' if len(sys.argv) <= 1 else sys.argv[1] 
    Solution(filename)