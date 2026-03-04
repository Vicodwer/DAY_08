# ============================================================
# PART C: Interview Ready
# ============================================================

# ------------------------------------------------------------
# Q1: Difference between elif and multiple if statements
# ------------------------------------------------------------

"""
EXPLANATION:
------------
Multiple IF statements:
- Each if is checked INDEPENDENTLY, one after another
- Even if a condition is True, Python still checks the rest
- Can result in MULTIPLE conditions being True and overwriting values

elif (else-if):
- Checks conditions in a CHAIN
- Once one condition is True, the rest are SKIPPED
- Only ONE branch executes

EXAMPLE WHERE THEY DIFFER:
---------------------------
Input: score = 85
"""

print("=" * 50)
print("Q1: elif vs multiple if")
print("=" * 50)

score = 85

# --- Using multiple if (BUGGY behavior) ---
print("\n--- Using multiple if ---")
if score >= 60:
    grade = 'D'
if score >= 70:
    grade = 'C'
if score >= 80:
    grade = 'B'
if score >= 90:
    grade = 'A'

print(f"Score: {score} → Grade: {grade}")
# Output: B
# Why: All conditions up to >=80 are True
# Each one OVERWRITES grade, last True one wins

# --- Using elif (CORRECT behavior) ---
print("\n--- Using elif ---")
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"Score: {score} → Grade: {grade}")
# Output: B
# Why: First True condition (>=80) executes, rest are SKIPPED

"""
SUMMARY TABLE:
--------------
Input        | Multiple IF  | elif
-------------|--------------|------
score = 85   | 'B'          | 'B'   ← same here accidentally
score = 65   | 'C'          | 'D'   ← DIFFERENT! (see below)
"""

print("\n--- Score = 65: multiple if vs elif ---")
score = 65

# Multiple if
if score >= 60:
    grade_multi = 'D'
if score >= 70:
    grade_multi = 'C'   # NOT triggered, so grade stays 'D'
if score >= 80:
    grade_multi = 'B'
if score >= 90:
    grade_multi = 'A'

# elif
if score >= 90:
    grade_elif = 'A'
elif score >= 80:
    grade_elif = 'B'
elif score >= 70:
    grade_elif = 'C'
elif score >= 60:
    grade_elif = 'D'
else:
    grade_elif = 'F'

print(f"Score: {score}")
print(f"Multiple if → Grade: {grade_multi}")  # D (correct here)
print(f"elif        → Grade: {grade_elif}")   # D

# The KEY difference — score = 75
print("\n--- Score = 75: WHERE THEY TRULY DIFFER ---")
score = 75

grade_multi = None
if score >= 60:
    grade_multi = 'D'    # ✅ True → grade = D
if score >= 70:
    grade_multi = 'C'    # ✅ True → grade OVERWRITTEN to C
if score >= 80:
    grade_multi = 'B'    # ❌ False
if score >= 90:
    grade_multi = 'A'    # ❌ False

if score >= 90:
    grade_elif = 'A'
elif score >= 80:
    grade_elif = 'B'
elif score >= 70:
    grade_elif = 'C'     # ✅ First True → STOPS here
elif score >= 60:
    grade_elif = 'D'     # Skipped
else:
    grade_elif = 'F'

print(f"Score       : {score}")
print(f"Multiple if : {grade_multi}")   # C ← overwrites D
print(f"elif        : {grade_elif}")    # C ← same but for right reason

# ------------------------------------------------------------
# Q2: classify_triangle function
# ------------------------------------------------------------

print("\n" + "=" * 50)
print("Q2: Triangle Classifier")
print("=" * 50)

def classify_triangle(a, b, c):
    # Edge case: zero or negative values
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid input: sides must be positive numbers"

    # Not a triangle: any side >= sum of other two
    if a >= b + c or b >= a + c or c >= a + b:
        return "Not a triangle"

    # Equilateral: all sides equal
    if a == b == c:
        return "Equilateral triangle"

    # Isosceles: exactly two sides equal
    elif a == b or b == c or a == c:
        return "Isosceles triangle"

    # Scalene: all sides different
    else:
        return "Scalene triangle"


# --- Test Cases ---
test_cases = [
    (5, 5, 5),      # Equilateral
    (5, 5, 8),      # Isosceles
    (3, 4, 5),      # Scalene
    (1, 2, 10),     # Not a triangle
    (0, 4, 5),      # Zero value
    (-1, 4, 5),     # Negative value
    (5, 5, 10),     # Edge: degenerate triangle
]

for a, b, c in test_cases:
    print(f"  classify_triangle({a}, {b}, {c}) → {classify_triangle(a, b, c)}")

    # ------------------------------------------------------------
# Q3: Debug and Fix the grade code
# ------------------------------------------------------------

print("\n" + "=" * 50)
print("Q3: Debug & Fix")
print("=" * 50)

"""
ORIGINAL BUGGY CODE:
--------------------
score = 85

if score >= 60:
    grade = 'D'
if score >= 70:
    grade = 'C'
if score >= 80:
    grade = 'B'
if score >= 90:
    grade = 'A'

print(grade)

BUG EXPLANATION:
----------------
1. All four conditions are checked INDEPENDENTLY
2. For score = 85:
   - score >= 60 → True → grade = 'D'
   - score >= 70 → True → grade = 'C'  (overwrites D)
   - score >= 80 → True → grade = 'B'  (overwrites C)
   - score >= 90 → False → grade stays 'B'
3. Final output: 'B' which looks correct BUT
   it only works by coincidence — the logic is wrong

WHAT IF score = 100?
   - All 4 conditions are True
   - grade gets overwritten 4 times
   - Final grade = 'A' (accidentally correct)

THE REAL PROBLEM:
   - Multiple conditions can be True simultaneously
   - Each overwrites the previous — unpredictable

CORRECT FIX: Use if-elif-else chain
"""

score = 85

# ✅ Fixed version
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"\nBuggy code output for score=85  : 'B' (accidentally correct)")
print(f"Fixed code output for score=85  : {grade}")

# Show where buggy code truly fails
score2 = 95
grade_bug = None
if score2 >= 60: grade_bug = 'D'
if score2 >= 70: grade_bug = 'C'
if score2 >= 80: grade_bug = 'B'
if score2 >= 90: grade_bug = 'A'

if score2 >= 90:     grade_fix = 'A'
elif score2 >= 80:   grade_fix = 'B'
elif score2 >= 70:   grade_fix = 'C'
elif score2 >= 60:   grade_fix = 'D'
else:                grade_fix = 'F'

print(f"\nFor score = 95:")
print(f"  Buggy output : '{grade_bug}'  ← went through all 4 ifs")
print(f"  Fixed output : '{grade_fix}'  ← stopped at first True")
```

---

### 🧪 Expected Output (both test runs)
```
# Test Run 1 — score = 85
Multiple if → C (overwrites)
elif        → C (correct reason)

# Test Run 2 — Triangle tests
classify_triangle(5, 5, 5)   → Equilateral triangle
classify_triangle(5, 5, 8)   → Isosceles triangle
classify_triangle(3, 4, 5)   → Scalene triangle
classify_triangle(1, 2, 10)  → Not a triangle
classify_triangle(0, 4, 5)   → Invalid input
classify_triangle(-1, 4, 5)  → Invalid input
classify_triangle(5, 5, 10)  → Not a triangle