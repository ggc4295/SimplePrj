"""Interactive CLI calculator using ast-based safe expression evaluation."""

import ast
import operator
import sys

# Supported operators
OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}


def safe_eval(expr: str) -> float:
    """Safely evaluate a math expression using AST parsing (no eval).

    Supports: +, -, *, /, **, %, parentheses, integers and floats.

    Args:
        expr: Math expression string, e.g. "2 + 3 * (4 - 1)"

    Returns:
        Computed float result.

    Raises:
        ValueError: If the expression is invalid or uses unsupported operations.
        ZeroDivisionError: If division or modulo by zero is attempted.
    """
    try:
        tree = ast.parse(expr.strip(), mode="eval")
    except SyntaxError:
        raise ValueError(f"Invalid expression: {expr!r}")

    def _eval(node):
        if isinstance(node, ast.Expression):
            return _eval(node.body)
        elif isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return float(node.value)
        elif isinstance(node, ast.BinOp):
            op_type = type(node.op)
            if op_type not in OPERATORS:
                raise ValueError(f"Unsupported operator: {op_type.__name__}")
            left = _eval(node.left)
            right = _eval(node.right)
            if op_type in (ast.Div, ast.Mod) and right == 0:
                raise ZeroDivisionError("Division or modulo by zero")
            return OPERATORS[op_type](left, right)
        elif isinstance(node, ast.UnaryOp):
            op_type = type(node.op)
            if op_type not in OPERATORS:
                raise ValueError(f"Unsupported unary operator: {op_type.__name__}")
            return OPERATORS[op_type](_eval(node.operand))
        else:
            raise ValueError(f"Unsupported expression type: {type(node).__name__}")

    return _eval(tree)


def format_result(value: float) -> str:
    """Format result: show int if no fractional part, else show float."""
    return str(int(value)) if value == int(value) else str(value)


def run_cli():
    """Run the interactive CLI calculator."""
    print("SimplePrj Calculator — type an expression to evaluate")
    print("Supports: + - * / ** % and parentheses")
    print("Type 'help' for examples, 'quit' or 'exit' to quit.\n")

    while True:
        try:
            raw = input("calc> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBye!")
            sys.exit(0)

        if not raw:
            continue

        if raw.lower() in ("quit", "exit", "q"):
            print("Bye!")
            sys.exit(0)

        if raw.lower() == "help":
            print("  Examples:")
            print("    2 + 3           → 5")
            print("    10 / 4          → 2.5")
            print("    2 ** 8          → 256")
            print("    (3 + 4) * 2     → 14")
            print("    17 % 5          → 2")
            continue

        try:
            result = safe_eval(raw)
            print(f"  = {format_result(result)}")
        except ZeroDivisionError as e:
            print(f"  Error: {e}")
        except ValueError as e:
            print(f"  Error: {e}")


def main():
    """Entry point for the CLI."""
    run_cli()


if __name__ == "__main__":
    main()
