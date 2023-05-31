from collections import defaultdict

# inc is a integer indicating which register to increment
# dec is a pair of (register, lines to jump backwards)
# a program is a list of inc and dec instructions

# 2n + 2
prog = [2, 2, (1, 2)]

def run(prog, init = 1, max_cnt = 500):
    r = defaultdict(int)
    r[1] = init
    pc = 0
    cnt = 0
    while 0 <= pc < len(prog) and cnt < max_cnt:
        cnt += 1
        instr = prog[pc]
        if isinstance(instr, int):
            r[instr] += 1
            pc += 1
        else:
            idx, jmp = instr
            if r[idx] > 0:
                r[idx] -= 1
                pc -= jmp
            else:
                pc += 1
    if cnt < max_cnt:
        return sum(r.values()), cnt
    else:
        return -1, -1

class Tracker:
    def __init__(self):
        self.init = 1
        self.max_sum = 0

    def add(self, prog):
        out, cnt = run(prog, self.init)
        if out > self.max_sum:
            self.max_sum = out
            print(prog, self.max_sum, cnt)
        return cnt >= 0

def gen_prog(nr, k, exe, acc = []):
    terminated = exe.add(acc)
    if len(acc) == k or not terminated:
        return
    # sequence of incs should be non-decreasing register idx
    lower = acc[-1] if acc and isinstance(acc[-1], int) else 1
    for i in range(lower,nr+1):
        acc.append(i)
        gen_prog(nr, k, exe, acc)
        acc.pop()
    for i in range(1,nr+1):
        for j in range(1,len(acc)+1):
            # do not allow inc i within dec i j
            if i in acc[-j:]:
                break
            acc.append( (i,j) )
            gen_prog(nr, k, exe, acc)
            acc.pop()

def search():
    gen_prog(3, 7, Tracker()) 

def main():
    prog = [2, 2, (3, 2), 3, 3, (2, 2), (1, 6)]
    for i in range(10):
        print(run(prog, init=i, max_cnt=10000000))

# (r=3,k=7,n=0) [1, 1, 1, 2, 2, 2, (1, 3)] sum=12 steps=19

# computes 2^(2*n+1) - 2
# (r=3,k=7,n=1) [2, 2, (3, 2), 3, 3, (2, 2), (1, 6)] sum=30 steps=80

# (r=3,k=8,n=0) [1, 2, 2, (3, 2), 3, 3, (2, 2), (1, 6)] sum=30 steps=81
# (r=3,k=8,n=1) [1, 2, 2, (3, 2), 3, 3, (2, 2), (1, 6)] sum=126 steps=364

if __name__ == "__main__":
    search()