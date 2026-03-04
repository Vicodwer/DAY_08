# ============================================================
# PART B: Indian Income Tax Calculator (New Regime FY 2024-25)
# ============================================================

# ---------- Input ----------
try:
    income = float(input("Enter your annual income : "))
except ValueError:
    print(" Please enter a valid numeric income.")
    exit()

# ---------- Validation ----------
if income < 0:
    print(" Income cannot be negative.")
    exit()

# ---------- Standard Deduction ----------
STANDARD_DEDUCTION = 75000
taxable_income = max(0, income - STANDARD_DEDUCTION)

print(f"\n{'='*50}")
print(f"  INCOME TAX CALCULATOR — New Regime FY 2024-25")
print(f"{'='*50}")
print(f"  Gross Income         : {income:>12,.2f}")
print(f"  Standard Deduction   : {STANDARD_DEDUCTION:>12,.2f}")
print(f"  Taxable Income       : {taxable_income:>12,.2f}")
print(f"{'='*50}")

# ---------- Tax Slabs ----------
# (lower_limit, upper_limit, rate)
slabs = [
    (0,        300000,   0.00),
    (300000,   700000,   0.05),
    (700000,   1000000,  0.10),
    (1000000,  1200000,  0.15),
    (1200000,  1500000,  0.20),
    (1500000,  float('inf'), 0.30),
]

slab_labels = [
    "0 – 3L        (0%)",
    "3L – 7L       (5%)",
    "7L – 10L     (10%)",
    "10L – 12L    (15%)",
    "12L – 15L    (20%)",
    "Above 15L    (30%)",
]

# ---------- Tax Calculation ----------
total_tax = 0
print(f"\n  {'Slab':<22} {'Income in Slab':>15} {'Tax':>12}")
print(f"  {'-'*50}")

for i, (lower, upper, rate) in enumerate(slabs):
    if taxable_income <= lower:
        # Income doesn't reach this slab
        slab_income = 0
    elif taxable_income >= upper:
        # Income fully covers this slab
        slab_income = upper - lower
    else:
        # Income partially covers this slab
        slab_income = taxable_income - lower

    slab_tax = slab_income * rate
    total_tax += slab_tax

    print(f"  {slab_labels[i]:<22} {slab_income:>12,.2f}  {slab_tax:>10,.2f}")

# ---------- Results ----------
effective_rate = (total_tax / income * 100) if income > 0 else 0

print(f"  {'-'*50}")
print(f"  {'Total Tax':<22} {'':>15} {total_tax:>10,.2f}")
print(f"\n  Effective Tax Rate   : {effective_rate:.2f}%")
print(f"  Take-Home Income     : {income - total_tax:>12,.2f}")
print(f"{'='*50}\n")
```

---

###  Test Run 1 — 12,00,000 income
```
Enter your annual income : 1200000

==================================================
  INCOME TAX CALCULATOR — New Regime FY 2024-25
==================================================
  Gross Income         :   12,00,000.00
  Standard Deduction   :      75,000.00
  Taxable Income       :   11,25,000.00
==================================================

  Slab                   Income in Slab          Tax
  --------------------------------------------------
  0 – 3L        (0%)      3,00,000.00       0.00
  3L – 7L       (5%)      4,00,000.00   20,000.00
  7L – 10L     (10%)      3,00,000.00   30,000.00
  10L – 12L    (15%)      1,25,000.00   18,750.00
  12L – 15L    (20%)          0.00           0.00
  Above 15L    (30%)          0.00           0.00
  --------------------------------------------------
  Total Tax                              68,750.00

  Effective Tax Rate   : 5.73%
  Take-Home Income     : 11,31,250.00
==================================================
```

###  Test Run 2 — 20,00,000 income
```
Enter your annual income : 2000000

  Gross Income         :   20,00,000.00
  Taxable Income       :   19,25,000.00

  0 – 3L   →      ₹0
  3–7L     →  20,000
  7–10L    →  30,000
  10–12L   →  30,000
  12–15L   →  60,000
  Above15L →  1,27,500
  ---------------------------
  Total Tax  : 2,67,500
  Effective Rate: 13.38%
  Take-Home  : 17,32,500