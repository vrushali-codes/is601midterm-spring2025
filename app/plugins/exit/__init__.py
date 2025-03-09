# app/plugins/exit/__init__.py
from app.commands import Command

class ExitCommand(Command):
    def execute(self):
        print("Exiting...")
        raise SystemExit