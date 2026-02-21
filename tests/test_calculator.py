"""Tests for the Calculator module."""

import pytest

from src.calculator import Calculator


@pytest.fixture
def calc():
    """Create a Calculator instance for testing."""
    return Calculator()


class TestAdd:
    """Tests for the add method."""

    def test_add_positive_numbers(self, calc):
        assert calc.add(2, 3) == 5

    def test_add_negative_numbers(self, calc):
        assert calc.add(-1, -1) == -2

    def test_add_mixed_numbers(self, calc):
        assert calc.add(-1, 1) == 0

    def test_add_floats(self, calc):
        assert calc.add(0.1, 0.2) == pytest.approx(0.3)

    def test_add_zero(self, calc):
        assert calc.add(5, 0) == 5


class TestSubtract:
    """Tests for the subtract method."""

    def test_subtract_positive_numbers(self, calc):
        assert calc.subtract(5, 3) == 2

    def test_subtract_negative_result(self, calc):
        assert calc.subtract(3, 5) == -2

    def test_subtract_zero(self, calc):
        assert calc.subtract(5, 0) == 5


class TestMultiply:
    """Tests for the multiply method."""

    def test_multiply_positive_numbers(self, calc):
        assert calc.multiply(3, 4) == 12

    def test_multiply_by_zero(self, calc):
        assert calc.multiply(5, 0) == 0

    def test_multiply_negative_numbers(self, calc):
        assert calc.multiply(-2, -3) == 6

    def test_multiply_mixed_sign(self, calc):
        assert calc.multiply(-2, 3) == -6


class TestDivide:
    """Tests for the divide method."""

    def test_divide_positive_numbers(self, calc):
        assert calc.divide(10, 2) == 5

    def test_divide_with_remainder(self, calc):
        assert calc.divide(7, 2) == 3.5

    def test_divide_by_zero(self, calc):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calc.divide(10, 0)

    def test_divide_negative_numbers(self, calc):
        assert calc.divide(-6, -2) == 3


class TestPower:
    """Tests for the power method."""

    def test_power_positive(self, calc):
        assert calc.power(2, 3) == 8

    def test_power_zero_exponent(self, calc):
        assert calc.power(5, 0) == 1

    def test_power_negative_exponent(self, calc):
        assert calc.power(2, -1) == 0.5


class TestModulo:
    """Tests for the modulo method."""

    def test_modulo_basic(self, calc):
        assert calc.modulo(10, 3) == 1

    def test_modulo_even_division(self, calc):
        assert calc.modulo(10, 5) == 0

    def test_modulo_by_zero(self, calc):
        with pytest.raises(ValueError, match="Cannot modulo by zero"):
            calc.modulo(10, 0)
