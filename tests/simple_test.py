from testing.testing import calculate_diff, calculate_sum


def test_calculate_sum():
    assert calculate_sum(1, 2) == 3


def test_calculate_diff():
    assert calculate_diff(4, 2) == 2
