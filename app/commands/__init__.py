from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self, *args):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, input_str: str):
        # Split the input into command and arguments
        parts = input_str.strip().split()
        if len(parts) == 0:
            print("No command entered.")
            return
        
        command_name = parts[0]  # First word is the command
        args = parts[1:]  # The rest are arguments

        try:
            if command_name in self.commands:
                self.commands[command_name].execute(*args)  # Pass arguments to the command
            else:
                print(f"No such command: {command_name}")
        except Exception as e:
            print(f"An error occurred: {e}")