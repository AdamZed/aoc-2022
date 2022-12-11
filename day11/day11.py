from functools import reduce
import re
from operator import mul, add

OPS = {"*": mul, "+": add}
class Monkey:
    
    def __init__(self, data):
        lines = data.split('\n')
        self.in_hand = [int(x) for x in lines[1][18:].split(', ')]
        self.operations = re.search(r'  Operation: new = old ([\+|\*]) (old|[0-9]{1,2})', lines[2]).groups()
        self.test = int(re.search(r'  Test: divisible by ([0-9]*)', lines[3]).group(1))
        self.ifs = {}
        self.ifs[True] = int(re.search(r'    If true: throw to monkey ([0-9])',  lines[4]).group(1))
        self.ifs[False] = int(re.search(r'    If false: throw to monkey ([0-9])', lines[5]).group(1))
        self.inspections = 0
        
    def run_round(self, monkeys):
        self.inspections += len(self.in_hand)
        for item in self.in_hand:
            op, mag = self.operations
            mag = item if mag == 'old' else int(mag)
            new = OPS[op](item, mag)//3
            pass_to = self.ifs[new % self.test == 0]
            monkeys[pass_to].in_hand.append(new)
        self.in_hand.clear()

    def run_round2(self, monkeys, modu):
        self.inspections += len(self.in_hand)
        for item in self.in_hand:
            op, mag = self.operations
            mag = item if mag == 'old' else int(mag)
            new = OPS[op](item, mag) % modu
            pass_to = self.ifs[new % self.test == 0]
            monkeys[pass_to].in_hand.append(new)
        self.in_hand.clear()

    def show_hands(self, name):
        print(f'Monkey {name}: {self.in_hand}')

class Solution:

    def __init__(self, fname):
        self.data = self.parse_file(fname)
        print(f'Part 1: {self.part1()}')
        self.data = self.parse_file(fname)
        print(f'Part 2: {self.part2()}')

    def parse_file(self, fname):
        with open(fname) as f:
            return [Monkey(x) for x in f.read().strip().split('\n\n')]
            
    def part1(self):
        for _ in range(20):
            for monkey in self.data:
                monkey.run_round(self.data)
        inspects = sorted([m.inspections for m in self.data])
        return inspects[-1] * inspects[-2]

    def part2(self):
        modu = reduce(mul, (m.test for m in self.data))
        for _ in range(10000):
            for monkey in self.data:
                monkey.run_round2(self.data, modu)
        inspects = sorted([m.inspections for m in self.data])
        return inspects[-1] * inspects[-2]


if __name__ == "__main__":
    import sys
    filename = 'input.txt' if len(sys.argv) <= 1 else sys.argv[1] 
    Solution(filename)