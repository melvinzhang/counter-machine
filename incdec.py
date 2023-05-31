from collections import defaultdict

# inc is a integer indicating which register to increment
# dec is a pair of (register, lines to jump backwards)
# a program is a list of inc and dec instructions

def run(prog, init = 1):
    r = defaultdict(int)
    r[1] = init
    pc = 0
    cnt = 0
    last_dec = {}
    while 0 <= pc < len(prog):
        cnt += 1
        instr = prog[pc]
        if isinstance(instr, int):
            r[instr] += 1
            pc += 1
        else:
            idx, jmp = instr
            if r[idx] > 0:
                if pc in last_dec and r[idx] >= last_dec[pc]:
                    return 0, -cnt
                last_dec[pc] = r[idx]
                r[idx] -= 1
                pc -= jmp
            else:
                last_dec.pop(pc, None)
                pc += 1
    return sum(r.values()), cnt

class Tracker:
    def __init__(self, init):
        self.init = init
        self.max_sum = 0
        self.max_term = 0

    def add(self, prog):
        out, cnt = run(prog, self.init)
        if out > self.max_sum:
            self.max_sum = out
            print(prog, self.max_sum, cnt)
        if cnt < 0 and -cnt > self.max_term:
            self.max_term = -cnt
            print("terminated", prog, self.max_term)
        return cnt >= 0

def gen_prog(nr, k, exe, acc = []):
    terminated = exe.add(acc)
    if len(acc) == k or not terminated:
        return
    # append inc, sequence of incs should be non-decreasing register idx
    lower = acc[-1] if acc and isinstance(acc[-1], int) else 1
    for i in range(lower,nr+1):
        acc.append(i)
        gen_prog(nr, k, exe, acc)
        acc.pop()
    # append dec
    for i in range(1,nr+1):
        for j in range(2,len(acc)+1):
            # do not allow inc i within dec i j
            if i in acc[-j:]:
                break
            # dest must be inc
            if not isinstance(acc[-j], int):
                continue
            acc.append( (i,j) )
            gen_prog(nr, k, exe, acc)
            acc.pop()

def search():
    gen_prog(3, 11, Tracker(0))

def main():
    prog = [2, 2, (3, 2), 3, 3, (2, 2), (1, 6)]
    for i in range(10):
        print(run(prog, init=i, max_cnt=10000000))

# (r=3,k=7,n=0) [1, 1, 1, 2, 2, 2, (1, 3)] sum=12 steps=19
# no difference for r=4

# computes 2^(2*(n+1)+1) - 2
# (r=3,k=7,n=1) [2, 2, (3, 2), 3, 3, (2, 2), (1, 6)] sum=30 steps=80
# no difference for r=4

# (r=3,k=8,n=0) [1, 2, 2, (3, 2), 3, 3, (2, 2), (1, 6)] sum=30 steps=81
# no difference for r=4

# (r=3,k=8,n=1) [1, 2, 2, (3, 2), 3, 3, (2, 2), (1, 6)] sum=126 steps=364
# no difference for r=4

# (r=3,k=9,n=0) at least 126 (proved 126 assuming jump at least 2, and dest must be inc)
# (r=3,k=10,n=0) at least 510 (proved 510 assuming jumnp at least 2 and dest must be inc)

# (r=3,k=11,n=0) [1, 1, 1, 2, 2, (3, 2), 3, 3, 3, (2, 3), (1, 7)] sum=2331 steps=5116

if __name__ == "__main__":
    search()
