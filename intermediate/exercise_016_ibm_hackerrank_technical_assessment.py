"""
IBM HackerRank Technical Assessment — Custom Problem
----------------------------------------------------

This problem was part of a technical interview for IBM delivered through HackerRank.
The task consists of computing the minimum number of steps required to reach a
given target position starting from position 0, following a dynamic step pattern.

Description
-----------
You start at position 0. On each iteration, you take a step whose size equals
the step number (first step = size 1, second = size 2, third = size 3, ...).

Movement rules:
- If moving forward by the current step size would go *beyond* the target
  position, you must move backward instead (subtract the step size).
- Otherwise, move forward.

You must determine the **minimum number of steps** needed to land **exactly**
on the target position.

Example walk
------------
Target = 7

Step 1: pos = 0 + 1 = 1
Step 2: pos = 1 + 2 = 3
Step 3: pos = 3 + 3 = 6
Step 4: pos + 4 would be 10 (overshoot), so move backward:
        pos = 6 - 4 = 2
Step 5: pos + 5 = 7 (valid, does not overshoot)
        pos = 7 --> reached target

Answer: 5 steps

Function Requirements
---------------------
Implement a function:

    def reach_target(target: int) -> int:
        
        ## Returns the **minimum number of steps** required to reach exactly the
        given target, following the movement rules described above.
        

Constraints (reconstructed)
---------------------------
- target is a non-negative integer
- You must finish exactly at 'target'
- Step sizes always increase by 1 each iteration

"""
def obtain_input() -> int:
	while True:
		try:
			n = int(input("\nPlease, enter a number an integer number to act as a position to reach: "))
			break
		except ValueError:
			print("Sorry, it seems that you didn't enter a number. Try again.")
	return n

def reach_target(target: int) -> int:
    steps = 0
    total = 0

    while total < target or (total - target) % 2 != 0:
        steps += 1
        total += steps

    return steps

if __name__ == "__main__":
	user_input = obtain_input()
	print(f"\n=> Minimum steps to reach position {user_input} = {reach_target(user_input)} steps.\n")
	

# Explanation:
# We look for the smallest n such that the triangular number S(n) = n(n+1)/2
# is at least the target and the difference S(n) - target is even.
# Why even? Because switching any step k from +k to -k changes the total by 2k,
# which allows adjusting the difference only in even increments.
# Thus, the first n where S(n) >= target and (S(n) - target) % 2 == 0
# guarantees that the target is reachable.
#
# Example: target = 4
# Steps: 1 + 2 + 3 = 6 (S(3) = 6, 6-4=2, which is even)
# So, 3 steps are enough.
#
# This approach is much more efficient than simulating every possible path.
# 
# We never actually need to simulate "going back" with "total -= steps" in the algorithm,
# because the parity adjustment ensures we can reach the exact target by flipping the sign
# of some steps if necessary.
# Therefore, it's enough to find the first n such that S(n) >= target and (S(n) - target) is even.
