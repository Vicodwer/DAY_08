# Day 08 — Python Conditionals Assignment

**Date:** 03/03/2026
**Topics:** `if / elif / else`, comparison & logical operators, nested if, ternary operator, `match-case`, input validation

---

## 📁 File Structure
```
Day-08/
├── part_a_admission.py
├── part_b_tax_calculator.py
├── part_c_interview.py
├── part_d_pan_validator.py
├── part_e_transaction_validator.py
└── README.md
```

---

## 📝 Part Summary

### Part A — Student Admission Decision System (40%)
Evaluates student eligibility based on:
- Category-wise entrance score cutoffs (General / OBC / SC-ST)
- Minimum GPA requirement (7.0)
- Auto-admit with scholarship if score ≥ 95
- Bonus points for recommendation letter (+5) and extracurricular score > 8 (+3)
- Outputs: ADMITTED / WAITLISTED / REJECTED with reasons

**Test Inputs:**
```
Input 1: score=72, gpa=8.5, recommendation=yes, category=general, extra=9 → ADMITTED (Regular)
Input 2: score=97, gpa=9.0, recommendation=no, category=obc, extra=6   → ADMITTED (Scholarship)
```

---

### Part B — Income Tax Calculator (30%)
Progressive tax calculator under New Regime FY 2024-25:
- Applies ₹75,000 standard deduction
- Slab-wise tax breakdown
- Shows effective tax rate and take-home income

**Test Inputs:**
```
Input 1: ₹12,00,000 → Tax: ₹68,750  | Effective Rate: 5.73%
Input 2: ₹20,00,000 → Tax: ₹2,67,500 | Effective Rate: 13.38%
```

---

### Part C — Interview Questions (20%)

| Question | Topic |
|----------|-------|
| Q1 | `elif` vs multiple `if` — conceptual difference with example |
| Q2 | `classify_triangle()` — Equilateral / Isosceles / Scalene / Invalid |
| Q3 | Debug & fix grade-assignment code using `elif` chain |

---

### Part D — AI-Augmented PAN Validator (10%)
- Prompt given to Claude AI
- AI-generated code pasted and critically evaluated
- Improved version with taxpayer type validation and edge case handling

**Test Inputs:**
```
Input 1: ABCPE1234F → ✅ Valid PAN — Taxpayer Type: Individual
Input 2: abc1234    → ❌ Invalid length: must be 10 characters
```

---

### Part E — Smart Transaction Validator (Bonus)
Rule-based fraud detection system:
- **BLOCK:** single transaction > ₹50,000 or daily limit > ₹1,00,000
- **FLAG:** unusual hours (before 6AM / after 11PM) or category limit breach
- **VIP mode:** doubles all limits using ternary operator

**Test Inputs:**
```
Input 1: ₹3000, food, 14:00, daily=₹10000, VIP=no       → ✅ APPROVED
Input 2: ₹60000, electronics, 02:00, daily=₹20000, VIP=yes → ⚠️ FLAGGED (unusual hour)
```

---

## 🧠 Key Concepts Used

- `if / elif / else` chains
- Comparison operators (`>=`, `<=`, `==`, `!=`)
- Logical operators (`and`, `or`, `not`)
- Ternary operator (`x if condition else y`)
- Input validation with `try / except`
- Functions with edge case handling

---

## 🚀 How to Run
```bash
# Run any part individually
python part_a_admission.py
python part_b_tax_calculator.py
python part_c_interview.py
python part_d_pan_validator.py
python part_e_transaction_validator.py
```

> Requires Python 3.10+
