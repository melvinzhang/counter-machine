Counter Machine
===============

A k counter machine has k counters, each able to store a single natural number.
Initialy all counters are zero. For problems with inputs, some of the counters
are used to store the input.

The possible instructions are
1) increment counter i, jump to line n
2) decrement counter i, if successful jump to line n else jump to line m

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

Proved in minsky1967


Limitations of 2CM using standard encoding
------------------------------------------

A 2CM cannot recognize if counter 1 is prime.

A 2CM cannot recognize if counter 1 is of the form n^k for integer k >= 2.

Proved in ibarra1993
