Counter Machine
===============

A k counter machine has k counters, each able to store a single natural number.
Initialy all counters are zero. For problems with inputs, some of the counters
are used to store the input.

The possible instructions are
1) increment counter i, jump to line n
2) decrement counter i, if successful jump to line n else jump to line m

Also known as a [Minsky machine](https://esolangs.org/wiki/Minsky_machine)

Largest sum
-----------
Let s(m) be the largest sum of all counters after executing a program with m instructions.

s(m) >= m since we can construct a program with m increment instructions.

| m | s |
|---|---|
| 7 | 12 |
| 8 | 30 |
| 9 | 126 |
| 10 | 510 |
| 11 | 2331 |

See [incdec.py](incdec.py)

Largest function
----------------
Given a starting configuration with n in counter 1. Let f(n,m) be the largest sum of all
counters after executing a program with m instructions.

The following table lists lower bounds for some m. See [largest_sum.py](largest_sum.py) for the programs that achieves the lower bound.

| m | f |
|---|---|
| 3 | 2n |
| 4 | 3n |
| 7 | 2^n |
| 8 | 2^(2n) |
| 9 | 2^n 3^n |
| 10 | 3^(2n) |
| 11 | 2^(4n) |


Multiplication with 3CM
-----------------------

A 3CM with X in counter 1 and Y in counter 2 is able to compute X * Y in counter 2.

Proof: Two algorithms are given in [mult.py](mult.py), one from schroeppel1972 and the other from petersen2018


Squaring with 3CM
-----------------

A 3CM with X in counter 1 is able to compute X^2.

Proof: See [square.py](square.py) for the algorithm from schroeppel1972

More generally, minsky1967 proved that a 3CM can compute all partial recursive
function of one variable and recognize all computably enumerable sets.


2CM is Turing complete
----------------------

Turing machine 

= FSM with two stacks 

= FSM with four counters 

= FSM with two counters (by encoding the 4 counters as 2^A * 3^B * 5^C * 7^D)

Proved in minsky1967.


Limitations of 2CM using standard encoding
------------------------------------------

schroeppel1972 showed that given n in counter 1, 2CM cannot compute 2^n

The following are due to ibarra1993:
* A 2CM cannot recognize if counter 1 is prime
* A 2CM cannot recognize if counter 1 is of the form n^k for integer k >= 2


Decidable 2CM problems
----------------------
instruction set:
* inc c: reg[c] += 1; pc += 1
* dec c q: if reg[c] == 0 pc += 1 else reg[c] -= 1; pc = q

Decidable problems:
* halting for a 2CM where dec jumps to q if reg[c] == 0
* halting of reversible 2CM
* is there a uniform bound on number of reachable configurations
* is there a uniform bound on number of steps in any run

Uniform means from any starting configuration.

Proved in Certified Decision Procedures for Two-Counter Machines.
