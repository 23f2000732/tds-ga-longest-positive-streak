import pytest
from streak import longest_positive_streak

def test_empty_list_returns_zero():
    assert longest_positive_streak([]) == 0

def test_all_positive_returns_length():
    assert longest_positive_streak([1, 1, 1]) == 3

def test_multiple_streaks_longest_wins():
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_zeros_and_negatives_break_streak():
    assert longest_positive_streak([0, -1, 0, -5]) == 0
    assert longest_positive_streak([1, 2, 0, 3, 4, -1, 5, 6, 7, 8]) == 4

def test_single_positive_and_negative_values():
    assert longest_positive_streak([5]) == 1
    assert longest_positive_streak([-1]) == 0
    assert longest_positive_streak([0]) == 0

def test_interleaved_values():
    assert longest_positive_streak([1, -1, 1, -1, 1]) == 1
