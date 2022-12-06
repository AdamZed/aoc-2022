import re

class Solution:

    def __init__(self, fname):
        self.parse_file(fname)
        print(f'Part 1: {self.part1()}')
        self.parse_file(fname)
        print(f'Part 2: {self.part2()}')

    def parse_file(self, fname):
        with open(fname) as f:
            crates, moves = f.read().split('\n\n')
            self.moves = moves.strip().split('\n')

            n_crates = int(crates.strip()[-1])
            configs = crates.split('\n')[:-1][::-1]
            stacks = [list() for _ in range(n_crates)]
            for row in configs:
                for i in range(n_crates):
                    item = row[1 + i*4]
                    if item != ' ': stacks[i].append(item)
            self.stacks = stacks
    
    def do_work(self, work_method):
        for move in self.moves:
            n, frm, to = [int(x) for x in re.search(r'move ([0-9]{1,2}) from ([0-9]) to ([0-9])', move).groups()]
            work_method(self.stacks, n, frm, to)

        return ''.join(stk[-1] for stk in self.stacks)

    def part1(self):
        def work(stacks, n, frm, to):
            for _ in range(n): stacks[to-1].append(stacks[frm-1].pop())
        return self.do_work(work)

    def part2(self):
        def work(stacks, n, frm, to):
            lift = [stacks[frm-1].pop() for _ in range(n)]
            stacks[to-1].extend(lift[::-1])
        return self.do_work(work)

if __name__ == "__main__":
    import sys
    filename = 'input.txt' if len(sys.argv) <= 1 else sys.argv[1] 
    Solution(filename)