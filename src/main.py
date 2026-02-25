"""Main entry point for SimplePrj executable."""

from calculator import Calculator
from utils import fibonacci, factorial


def main():
    """Run a simple demo of the SimplePrj functions."""
    print("=" * 40)
    print("  SimplePrj Demo")
    print("=" * 40)

    calc = Calculator()
    print("\nCalculator Demo:")
    print(f"  3 + 5      = {calc.add(3, 5)}")
    print(f"  10 - 4     = {calc.subtract(10, 4)}")
    print(f"  6 * 7      = {calc.multiply(6, 7)}")
    print(f"  20 / 4     = {calc.divide(20, 4)}")
    print(f"  2 ^ 10     = {calc.power(2, 10)}")
    print(f"  17 mod 5   = {calc.modulo(17, 5)}")

    print(f"\nFibonacci (first 10): {fibonacci(10)}")
    print(f"Factorial of 10: {factorial(10)}")

    print("\nDone.")
    input("\nPress Enter to exit...")


if __name__ == "__main__":
    main()
