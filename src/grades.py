def grade_for(score):
    """
    Return the letter grade for a numeric score.

    Grade bands (lower bound inclusive):
        90 and above -> "A"
        75 to 89     -> "B"
        60 to 74     -> "C"
        below 60     -> "F"

    Conditions are checked from the highest band down, so each score
    lands in the first band whose lower bound it meets.

    Args:
        score: The numeric score.

    Returns:
        str: One of "A", "B", "C", "F".
    """
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    return "F"
