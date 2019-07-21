# Implemention of Petersen's algorithm for multipling two numbers using a 3 counter machine
# input is stored in counter A and counter B, third counter used as scratch memory
# output is stored in counter B

# Correctness verified by testing all tuples (i,j) where 0 <= i,j < 100

def odd(n):
    return n % 2 == 1

def even(n):
    return n % 2 == 0

def mult(A, B):
    # special case: A * 0 = 0
    if B == 0: return 0

    # flag in lowest bit
    A = 2 * A + 1

    # loop 1
    while B > 0:
        A = 2 * A
        if odd(B): A = A + 1
        A = 2 * A
        B = B // 2
    B = A
    A = A + 1
    # loop 2
    while even(B):
        A = 2 * A
        B = B // 4
    B = B - 1
    # loop 3
    while even(A):
        B = 8 * B
        A = A // 2
    A = A - 1
    # loop 4
    while even(A):
        A = A // 2
        B = B // 4
        if odd(A): A = A + B
        A = A // 2
        B = B // 2
    A = A - B
    B = A
    B = B // 2
    
    return B

for i in range(100):
    for j in range(100):
        print(i,j)
        k = mult(i,j)
        print(k)
        assert i * j == mult(i,j)

print("Correct")

