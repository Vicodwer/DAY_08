# ============================================================
# PART C — AI-Augmented Task: Diamond Pattern
# Day 8 Assignment
# ============================================================

# ─────────────────────────────────────────────────────────────
# EXACT PROMPT USED:
# ─────────────────────────────────────────────────────────────
"""
"Write a Python program that prints a diamond pattern of asterisks.
The user inputs the number of rows for the upper half.
Include proper spacing and use nested loops only
(no string multiplication tricks)."
"""

# ─────────────────────────────────────────────────────────────
# AI'S OUTPUT (Claude / ChatGPT response — reproduced as-is)
# ─────────────────────────────────────────────────────────────
"""
n = int(input("Enter number of rows for upper half: "))

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()

for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()
"""

# ─────────────────────────────────────────────────────────────
# CRITICAL EVALUATION OF AI OUTPUT
# ─────────────────────────────────────────────────────────────
"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. SPACING CORRECTNESS 
   The formula (n - i) spaces before each row is correct.
   Stars = (2i - 1) is the right formula for a diamond row.

2. READABILITY  (Needs Improvement)
   Variable names i, j, k are generic.
   No comments explaining the math/formulas.
   Hard for a beginner to understand why (2*i - 1) or (n - i).

3. EDGE CASES  (Not Handled)
   n = 0  → upper half loop range(1,1) → nothing printed. Silent fail.
   n = 1  → prints a single "*". Technically correct but no guard/message.
   Negative input → range becomes invalid, no error handling.

4. NESTED LOOPS vs STRING TRICKS 
   Correctly uses nested for loops as requested.
   No str * n usage anywhere — follows the constraint.

5. TIME COMPLEXITY
   Upper half: O(n²) — two nested loops per row, n rows.
   Lower half: O(n²) — same structure.
   Overall   : O(n²) — unavoidable for printing n² characters.

VERDICT: The AI code WORKS but lacks robustness, comments, and edge case handling.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

# ─────────────────────────────────────────────────────────────
# YOUR IMPROVED VERSION
# ─────────────────────────────────────────────────────────────

def print_diamond(n):
    """
    Prints a diamond pattern of '*' using nested loops only.
    n = number of rows in the upper half (including the middle row).

    Pattern for n=4:
       *          ← row 1: 3 spaces, 1 star
      ***         ← row 2: 2 spaces, 3 stars
     *****        ← row 3: 1 space,  5 stars
    *******       ← row 4: 0 spaces, 7 stars  (widest/middle)
     *****        ← mirror: back up
      ***
       *

    Formula:
      spaces = n - row_number
      stars  = 2 * row_number - 1
    """

    # ── Edge case guards ──────────────────────────────────────
    if n <= 0:
        print("Please enter a positive integer.")
        return
    if n == 1:
        print("*")
        return

    # ── Upper half (including middle row) ────────────────────
    # Outer loop: each row from 1 to n
    for row in range(1, n + 1):

        # Inner loop 1: print leading spaces
        for space in range(n - row):    # spaces decrease as row grows
            print(" ", end="")

        # Inner loop 2: print stars
        for star in range(2 * row - 1):  # stars = 1, 3, 5, 7...
            print("*", end="")

        print()                         # newline after each row

    # ── Lower half (mirror, skipping middle row) ─────────────
    # Outer loop: count back from n-1 down to 1
    for row in range(n - 1, 0, -1):

        # Inner loop 1: print leading spaces
        for space in range(n - row):
            print(" ", end="")

        # Inner loop 2: print stars
        for star in range(2 * row - 1):
            print("*", end="")

        print()                         # newline after each row


# ─────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────
def main():
    print("=" * 40)
    print("    DIAMOND PATTERN GENERATOR")
    print("=" * 40)

    n = int(input("Enter number of rows for upper half: "))
    print()
    print_diamond(n)
    print()


# ─────────────────────────────────────────────────────────────
# TWO SAMPLE RUNS
# ─────────────────────────────────────────────────────────────
"""
── SAMPLE INPUT 1: n = 4 ──────────────────────────
   *
  ***
 *****
*******
 *****
  ***
   *

── SAMPLE INPUT 2: n = 1 ──────────────────────────
*

── EDGE CASE: n = 0 ───────────────────────────────
Please enter a positive integer.
"""

if __name__ == "__main__":
    main()