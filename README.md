Counter Machine
===============

A k counter machine has k counters, each able to store a single natural number.
Initialy all counters are zero. For problems with inputs, some of the counters
are used to store the input.

The possible instructions are
1) increment counter i, jump to line n
2) decrement counter i, if successful jump to line n else jump to line m
