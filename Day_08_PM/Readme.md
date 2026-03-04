# 📘 Day 8 — PM Assignment | Python Loops

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Due](https://img.shields.io/badge/Due-06--03--2026-orange)

---

## 🗂️ Folder Structure

```
Day_08_PM/
├── part_a_password.py        # Password Analyzer & Generator
├── part_b_interview.py       # Interview Q&A + Coding + Debug
├── part_c_diamond.py         # Diamond Pattern (AI Task)
├── part_d_transactions.py    # Paytm Transaction Analyzer (Bonus)
└── README.md                 # This file
```

---

## 📌 Topics Covered

| Topic | Used In |
|-------|---------|
| `for` loop (range, enumerate, string iteration) | All parts |
| `while` loop | Part A, Part D |
| `break` & `continue` | Part A, Part B, Part D |
| `loop-else` | Part B (Q1) |
| Nested loops | Part C, Part D |
| Time complexity O(n) vs O(n²) | Part B (Q2, Q3) |

---

## 🔐 Part A — Password Strength Analyzer & Generator

**File:** `part_a_password.py`

A cybersecurity-inspired program that evaluates password strength and generates secure passwords.

### Features
- Scores password from **0 to 7** based on:
  - Length (≥8 → +1, ≥12 → +2, ≥16 → +3)
  - Uppercase, Lowercase, Digit, Special character (+1 each)
  - No triple consecutive repeated characters (+1)
- `while` loop keeps asking until score ≥ 5
- `for` loop generates a random password of user-specified length

### Sample Run
```
Enter password: hello
>> Strength: 2/7 (Weak)
>> Missing  : too short, uppercase letter, digit, special character
>> ❌ Try again

Enter password: H3llo@World!
>> Strength: 6/7 (Strong)
>> ✅ Password accepted!
```

---

## 💼 Part B — Interview Ready

**File:** `part_b_interview.py`

### Q1 — Conceptual
- `break` vs `continue` with runnable examples
- `loop-else` clause — when it executes and practical search pattern use case

### Q2 — find_pairs()
Returns all pairs from a list that sum to a target value.

```python
find_pairs([1, 2, 3, 4, 5], 6)
→ [(1, 5), (2, 4)]
```

| Version | Approach | Time Complexity |
|---------|----------|----------------|
| V1 | Nested loops | O(n²) |
| V2 | Set lookup | O(n) |

### Q3 — Debug is_prime()
- **Bug identified:** `range(2, n)` checks all numbers up to `n` → O(n)
- **Fix:** `range(2, int(n**0.5) + 1)` → only checks up to √n → O(√n)

---

## 💎 Part C — AI-Augmented Task (Diamond Pattern)

**File:** `part_c_diamond.py`

### Prompt Used
> *"Write a Python program that prints a diamond pattern of asterisks. The user inputs the number of rows for the upper half. Include proper spacing and use nested loops only (no string multiplication tricks)."*

### AI Output Evaluation

| Criteria | Result |
|----------|--------|
| Spacing correctness | ✅ Correct formula `(n - i)` spaces |
| Readability | ⚠️ Generic variable names, no comments |
| Edge cases (n=0, n=1) | ❌ Not handled |
| Nested loops (no string tricks) | ✅ Followed correctly |
| Time complexity | O(n²) — unavoidable |

### Improved Version
- Added edge case guards for `n = 0` and `n = 1`
- Descriptive variable names (`row`, `space`, `star`)
- Inline comments explaining the math formula

### Sample Output (n = 4)
```
   *
  ***
 *****
*******
 *****
  ***
   *
```

---

## 💰 Part D — Paytm Transaction Analyzer (Bonus)

**File:** `part_d_transactions.py`

A mini analytics dashboard simulating Paytm's backend transaction tracking.

### Features
- `while` loop accepts transactions until user types `done`
- `continue` skips invalid inputs gracefully
- Flags transactions **> ₹10,000** as 🚨 High Value
- `for` loop with `enumerate` prints a bar chart (★ per ₹1,000)
- **Bonus:** Category tracking (food, travel, bills, shopping, other) with % breakdown

### Summary Output Includes
- Total credits & debits
- Net balance
- Highest & average transaction
- Spending breakdown by category

### Sample Run
```
Enter amount: 12000
Type: debit
Category: travel
🚨 HIGH VALUE TRANSACTION FLAGGED: ₹12,000.00

📊 BAR CHART — LAST 10 TRANSACTIONS
  # 1 ↑ ₹  5,000.00 | ★★★★★
  # 2 ↓ ₹ 12,000.00 | ★★★★★★★★★★★★ 🚨

📋 TRANSACTION SUMMARY
  Total Transactions  : 2
  Net Balance         : ₹-7,000.00  ⚠️ Negative
  Highest Transaction : ₹12,000.00
  Average Amount      : ₹8,500.00
```

---

## 🧠 Key Concepts Summary

```
while loop    → repeat until a condition is met (unknown iterations)
for loop      → iterate over a sequence (known iterations)
break         → exit the loop entirely
continue      → skip current iteration, resume next
loop-else     → runs only if loop completed without hitting break
O(n)          → one loop = linear time
O(n²)         → nested loops = quadratic time
O(√n)         → optimal for primality check
```

---
