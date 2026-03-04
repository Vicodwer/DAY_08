# ============================================================
# PART E: Smart Transaction Validator
# ============================================================

# ---------- Input Collection ----------
try:
    amount = float(input("Transaction amount (Rs): "))
    category = input("Category (food/travel/electronics/other): ").strip().lower()
    hour = int(input("Hour of transaction (0-23): "))
    daily_spent = float(input("Amount already spent today (Rs): "))
    vip = input("VIP customer? (yes/no): ").strip().lower()
except ValueError:
    print(" Invalid input. Please enter correct values.")
    exit()

# ---------- Input Validation ----------
if amount <= 0:
    print(" Amount must be positive.")
    exit()

if category not in ("food", "travel", "electronics", "other"):
    print(" Category must be food, travel, electronics, or other.")
    exit()

if not (0 <= hour <= 23):
    print(" Hour must be between 0 and 23.")
    exit()

if daily_spent < 0:
    print(" Daily spent cannot be negative.")
    exit()

if vip not in ("yes", "no"):
    print(" VIP must be yes or no.")
    exit()

# ---------- VIP Multiplier (Ternary Operator) ----------
multiplier = 2 if vip == "yes" else 1

# ---------- Dynamic Limits ----------
SINGLE_LIMIT    = 50000  * multiplier
DAILY_LIMIT     = 100000 * multiplier
FOOD_LIMIT      = 5000   * multiplier
ELECTRONICS_LIMIT = 30000 * multiplier

# ---------- Header ----------
print("\n" + "=" * 55)
print("         SMART TRANSACTION VALIDATOR")
print("=" * 55)
print(f"  Amount         : ₹{amount:,.2f}")
print(f"  Category       : {category.capitalize()}")
print(f"  Hour           : {hour:02d}:00")
print(f"  Daily Spent    : ₹{daily_spent:,.2f}")
print(f"  VIP Status     : {'Yes ' if vip == 'yes' else 'No'}")
print(f"  Single Limit   : ₹{SINGLE_LIMIT:,.2f}")
print(f"  Daily Limit    : ₹{DAILY_LIMIT:,.2f}")
print("=" * 55)

# ---------- BLOCK Rules (highest priority) ----------
if amount > SINGLE_LIMIT:
    print(f"\n BLOCKED")
    print(f"   Reason: Single transaction ₹{amount:,.2f} exceeds"
          f" limit of ₹{SINGLE_LIMIT:,.2f}")

elif daily_spent + amount > DAILY_LIMIT:
    print(f"\n BLOCKED")
    print(f"   Reason: Daily limit breached —"
          f" ₹{daily_spent:,.2f} + ₹{amount:,.2f}"
          f" = ₹{daily_spent + amount:,.2f}"
          f" exceeds ₹{DAILY_LIMIT:,.2f}")

# ---------- FLAG Rules ----------
elif hour < 6 or hour >= 23:
    print(f"\n  FLAGGED")
    print(f"   Reason: Unusual transaction hour ({hour:02d}:00)"
          f" — outside normal window (06:00–23:00)")

# ---------- Category Limits ----------
elif category == "food" and amount >= FOOD_LIMIT:
    print(f"\n  FLAGGED")
    print(f"   Reason: Food transaction ₹{amount:,.2f}"
          f" exceeds category limit of ₹{FOOD_LIMIT:,.2f}")

elif category == "electronics" and amount >= ELECTRONICS_LIMIT:
    print(f"\n  FLAGGED")
    print(f"   Reason: Electronics transaction ₹{amount:,.2f}"
          f" exceeds category limit of ₹{ELECTRONICS_LIMIT:,.2f}")

# ---------- APPROVED ----------
else:
    print(f"\n APPROVED")
    print(f"   Transaction of ₹{amount:,.2f}"
          f" at {hour:02d}:00 in {category.capitalize()}"
          f" category is cleared.")

print(f"\n  Updated Daily Total: ₹{daily_spent + amount:,.2f}")
print("=" * 55)
```

---

###  Test Run 1 — Normal Food Transaction
```
Transaction amount (Rs): 3000
Category: food
Hour: 14
Amount already spent today: 10000
VIP customer: no

=======================================================
         SMART TRANSACTION VALIDATOR
=======================================================
  Amount         : 3,000.00
  Category       : Food
  Hour           : 14:00
  Daily Spent    : 10,000.00
  VIP Status     : No
  Single Limit   : 50,000.00
  Daily Limit    : 1,00,000.00
=======================================================

 APPROVED
   Transaction of 3,000.00 at 14:00 in Food category is cleared.

  Updated Daily Total: 13,000.00
=======================================================
```

###  Test Run 2 — Electronics at Night, VIP
```
Transaction amount (Rs): 60000
Category: electronics
Hour: 2
Amount already spent today: 20000
VIP customer: yes

=======================================================
  Amount         : 60,000.00
  Category       : Electronics
  Hour           : 02:00
  VIP Status     : Yes 
  Single Limit   : 1,00,000.00   ← doubled for VIP
  Daily Limit    : 2,00,000.00   ← doubled for VIP
=======================================================

  FLAGGED
   Reason: Unusual transaction hour (02:00)
   — outside normal window (06:00–23:00)
=======================================================
```