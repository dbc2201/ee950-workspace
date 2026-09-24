import sys, pytest
sys.path.insert(0, "src")

from buckets import bucket_index


def test_positive_value_falls_in_correct_bucket():
    """
    Given a value 25 and a bucket width 10
    When bucket_index calculates the bucket
    Then the result should be 2 (the 20-29 bucket)
    """
    # Arrange
    value = 25
    width = 10

    # Act
    result = bucket_index(value, width)

    # Assert
    assert result == 2

def test_negative_value_falls_in_negative_bucket():
    """
    Given a value -5 and a bucket width 10
    When bucket_index calculates the bucket
    Then the result should be -1 (the -10 to -1 bucket), not 0
    """
    # Arrange
    value = -5
    width = 10

    # Act
    result = bucket_index(value, width)

    # Assert
    assert result == -1

def test_zero_width_raises_value_error():
    """
    Given a value 25 and a bucket width 0
    When bucket_index calculates the bucket
    Then a ValueError should be raised (width must be positive)
    """
    # Arrange
    value = 25
    width = 0

    # Act + Assert
    with pytest.raises(ValueError):
        bucket_index(value, width)
