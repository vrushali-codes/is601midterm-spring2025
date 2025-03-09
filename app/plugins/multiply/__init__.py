from app.commands import Command

class MultiplyCommand(Command):
    def execute(self, a: str, b: str):
        """Multiplies two numbers."""
        a = int(a)
        b = int(b)
        result = a * b
        print(f"The result of {a} * {b} is {result}")