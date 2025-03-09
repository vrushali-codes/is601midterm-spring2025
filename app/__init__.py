import os
import sys
import logging
import logging.config
import pkgutil
import importlib
import pandas as pd
from dotenv import load_dotenv
from app.commands import Command, CommandHandler
from app.plugins.menu import MenuCommand

class ShowHistoryManager:
    FILE_PATH = "calculation_history.csv"
    history_df = pd.DataFrame(columns=["Operation", "Operand1", "Operand2", "Result"])

    @classmethod
    def load_history(cls):
        """Load history from a CSV file into a Pandas DataFrame."""
        if os.path.exists(cls.FILE_PATH):
            cls.history_df = pd.read_csv(cls.FILE_PATH)
        else:
            cls.history_df = pd.DataFrame(columns=["Operation", "Operand1", "Operand2", "Result"])

    @classmethod
    def show_history(cls):
        """Display the calculation history in tabular form using Pandas."""
        cls.load_history()  # Load history to ensure it is up to date
        logging.info("Displaying calculation history.")  # Log message for showing history
        print("\nCalculation History:")
        if cls.history_df.empty:
            print("No history available.")
        else:
            print(cls.history_df)

    @classmethod
    def add_calculation(cls, operation, operand1, operand2, result):
        """Add a new calculation to the history."""
        new_entry = pd.DataFrame({
            "Operation": [operation],
            "Operand1": [operand1],
            "Operand2": [operand2],
            "Result": [result]
        })

        # Only concatenate if history_df is not empty or new_entry contains valid data
        if not new_entry.isnull().all().all() and not cls.history_df.isnull().all().all():
            cls.history_df = pd.concat([cls.history_df, new_entry], ignore_index=True)
        elif not new_entry.isnull().all().all():  # If only new_entry has valid data
            cls.history_df = new_entry

        cls.history_df.to_csv(cls.FILE_PATH, index=False)  # Save to CSV

    @classmethod
    def delete_calculation(cls, index):
        """Delete a calculation from the history by index."""
        cls.load_history()  # Load history to ensure it is up to date
        if index < 0 or index >= len(cls.history_df):
            logging.error("Invalid index for deletion: %d", index)
            print(f"Invalid index: {index}. Please provide a valid index between 0 and {len(cls.history_df) - 1}.")
            return

        deleted_row = cls.history_df.iloc[index]
        cls.history_df = cls.history_df.drop(index).reset_index(drop=True)
        cls.history_df.to_csv(cls.FILE_PATH, index=False)  # Save updated history
        logging.info("Deleted calculation at index %d: %s", index, deleted_row.to_dict())
        print(f"Deleted row at index {index}: {deleted_row.to_dict()}")

class ClearHistoryManager:
    FILE_PATH = "calculation_history.csv"

    @classmethod
    def clear_history(cls):
        """Clear the history both in memory and in the file."""
        if os.path.exists(cls.FILE_PATH):
            os.remove(cls.FILE_PATH)
            logging.info("Calculation history cleared.")  # Log message for clearing history
        else:
            logging.warning("Attempted to clear history, but no history file exists.")
        print("History cleared.")

class DeleteHistoryCommand(Command):
    """Command to delete a specific entry from the calculation history."""

    def execute(self, index):
        """Execute the delete command."""
        ShowHistoryManager.delete_calculation(index)

