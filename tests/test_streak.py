import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_multiple_streaks():
    """Test that the longest streak is returned when multiple streaks exist."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_with_zeros_and_negatives():
    """Test that zeros and negative numbers correctly break streaks."""
    assert longest_positive_streak([1, 2, 0, 4, 5, -2, 8, 9, 10, 11]) == 4

def test_all_positive():
    """Test a list with all positive numbers."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_all_non_positive():
    """Test a list with all non-positive numbers."""
    assert longest_positive_streak([-1, -2, 0, -5]) == 0

def test_single_element_positive():
    """Test a list with a single positive number."""
    assert longest_positive_streak([10]) == 1

def test_single_element_non_positive():
    """Test a list with a single non-positive number."""
    assert longest_positive_streak([-5]) == 0
    assert longest_positive_streak([0]) == 0

def test_streaks_at_beginning_and_end():
    """Test streaks at the beginning and end of the list."""
    assert longest_positive_streak([1, 2, 3, -5, 4, 5]) == 3 # beginning is longer
    assert longest_positive_streak([1, 2, -5, 4, 5, 6]) == 3 # end is longer

def test_long_list():
    """Test with a longer list."""
    assert longest_positive_streak([1]*10 + [-1] + [1]*20 + [0] + [1]*5) == 20