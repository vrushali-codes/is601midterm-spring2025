import logging
from app.commands import Command
from decimal import Decimal, InvalidOperation

class AddCommand(Command):
    def execute(self, *args):
        if len(args) != 2:
            logging.error("Error: 'add' command requires exactly 2 arguments.")
            # This will raise a TypeError when there are insufficient or too many arguments
            raise TypeError("Error: 'add' command requires exactly 2 arguments.")

        try:
            a = Decimal(args[0])
            b = Decimal(args[1])
            result = a + b
            logging.info(f"The result of {a} + {b} is {result}")
            print(f"The result of {a} + {b} is {result}")
        except InvalidOperation:
            logging.error("Invalid input: Please provide valid numbers.")
            # Raising ValueError as per test requirement
            raise ValueError("Invalid input: Please provide valid numbers.")