class App:
    def __init__(self):  # Constructor
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')
        self.command_handler = CommandHandler()
        ShowHistoryManager.load_history()  # Load history when initializing the app

    def configure_logging(self):
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging configured.")

    def load_environment_variables(self):
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded.")
        return settings

    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        return self.settings.get(env_var, None)

    def load_plugins(self):
        # Dynamically load all plugins in the plugins directory
        plugins_package = 'app.plugins'
        plugins_path = plugins_package.replace('.', '/')
        if not os.path.exists(plugins_path):
            logging.warning(f"Plugins directory '{plugins_path}' not found.")
            return
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_path]):
            if is_pkg:  # Ensure it's a package
                try:
                    plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                    self.register_plugin_commands(plugin_module, plugin_name)
                except ImportError as e:
                    logging.error(f"Error importing plugin {plugin_name}: {e}")

    def register_plugin_commands(self, plugin_module, plugin_name):
        for item_name in dir(plugin_module):
            item = getattr(plugin_module, item_name)
            try:
                if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                    self.command_handler.register_command(plugin_name, item())
                    logging.info(f"Command '{plugin_name}' from plugin '{plugin_name}' registered.")
            except TypeError:
                continue
        
        # Register the MenuCommand
        self.command_handler.register_command("menu", MenuCommand(self.command_handler))

        # Register the DeleteHistoryCommand
        self.command_handler.register_command("delete", DeleteHistoryCommand())

    def start(self):
        self.load_plugins()
        logging.info("Application started. Type 'exit' to exit.")
        print("Usage: <command> <num1> <num2> | eg: add 2 3")
        print("Type 'menu' to see all available commands.")
        print("Type 'exit' to exit.")
        print("Type 'history' to see calculation history.")
        print("Type 'clear history' to clear calculation history.")
        print("Type 'delete <index>' to delete a specific entry from history.")

        try:
            while True:  # REPL Read, Evaluate, Print, Loop
                cmd_input = input(">>> ").strip()

                # Handle commands without numbers
                if cmd_input.lower() == 'exit':
                    logging.info("Application exit.")
                    sys.exit(0)  # Use sys.exit(0) for a clean exit, indicating success.
                elif cmd_input.lower() == "menu":
                    self.command_handler.commands["menu"].execute()  # Execute the menu command
                elif cmd_input.lower() == "history":
                    ShowHistoryManager.show_history()  # Show history
                elif cmd_input.lower() == "clear history":
                    ClearHistoryManager.clear_history()  # Clear history
                elif cmd_input.lower().startswith("delete "):
                    try:
                        index = int(cmd_input.split()[1])
                        self.command_handler.commands["delete"].execute(index)  # Delete specific entry
                    except (IndexError, ValueError):
                        print("Invalid format. Please use 'delete <index>'.")
                else:
                    # Handle regular calculator operations here (add, subtract, multiply, divide)
                    try:
                        operation, operand1, operand2 = cmd_input.split()
                        operand1 = float(operand1)
                        operand2 = float(operand2)

                        if operation == "add":
                            result = operand1 + operand2
                            logging.info(f"Performed addition: {operand1} + {operand2} = {result}")
                            print(f"{operand1} + {operand2} = {result}")
                        elif operation == "subtract":
                            result = operand1 - operand2
                            logging.info(f"Performed subtraction: {operand1} - {operand2} = {result}")
                            print(f"{operand1} - {operand2} = {result}")
                        elif operation == "multiply":
                            result = operand1 * operand2
                            logging.info(f"Performed multiplication: {operand1} * {operand2} = {result}")
                            print(f"{operand1} * {operand2} = {result}")
                        elif operation == "divide":
                            if operand2 == 0:
                                raise ZeroDivisionError("Cannot divide by zero.")
                            result = operand1 / operand2
                            logging.info(f"Performed division: {operand1} / {operand2} = {result}")
                            print(f"{operand1} / {operand2} = {result}")
                        else:
                            raise ValueError(f"No such command: {operation}")  # New error handling

                        # Save to history
                        ShowHistoryManager.add_calculation(operation, operand1, operand2, result)
                    except ValueError as e:
                        logging.error(f"Invalid command format or operation. Error: {e}")
                        print(f"Invalid command format. Please try again. Error: {e}")  # Updated error message
                    except ZeroDivisionError as e:
                        logging.error(str(e))
                        print(str(e))
        except KeyboardInterrupt:
            logging.info("Application interrupted and exiting gracefully.")
            sys.exit(0)  # Assuming a KeyboardInterrupt should also result in a clean exit.
        finally:
            logging.info("Application shutdown.")

if __name__ == "__main__":
    app = App()
    app.start()