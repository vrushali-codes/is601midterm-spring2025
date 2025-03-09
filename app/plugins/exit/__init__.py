import logging
from app.commands import Command

class ExitCommand(Command):
    def execute(self):
        logging.info("Exiting the application.")
        print("Exiting...")
        raise SystemExit