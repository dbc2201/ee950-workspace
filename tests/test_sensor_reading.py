import sys, pytest
sys.path.insert(0, "src")

from sensor import process_sensor_reading


def test_parses_integer_string():
    """
    Given a raw sensor string "42" (integer format, no decimal point)
    When process_sensor_reading processes it
    Then the result's coerced_value should be 42 (as an int)
    """
    # Arrange
    raw_input = "42"

    # Act
    result = process_sensor_reading(raw_input)

    # Assert
    assert result["coerced_value"] == 42

def test_parses_different_integer_string():
    """
    Given a raw sensor string "100" (a different integer value)
    When process_sensor_reading processes it
    Then the result's coerced_value should be 100, not the hardcoded 42
    """
    # Arrange
    raw_input = "100"

    # Act
    result = process_sensor_reading(raw_input)

    # Assert
    assert result["coerced_value"] == 100

def test_parses_float_string():
    """
    Given a raw sensor string "3.14" (contains a decimal point)
    When process_sensor_reading processes it
    Then the result's coerced_value should be 3.14 (a float)
    """
    # Arrange
    raw_input = "3.14"

    # Act
    result = process_sensor_reading(raw_input)

    # Assert
    assert result["coerced_value"] == 3.14

def test_strips_whitespace_from_input():
    """
    Given a raw sensor string with surrounding whitespace "  -105 "
    When process_sensor_reading processes it
    Then the whitespace should be stripped and coerced_value should be -105
    """
    # Arrange
    raw_input = "  -105 "

    # Act
    result = process_sensor_reading(raw_input)  # raw, un-stripped

    # Assert
    assert result["coerced_value"] == -105

def test_empty_string_raises_value_error():
    """
    Given an empty string ""
    When process_sensor_reading processes it
    Then a ValueError should be raised
    """
    # Arrange
    raw_input = ""

    # Act + Assert
    with pytest.raises(ValueError):
        process_sensor_reading(raw_input)

def test_non_string_input_raises_type_error():
    """
    Given a non-string input, the integer 100
    When process_sensor_reading processes it
    Then a TypeError should be raised
    """
    # Arrange
    raw_input = 100

    # Act + Assert
    with pytest.raises(TypeError):
        process_sensor_reading(raw_input)
