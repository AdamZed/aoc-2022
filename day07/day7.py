class Node:
    def __init__(self, name, par, size):
        self.name = name
        self.par = par
        self.size = size
        self.children = {} if size == 'dir' else None
    
    def calc_size(self):
        if self.size != 'dir': return int(self.size)
        self.dir_size = sum(child.calc_size() for child in self.children.values())
        return self.dir_size

SMALL_DIR_SZ = 100000
MAX_SPACE    = 70000000
SPACE_NEEDED = 30000000
class Solution:

    def __init__(self, fname):
        self.data = self.parse_file(fname)
        self.build_tree()
        self.root.calc_size()

        print(f'Part 1: {self.part1()}')
        print(f'Part 2: {self.part2()}')

    def build_tree(self):
        self.root = Node("/", None, 'dir')
        curr_dir = self.root
        reading_ls = False
        for output in self.data:
            if reading_ls: 
                if output.startswith("$"): reading_ls == False
                else:
                    size, name = output.split()
                    curr_dir.children[name] = Node(name, curr_dir, size)
                    
            if output.startswith("$"):
                args = output.split()[1:]
                if args[0] == 'ls': reading_ls = True
                elif args[0] == 'cd':
                    name = args[1]
                    if   name == "..": curr_dir = curr_dir.par
                    elif name == "/":  curr_dir = self.root
                    else: curr_dir = curr_dir.children[name]
        
    def parse_file(self, fname):
        with open(fname) as f:
            return f.read().strip().split('\n')
            
    def part1(self):
        ans = 0
        def dfs(node):
            nonlocal ans
            if node.size != 'dir': return
            if node.dir_size <= SMALL_DIR_SZ: ans += node.dir_size
            for child in node.children.values(): dfs(child)
        dfs(self.root)
        return ans

    def part2(self):
        min_delete_sz = self.root.dir_size - (MAX_SPACE - SPACE_NEEDED)
        ans = float('inf')
        def dfs(node):
            nonlocal ans
            if node.size != 'dir' or node.dir_size < min_delete_sz: return
            ans = min(ans, node.dir_size)
            for child in node.children.values(): dfs(child)
        dfs(self.root)
        return ans

if __name__ == "__main__":
    import sys
    filename = 'input.txt' if len(sys.argv) <= 1 else sys.argv[1] 
    Solution(filename)