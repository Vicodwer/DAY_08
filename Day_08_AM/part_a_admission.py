# ============================================================
# Student Admission Decision System (Function-Based Version)
# ============================================================

def get_inputs():
    """Collect user inputs safely."""
    try:
        entrance_score = float(input("Enter entrance score (0-100): "))
        gpa = float(input("Enter GPA (0-10): "))
        has_recommendation = input("Do you have a recommendation letter? (yes/no): ").strip().lower()
        category = input("Enter category (general/obc/sc_st): ").strip().lower()
        extracurricular_score = float(input("Enter extracurricular score (0-10): "))
    except ValueError:
        print("Invalid input. Please enter numeric values where required.")
        return None
    
    return entrance_score, gpa, has_recommendation, category, extracurricular_score


def validate_inputs(entrance_score, gpa, has_recommendation, category, extracurricular_score):
    """Validate all inputs."""
    if not (0 <= entrance_score <= 100):
        print("Entrance score must be between 0 and 100.")
        return False

    if not (0 <= gpa <= 10):
        print("GPA must be between 0 and 10.")
        return False

    if has_recommendation not in ("yes", "no"):
        print("Recommendation must be 'yes' or 'no'.")
        return False

    if category not in ("general", "obc", "sc_st"):
        print("Category must be general, obc, or sc_st.")
        return False

    if not (0 <= extracurricular_score <= 10):
        print("Extracurricular score must be between 0 and 10.")
        return False

    return True


def calculate_bonus(entrance_score, has_recommendation, extracurricular_score):
    """Calculate bonus and effective score."""
    bonus = 0
    bonus_details = []

    if has_recommendation == "yes":
        bonus += 5
        bonus_details.append("+5 (recommendation)")

    if extracurricular_score > 8:
        bonus += 3
        bonus_details.append("+3 (extracurricular)")

    effective_score = entrance_score + bonus

    return effective_score, bonus_details


def make_decision(entrance_score, effective_score, gpa, category):
    """Return final admission decision."""
    
    # Auto Scholarship
    if entrance_score >= 95:
        return "ADMITTED (Scholarship)", "Entrance score ≥ 95 — Auto-admit with full scholarship."
    
    cutoffs = {"general": 75, "obc": 65, "sc_st": 55}
    min_score = cutoffs[category]
    min_gpa = 7.0

    score_ok = effective_score >= min_score
    gpa_ok = gpa >= min_gpa

    if score_ok and gpa_ok:
        return "ADMITTED (Regular)", f"Meets {category.upper()} cutoff and GPA requirement."
    
    elif score_ok and not gpa_ok:
        return "WAITLISTED", "Score qualifies but GPA too low."
    
    elif not score_ok and gpa_ok:
        return "REJECTED", "Effective score below category cutoff."
    
    else:
        return "REJECTED", "Score below cutoff AND GPA below minimum."


def main():
    """Main controller function."""
    
    data = get_inputs()
    if data is None:
        return
    
    entrance_score, gpa, has_recommendation, category, extracurricular_score = data

    if not validate_inputs(entrance_score, gpa, has_recommendation, category, extracurricular_score):
        return

    effective_score, bonus_details = calculate_bonus(
        entrance_score, has_recommendation, extracurricular_score
    )

    decision, reason = make_decision(
        entrance_score, effective_score, gpa, category
    )

    print("\n--- RESULT ---")
    print("Bonus Applied:", " ".join(bonus_details) if bonus_details else "None")
    print("Effective Score:", effective_score)
    print("Decision:", decision)
    print("Reason:", reason)


# Run program
if __name__ == "__main__":
    main()