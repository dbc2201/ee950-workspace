import sys
sys.path.insert(0, "src")

from grades import grade_for


def test_high_score_gets_a():
    """
    Given a score of 95
    When grade_for calculates the grade
    Then the result should be "A"
    """
    # Arrange
    score = 95

    # Act
    result = grade_for(score)

    # Assert
    assert result == "A"

def test_low_score_gets_f():
    """
    Given a score of 40
    When grade_for calculates the grade
    Then the result should be "F"
    """
    # Arrange
    score = 40

    # Act
    result = grade_for(score)

    # Assert
    assert result == "F"

def test_middle_score_gets_b():
    """
    Given a score of 80
    When grade_for calculates the grade
    Then the result should be "B"
    """
    # Arrange
    score = 80

    # Act
    result = grade_for(score)

    # Assert
    assert result == "B"

def test_lowest_b_score_gets_b():
    """
    Given a score of 75, the lowest score in the B range
    When grade_for calculates the grade
    Then the result should be "B"
    """
    # Arrange
    score = 75

    # Act
    result = grade_for(score)

    # Assert
    assert result == "B"

def test_lowest_c_score_gets_c():
    """
    Given a score of 60, the lowest score in the C range
    When grade_for calculates the grade
    Then the result should be "C"
    """
    # Arrange
    score = 60

    # Act
    result = grade_for(score)

    # Assert
    assert result == "C"

def test_lowest_a_score_gets_a():
    """
    Given a score of 90, the lowest score in the A range
    When grade_for calculates the grade
    Then the result should be "A"
    """
    # Arrange
    score = 90

    # Act
    result = grade_for(score)

    # Assert
    assert result == "A"
