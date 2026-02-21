"""Tests for the utils module."""

import pytest

from src.utils import clamp, factorial, fibonacci, is_even, is_positive


class TestIsEven:
    """Tests for is_even function."""

    def test_even_number(self):
        assert is_even(4) is True

    def test_odd_number(self):
        assert is_even(3) is False

    def test_zero(self):
        assert is_even(0) is True

    def test_negative_even(self):
        assert is_even(-2) is True

    def test_negative_odd(self):
        assert is_even(-3) is False


class TestIsPositive:
    """Tests for is_positive function."""

    def test_positive_number(self):
        assert is_positive(5) is True

    def test_negative_number(self):
        assert is_positive(-5) is False

    def test_zero(self):
        assert is_positive(0) is False


class TestFactorial:
    """Tests for factorial function."""

    def test_factorial_zero(self):
        assert factorial(0) == 1

    def test_factorial_one(self):
        assert factorial(1) == 1

    def test_factorial_five(self):
        assert factorial(5) == 120

    def test_factorial_negative(self):
        with pytest.raises(ValueError, match="not defined for negative"):
            factorial(-1)


class TestFibonacci:
    """Tests for fibonacci function."""

    def test_fibonacci_zero(self):
        assert fibonacci(0) == []

    def test_fibonacci_one(self):
        assert fibonacci(1) == [0]

    def test_fibonacci_five(self):
        assert fibonacci(5) == [0, 1, 1, 2, 3]

    def test_fibonacci_ten(self):
        assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    def test_fibonacci_negative(self):
        with pytest.raises(ValueError, match="n must be non-negative"):
            fibonacci(-1)


class TestClamp:
    """Tests for clamp function."""

    def test_clamp_within_range(self):
        assert clamp(5, 0, 10) == 5

    def test_clamp_below_min(self):
        assert clamp(-5, 0, 10) == 0

    def test_clamp_above_max(self):
        assert clamp(15, 0, 10) == 10

    def test_clamp_at_min(self):
        assert clamp(0, 0, 10) == 0

    def test_clamp_at_max(self):
        assert clamp(10, 0, 10) == 10
