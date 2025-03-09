from app.commands import Command

class SubtractCommand(Command):
    def execute(self, *args):
        if len(args) != 2:
            # Raise TypeError when there are insufficient or too many arguments
            raise TypeError("Error: 'subtract' command requires exactly 2 arguments.")

        try:
            a = int(args[0])
            b = int(args[1])
            result = a - b
            print(f"The result of {a} - {b} is {result}")
        except ValueError:
            # Raising ValueError for invalid input
            raise ValueError("Invalid input: Please provide valid integers.")