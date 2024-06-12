from testing.testing import calculate_diff, calculate_multiple, calculate_sum


def test_calculate_sum():
    assert calculate_sum(1, 2) == 3


def test_calculate_diff():
    assert calculate_diff(4, 2) == 2


def test_calculate_multiple():
    assert calculate_multiple(3, 4) == 12
