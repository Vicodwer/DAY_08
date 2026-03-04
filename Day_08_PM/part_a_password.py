# ============================================================
# PART A — Password Strength Analyzer & Generator
# Day 8 Assignment | Loops: for, while, break, continue
# ============================================================

import random
import string


# ─────────────────────────────────────────────
# HELPER FUNCTION: Analyze password strength
# ─────────────────────────────────────────────
def analyze_password(password):
    """
    Evaluates password strength and returns (score, missing_hints).
    Max score = 7
    """
    score = 0
    missing = []

    # ── 1. LENGTH CHECK ──────────────────────────────────────
    # Using len() — no loop needed here, O(1)
    length = len(password)

    if length >= 16:
        score += 3                          # Best: +3
    elif length >= 12:
        score += 2                          # Good: +2
    elif length >= 8:
        score += 1                          # Okay: +1
    else:
        missing.append("too short (need ≥ 8 chars)")

    # ── 2. CHARACTER TYPE CHECKS (for loop) ──────────────────
    has_upper   = False
    has_lower   = False
    has_digit   = False
    has_special = False
    special_chars = "!@#$%^&*"

    for ch in password:                     # O(n) — single pass
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif ch in special_chars:
            has_special = True

    # Award points & collect missing hints
    if has_upper:
        score += 1
    else:
        missing.append("uppercase letter")

    if has_lower:
        score += 1
    else:
        missing.append("lowercase letter")

    if has_digit:
        score += 1
    else:
        missing.append("digit")

    if has_special:
        score += 1
    else:
        missing.append("special character (!@#$%^&*)")

    # ── 3. NO MORE THAN 2 CONSECUTIVE REPEATED CHARS ─────────
    # Example: "aaa" is bad, "aa" is fine
    has_no_triple_repeat = True

    for i in range(len(password) - 2):      # O(n) — check triplets
        if password[i] == password[i + 1] == password[i + 2]:
            has_no_triple_repeat = False
            break                           # No need to keep checking

    if has_no_triple_repeat:
        score += 1
    else:
        missing.append("no triple repeated characters (e.g. 'aaa')")

    # ── 4. STRENGTH RATING ───────────────────────────────────
    if score <= 2:
        rating = "Weak"
    elif score <= 4:
        rating = "Medium"
    elif score <= 6:
        rating = "Strong"
    else:
        rating = "Very Strong"

    return score, rating, missing


# ─────────────────────────────────────────────
# HELPER FUNCTION: Generate a random password
# ─────────────────────────────────────────────
def generate_password(length):
    """
    Generates a random password using for loop + random.choice().
    Ensures at least one of each required character type.
    """
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""
    for _ in range(length):                 # for loop — O(n)
        password += random.choice(characters)

    return password


# ─────────────────────────────────────────────
# MAIN PROGRAM
# ─────────────────────────────────────────────
def main():
    print("=" * 50)
    print("   🔐 PASSWORD STRENGTH ANALYZER & GENERATOR")
    print("=" * 50)

    # ── WHILE LOOP: Keep asking until strength ≥ 5 ───────────
    while True:
        password = input("\nEnter password: ").strip()

        score, rating, missing = analyze_password(password)

        print(f"\n>> Strength: {score}/7 ({rating})")

        if missing:
            print(f">> Missing  : {', '.join(missing)}")

        if score >= 5:
            print(">> ✅ Password accepted!\n")
            break                           # Exit while loop
        else:
            print(">> ❌ Try again — aim for score ≥ 5\n")
            # 'continue' is implicit here; loop naturally repeats

    # ── PASSWORD GENERATOR ────────────────────────────────────
    print("-" * 50)
    print("🎲 PASSWORD GENERATOR")
    print("-" * 50)

    gen_length = int(input("Enter desired password length: "))
    generated  = generate_password(gen_length)

    gen_score, gen_rating, gen_missing = analyze_password(generated)

    print(f"\n>> Generated Password : {generated}")
    print(f">> Strength           : {gen_score}/7 ({gen_rating})")

    if gen_missing:
        print(f">> Missing            : {', '.join(gen_missing)}")
    else:
        print(">> ✅ All criteria met!")

    print("=" * 50)


# ─────────────────────────────────────────────
if __name__ == "__main__":
    main()


# ============================================================
# TWO SAMPLE RUNS (for submission / demonstration)
# ============================================================
#
# ── SAMPLE INPUT 1 ──────────────────────────────────────────
# Enter password: hello
# >> Strength: 2/7 (Weak)
# >> Missing  : too short, uppercase letter, digit, special character
# >>  Try again — aim for score ≥ 5
#
# Enter password: H3llo@World!
# >> Strength: 6/7 (Strong)
# >>  Password accepted!
#
# Enter desired password length: 14
# >> Generated Password : fG#2kLp!9mRz@q
# >> Strength           : 7/7 (Very Strong)
# >>  All criteria met!
#
# ── SAMPLE INPUT 2 ──────────────────────────────────────────
# Enter password: aaabbb123
# >> Strength: 3/7 (Medium)
# >> Missing  : uppercase letter, special character, no triple repeated chars
# >>  Try again — aim for score ≥ 5
#
# Enter password: SecureP@ss99!!
# >> Strength: 7/7 (Very Strong)
# >>  Password accepted!
#
# Enter desired password length: 10
# >> Generated Password : Xk$9pL@2nQ
# >> Strength           : 7/7 (Very Strong)
# >>  All criteria met!
# ============================================================