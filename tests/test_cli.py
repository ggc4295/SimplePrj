"""Tests for the CLI calculator (safe_eval and format_result)."""

import pytest
from src.cli import safe_eval, format_result


class TestSafeEval:
    """Tests for safe_eval()."""

    # Basic arithmetic
    def test_addition(self):
        assert safe_eval("2 + 3") == 5.0

    def test_subtraction(self):
        assert safe_eval("10 - 4") == 6.0

    def test_multiplication(self):
        assert safe_eval("3 * 4") == 12.0

    def test_division(self):
        assert safe_eval("10 / 4") == 2.5

    def test_power(self):
        assert safe_eval("2 ** 8") == 256.0

    def test_modulo(self):
        assert safe_eval("17 % 5") == 2.0

    # Parentheses & precedence
    def test_parentheses(self):
        assert safe_eval("(3 + 4) * 2") == 14.0

    def test_nested_parentheses(self):
        assert safe_eval("((2 + 3) * (4 - 1))") == 15.0

    def test_operator_precedence(self):
        assert safe_eval("2 + 3 * 4") == 14.0

    # Unary operators
    def test_unary_minus(self):
        assert safe_eval("-5 + 10") == 5.0

    def test_unary_plus(self):
        assert safe_eval("+3") == 3.0

    # Floats
    def test_float_input(self):
        assert safe_eval("1.5 + 2.5") == 4.0

    def test_float_result(self):
        assert safe_eval("1 / 3") == pytest.approx(0.3333, rel=1e-3)

    # Error cases
    def test_divide_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            safe_eval("5 / 0")

    def test_modulo_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            safe_eval("5 % 0")

    def test_invalid_expression(self):
        with pytest.raises(ValueError):
            safe_eval("2 +* 3")

    def test_empty_expression(self):
        with pytest.raises((ValueError, SyntaxError)):
            safe_eval("")

    def test_string_rejected(self):
        with pytest.raises(ValueError):
            safe_eval("'hello'")

    def test_function_call_rejected(self):
        with pytest.raises(ValueError):
            safe_eval("__import__('os')")


class TestFormatResult:
    """Tests for format_result()."""

    def test_integer_result(self):
        assert format_result(5.0) == "5"

    def test_float_result(self):
        assert format_result(2.5) == "2.5"

    def test_negative_integer(self):
        assert format_result(-3.0) == "-3"

    def test_zero(self):
        assert format_result(0.0) == "0"
