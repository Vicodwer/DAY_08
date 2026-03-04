"Write a Python program that validates an Indian PAN card number 
format using if-else conditions.
PAN format: 5 uppercase letters, 4 digits, 1 uppercase letter 
(e.g., ABCDE1234F).
The 4th character indicates the type of taxpayer."

# ============================================================
# PART D: AI-Generated Code
# ============================================================

def validate_pan(pan):
    if len(pan) != 10:
        return "Invalid PAN: must be 10 characters"
    
    for i in range(5):
        if not pan[i].isupper():
            return "Invalid PAN: first 5 must be uppercase letters"
    
    for i in range(5, 9):
        if not pan[i].isdigit():
            return "Invalid PAN: positions 6-9 must be digits"
    
    if not pan[9].isupper():
        return "Invalid PAN: last character must be uppercase letter"
    
    return "Valid PAN"

pan = input("Enter PAN number: ").strip()
print(validate_pan(pan))

"""
CRITICAL EVALUATION OF AI-GENERATED CODE:
==========================================

1. POSITIONS VALIDATED CORRECTLY?
   -  Length check (10 chars) — correct
   -  First 5 uppercase letters — correct
   -  Positions 6-9 digits — correct
   -  Last character uppercase — correct
   -  4th character taxpayer type NOT validated
     (P=Individual, C=Company, H=HUF, F=Firm etc.)
   -  5th character should be first letter of
     surname — not validated

2. EDGE CASES HANDLED?
   -  Lowercase input not handled (ABCDE1234f fails)
   -  Empty string not handled
   -  Special characters not checked
   -  Spaces inside PAN not caught

3. APPROACH: character-by-character vs regex?
   - Uses character-by-character  (matches assignment requirement)
   - But checks are slightly redundant — isupper()
     already implies isalpha(), not checked separately

4. IS THE CODE PYTHONIC?
   -  Using index-based for loops instead of slicing
   -  No use of all() which is more Pythonic
   -  Function returns string instead of bool + message
   -  Basic structure is clean and readable
"""

# ============================================================
# PART D: Improved PAN Validator (Your Version)
# ============================================================

# Valid 4th character taxpayer types
TAXPAYER_TYPES = {
    'P': 'Individual',
    'C': 'Company',
    'H': 'Hindu Undivided Family (HUF)',
    'F': 'Firm',
    'A': 'Association of Persons (AOP)',
    'T': 'Trust',
    'B': 'Body of Individuals (BOI)',
    'L': 'Local Authority',
    'J': 'Artificial Juridical Person',
    'G': 'Government'
}

def validate_pan(pan):
    # ---------- Edge Cases ----------
    if not pan:
        return False, " PAN cannot be empty"

    # Convert to uppercase to handle lowercase input
    pan = pan.strip().upper()

    # ---------- Length Check ----------
    if len(pan) != 10:
        return False, f" Invalid length: PAN must be 10 characters, got {len(pan)}"

    # ---------- First 3 characters: uppercase letters ----------
    if not pan[:3].isalpha() or not pan[:3].isupper():
        return False, " First 3 characters must be uppercase letters"

    # ---------- 4th character: taxpayer type ----------
    if pan[3] not in TAXPAYER_TYPES:
        return False, f" 4th character '{pan[3]}' is not a valid taxpayer type"

    # ---------- 5th character: uppercase letter ----------
    if not pan[4].isalpha() or not pan[4].isupper():
        return False, " 5th character must be an uppercase letter"

    # ---------- Characters 6-9: digits ----------
    if not pan[5:9].isdigit():
        return False, " Characters 6-9 must be digits"

    # ---------- 10th character: uppercase letter ----------
    if not pan[9].isalpha() or not pan[9].isupper():
        return False, " Last character must be an uppercase letter"

    # ---------- All checks passed ----------
    taxpayer = TAXPAYER_TYPES[pan[3]]
    return True, f" Valid PAN — Taxpayer Type: {taxpayer}"


# ---------- Input & Output ----------
print("=" * 50)
print("       PAN CARD VALIDATOR")
print("=" * 50)

pan_input = input("\nEnter PAN number: ").strip()
is_valid, message = validate_pan(pan_input)

print(f"\nPAN Entered : {pan_input.upper()}")
print(f"Result      : {message}")
print("=" * 50)
```

---

###  Test Run 1 — Valid PAN
```
Enter PAN number: ABCPE1234F

PAN Entered : ABCPE1234F
Result      :  Valid PAN — Taxpayer Type: Individual
```

###  Test Run 2 — Invalid PAN
```
Enter PAN number: abc1234

PAN Entered : ABC1234
Result      :  Invalid length: PAN must be 10 characters, got 7