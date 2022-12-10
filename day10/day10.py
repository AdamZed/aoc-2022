SCREEN_WID = 40
MAX_CYCLE = 240
class Solution:
    def __init__(self, fname):
        self.data = self.parse_file(fname)
        
        print(f'Part 1: {self.part1()}')
        print(f'Part 2: {self.part2()}')

    def parse_file(self, fname):
        with open(fname) as f:
            return f.read().strip().split('\n')
            
    def part1(self):
        TARGETS = [i*40 + 20 for i in range(6)]
        MAX_CYC = 220
        signal_sum = 0
        reg_X = 1
        commands = iter(self.data)
        curr_cmd = next(commands)
        ded_cycle = curr_cmd != 'noop'

        for n in range(1, MAX_CYC + 1):
            if n in TARGETS: signal_sum += reg_X * n
            if ded_cycle:
                ded_cycle = False
                continue
            if curr_cmd != 'noop':
                reg_X += int(curr_cmd.split()[1])
            curr_cmd = next(commands)
            ded_cycle = curr_cmd != 'noop'
        return signal_sum

    def part2(self):
        reg_X = 1
        cycle = 0
        visible_pixels = set()
        commands = iter(self.data)
        curr_cmd = next(commands)
        ded_cycle = curr_cmd != 'noop'
        while True:
            if cycle % 40 in [reg_X-1, reg_X, reg_X+1]: visible_pixels.add(cycle)
            cycle += 1
            if ded_cycle:
                ded_cycle = False
                continue
            if curr_cmd != 'noop': reg_X += int(curr_cmd.split()[1])

            try: curr_cmd = next(commands)
            except StopIteration: break

            ded_cycle = curr_cmd != 'noop'

        return self.get_render(visible_pixels)

    def get_render(self, pixels):
        render = '\n'
        cycle = 0
        for _ in range(MAX_CYCLE//SCREEN_WID):
            for _ in range(SCREEN_WID):
                render += '#' if cycle in pixels else ' '
                cycle += 1
            render += '\n'
        return render


if __name__ == "__main__":
    import sys
    filename = 'input.txt' if len(sys.argv) <= 1 else sys.argv[1] 
    Solution(filename)