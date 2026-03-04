# ============================================================
# PART D — Daily Transaction Analyzer (Paytm Case Study)
# Day 8 Assignment | Bonus Challenge
# ============================================================

# ─────────────────────────────────────────────────────────────
# MAIN PROGRAM
# ─────────────────────────────────────────────────────────────

def main():
    print("=" * 55)
    print("    PAYTM MINI ANALYTICS DASHBOARD")
    print("=" * 55)
    print("Enter transactions one by one.")
    print("Type 'done' to finish and see summary.\n")

    # ── DATA STORAGE ──────────────────────────────────────────
    transactions = []       # List of dicts: {amount, type, category}
    total_credits = 0.0
    total_debits  = 0.0

    # ── VALID OPTIONS ─────────────────────────────────────────
    valid_types      = ["credit", "debit"]
    valid_categories = ["food", "travel", "bills", "shopping", "other"]

    # ─────────────────────────────────────────────────────────
    # TODO 1 & 2: While loop — keep taking transactions
    # ─────────────────────────────────────────────────────────
    while True:
        print("-" * 40)
        raw = input("Enter amount (or 'done' to finish): ").strip().lower()

        if raw == "done":
            break           # Exit loop cleanly

        # ── Validate amount ───────────────────────────────────
        try:
            amount = float(raw)
            if amount <= 0:
                print("  Amount must be positive. Try again.")
                continue    # Skip this iteration, ask again
        except ValueError:
            print("  Invalid amount. Enter a number or 'done'.")
            continue

        # ── Transaction type ──────────────────────────────────
        txn_type = input("Type (credit / debit): ").strip().lower()
        if txn_type not in valid_types:
            print("  Invalid type. Please enter 'credit' or 'debit'.")
            continue

        # ── Category (Bonus Enhancement) ──────────────────────
        print(f"Category options: {', '.join(valid_categories)}")
        category = input("Category: ").strip().lower()
        if category not in valid_categories:
            category = "other"              # Default to 'other'

        # ── TODO 3: Flag high-value transactions ──────────────
        high_value = amount > 10000
        if high_value:
            print(f" HIGH VALUE TRANSACTION FLAGGED: ₹{amount:,.2f}")

        # ── Store transaction ─────────────────────────────────
        transactions.append({
            "amount"    : amount,
            "type"      : txn_type,
            "category"  : category,
            "high_value": high_value
        })

        # ── Update totals ─────────────────────────────────────
        if txn_type == "credit":
            total_credits += amount
        else:
            total_debits += amount

        print(f" Recorded: ₹{amount:,.2f} ({txn_type} | {category})")

    # ─────────────────────────────────────────────────────────
    # Check if any transactions were entered
    # ─────────────────────────────────────────────────────────
    if not transactions:
        print("\nNo transactions entered. Goodbye!")
        return

    # ─────────────────────────────────────────────────────────
    # TODO 5: Bar chart of last 10 transactions (* per ₹1000)
    # Using a for loop
    # ─────────────────────────────────────────────────────────
    print("\n"  "=" * 55)
    print("    BAR CHART — LAST 10 TRANSACTIONS")
    print("   (Each ★ = ₹1,000)")
    print("=" * 55)

    last_10 = transactions[-10:]            # Slice last 10

    for i, txn in enumerate(last_10, start=1):   # enumerate gives index
        stars_count = int(txn["amount"] / 1000)
        bar         = ""

        # Nested for loop to build the bar (no string multiplication)
        for _ in range(stars_count):
            bar += ""

        # Label direction with arrow
        direction = "↑" if txn["type"] == "credit" else "↓"
        hv_flag   = " " if txn["high_value"] else ""

        print(f"  #{i:2} {direction} ₹{txn['amount']:>10,.2f} | {bar}{hv_flag}")

    # ─────────────────────────────────────────────────────────
    # TODO 4 & 6: Summary statistics
    # ─────────────────────────────────────────────────────────
    net_balance       = total_credits - total_debits
    txn_count         = len(transactions)
    all_amounts       = [t["amount"] for t in transactions]
    highest_txn       = max(all_amounts)
    average_amount    = sum(all_amounts) / txn_count

    print("\n" + "=" * 55)
    print("    TRANSACTION SUMMARY")
    print("=" * 55)
    print(f"  Total Transactions  : {txn_count}")
    print(f"  Total Credits       : ₹{total_credits:,.2f}")
    print(f"  Total Debits        : ₹{total_debits:,.2f}")
    print(f"  Net Balance         : ₹{net_balance:,.2f}  "
          f"{' Positive' if net_balance >= 0 else '  Negative'}")
    print(f"  Highest Transaction : ₹{highest_txn:,.2f}")
    print(f"  Average Amount      : ₹{average_amount:,.2f}")

    # ── BONUS: Category spending breakdown ────────────────────
    print("\n" + "=" * 55)
    print("     SPENDING BY CATEGORY")
    print("=" * 55)

    category_totals = {}                    # Dict for tracking

    for txn in transactions:
        cat    = txn["category"]
        amount = txn["amount"]

        if cat not in category_totals:
            category_totals[cat] = 0.0      # Initialize

        category_totals[cat] += amount      # Accumulate

    for cat, total in category_totals.items():
        pct = (total / sum(all_amounts)) * 100
        print(f"  {cat.capitalize():<10} : ₹{total:>10,.2f}  ({pct:.1f}%)")

    print("=" * 55)
    print("   Thank you for using Paytm Analytics! ")
    print("=" * 55)


# ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    main()


# ─────────────────────────────────────────────────────────────
# TWO SAMPLE RUNS
# ─────────────────────────────────────────────────────────────
"""
── SAMPLE INPUT 1 ──────────────────────────────────────────
Enter amount: 5000
Type: credit
Category: food
 Recorded: 5,000.00 (credit | food)

Enter amount: 12000
Type: debit
Category: travel
 HIGH VALUE TRANSACTION FLAGGED: 12,000.00
 Recorded: 12,000.00 (debit | travel)

Enter amount: 3000
Type: debit
Category: bills
 Recorded: 3,000.00 (debit | bills)

Enter amount: done

 BAR CHART — LAST 10 TRANSACTIONS (Each  = 1,000)
  # 1 ↑   5,000.00 | 
  # 2 ↓  12,000.00 | 
  # 3 ↓   3,000.00 | 

 TRANSACTION SUMMARY
  Total Transactions  : 3
  Total Credits       : 5,000.00
  Total Debits        : 15,000.00
  Net Balance         : -10,000.00    Negative
  Highest Transaction : 12,000.00
  Average Amount      : 6,666.67

  SPENDING BY CATEGORY
  Food       :   5,000.00  (25.0%)
  Travel     :  12,000.00  (60.0%)
  Bills      :   3,000.00  (15.0%)

── SAMPLE INPUT 2 ──────────────────────────────────────────
Enter amount: 25000
Type: credit
Category: other
 HIGH VALUE TRANSACTION FLAGGED: 25,000.00

Enter amount: 800
Type: debit
Category: food

Enter amount: 1500
Type: debit
Category: bills

Enter amount: done

 BAR CHART
  # 1 ↑  25,000.00 |  
  # 2 ↓     800.00 |
  # 3 ↓   1,500.00 | 

 SUMMARY
  Total Transactions  : 3
  Net Balance         : 22,700.00   Positive
  Highest Transaction : 25,000.00
  Average Amount      : 9,100.00
"""