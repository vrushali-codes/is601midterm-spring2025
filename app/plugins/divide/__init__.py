import logging
from app.commands import Command

class DivideCommand(Command):
    def execute(self, a: str, b: str):
        """Divides two numbers."""
        try:
            a = int(a)
            b = int(b)
            if b == 0:
                logging.error("Error: cannot do division by zero.")
                # Raising ZeroDivisionError as required by the test
                raise ZeroDivisionError("Error: cannot do division by zero.")
            result = a / b
            logging.info(f"The result of {a} / {b} is {result}")
            print(f"The result of {a} / {b} is {result}")
        except ValueError:
            logging.error("Invalid input: Please provide valid integers.")
            raise ValueError("Invalid input: Please provide valid integers.")