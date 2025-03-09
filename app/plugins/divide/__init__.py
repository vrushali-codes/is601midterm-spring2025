from app.commands import Command

class DivideCommand(Command):
    def execute(self, a: str, b: str):
        """Divides two numbers."""
        a = int(a)
        b = int(b)
        if b == 0:
            # Raising ZeroDivisionError as required by the test
            raise ZeroDivisionError("Error: can not do Division by zero.")
        result = a / b
        print(f"The result of {a} / {b} is {result}")