# ============================================================
# PART B — Interview Ready
# Day 8 Assignment | Conceptual + Coding + Debug
# ============================================================


# ─────────────────────────────────────────────────────────────
# Q1 — CONCEPTUAL ANSWERS
# ─────────────────────────────────────────────────────────────

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Q1a) Difference between break and continue
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

► break   → EXITS the entire loop immediately.
            No more iterations happen after this point.

► continue → SKIPS the current iteration only.
             The loop moves on to the next iteration.

EXAMPLE:
"""

print("── break example ──")
for i in range(1, 6):
    if i == 3:
        break           # Stops the loop entirely when i = 3
    print(i)
# Output: 1  2
# 3, 4, 5 are never printed because loop exits at i=3

print("\n── continue example ──")
for i in range(1, 6):
    if i == 3:
        continue        # Skips i=3, but loop keeps going
    print(i)
# Output: 1  2  4  5
# Only 3 is skipped; rest continue normally

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Q1b) The else clause in for / while loops
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

► The else block runs ONLY IF the loop completed
  without hitting a break statement.

► If break was triggered → else does NOT run.
► If loop finishes normally → else RUNS.

PRACTICAL USE CASE — Search pattern:
  Use else to handle "item not found" gracefully
  without needing a found-flag variable.
"""

print("\n── loop-else: search pattern ──")
names = ["Alice", "Bob", "Charlie"]
target = "David"

for name in names:
    if name == target:
        print(f"Found: {name}")
        break
else:
    # This runs because we never hit 'break'
    print(f"'{target}' not found in list.")
# Output: 'David' not found in list.

# Compare with found = True target:
target2 = "Bob"
for name in names:
    if name == target2:
        print(f"Found: {name}")
        break           # break fires → else is SKIPPED
else:
    print(f"'{target2}' not found.")
# Output: Found: Bob   ← else block does NOT run


# ─────────────────────────────────────────────────────────────
# Q2 — CODING: find_pairs()
# ─────────────────────────────────────────────────────────────

# ── VERSION 1: O(n²) using nested loops ──────────────────────
def find_pairs_n2(numbers, target):
    """
    Returns all unique pairs (a, b) where a + b == target.
    Approach: nested loops → O(n²) time complexity.
    Outer loop picks each element; inner loop checks all elements after it.
    Using j = i+1 avoids duplicate pairs like (1,5) and (5,1).
    """
    pairs = []

    for i in range(len(numbers)):           # O(n) outer
        for j in range(i + 1, len(numbers)):  # O(n) inner → total O(n²)
            if numbers[i] + numbers[j] == target:
                pairs.append((numbers[i], numbers[j]))

    return pairs


# ── VERSION 2: O(n) using a set ──────────────────────────────
def find_pairs_n1(numbers, target):
    """
    Returns all unique pairs (a, b) where a + b == target.
    Approach: single pass with a set → O(n) time complexity.

    Logic:
      For each number x, we need (target - x).
      If (target - x) is already in our seen set → we found a pair!
      Otherwise, add x to seen and keep going.

    Why O(n)?
      Set lookup is O(1) average.
      We only iterate once → total O(n).
    """
    seen   = set()
    pairs  = []

    for x in numbers:                       # Single pass → O(n)
        complement = target - x

        if complement in seen:              # O(1) set lookup
            pairs.append((complement, x))

        seen.add(x)

    return pairs


# ── TEST BOTH VERSIONS ────────────────────────────────────────
print("\n── find_pairs tests ──")
nums   = [1, 2, 3, 4, 5]
target = 6

result_n2 = find_pairs_n2(nums, target)
result_n1 = find_pairs_n1(nums, target)

print(f"Input   : {nums}, target = {target}")
print(f"O(n²)   : {result_n2}")   # → [(1, 5), (2, 4)]
print(f"O(n)    : {result_n1}")   # → [(1, 5), (2, 4)]

# ── SAMPLE INPUT 2 ───────────────────────────────────────────
nums2   = [3, 7, 1, 9, 2, 8, 5]
target2 = 10

print(f"\nInput   : {nums2}, target = {target2}")
print(f"O(n²)   : {find_pairs_n2(nums2, target2)}")
print(f"O(n)    : {find_pairs_n1(nums2, target2)}")


# ─────────────────────────────────────────────────────────────
# Q3 — DEBUG & ANALYZE: is_prime()
# ─────────────────────────────────────────────────────────────

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ORIGINAL (BUGGY) CODE:

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, n):       # ← Bug here
            if n % i == 0:
                return False
        return True

BUGS IDENTIFIED:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

 BUG 1 — Performance Issue (not a logic bug, but O(n) when O(√n) is possible):
   range(2, n) checks ALL numbers from 2 up to n-1.
   This is unnecessary — if n has a factor greater than √n,
   it must also have a corresponding factor less than √n.
   So we only need to check up to √n.

   Fix: range(2, int(n**0.5) + 1)
   This makes it O(√n) instead of O(n).

 BUG 2 — Edge Case: n = 1
   Handled correctly (n < 2 returns False). 

 BUG 3 — Edge Case: n = 2 (smallest prime)
   With range(2, n) → range(2, 2) → empty range → returns True. 
   Still works, but only by coincidence of empty range behavior.
   The fix with int(n**0.5)+1 also handles this correctly.

SUMMARY TABLE:
   Input | Original | Fixed
   ------+----------+------
     1   |  False   | False  
     2   |  True    | True   
     3   |  True    | True   
    17   |  True    | True   
    18   |  False   | False 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

# ── FIXED VERSION ─────────────────────────────────────────────
def is_prime(n):
    """
    Checks if n is prime.
    Optimized: only checks divisors up to √n → O(√n) time.
    """
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):  #  Fixed: √n limit
        if n % i == 0:
            return False

    return True


# ── TEST is_prime ─────────────────────────────────────────────
print("\n── is_prime tests ──")
test_cases = [1, 2, 3, 4, 17, 18, 97, 100]
for num in test_cases:
    print(f"  is_prime({num:3}) → {is_prime(num)}")