from testing.testing import calculate_sum, calculate_quotient


def test_simple():
    assert calculate_sum(1, 2) == 3


def test_that_will_fail():
    assert calculate_quotient(6, 3) == 1
