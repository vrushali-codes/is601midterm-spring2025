import pkgutil
import importlib
import sys
# from app.commands import CommandHandler
from app.commands import Command, CommandHandler
from app.plugins.menu import MenuCommand

class App:
    def __init__(self):
        self.command_handler = CommandHandler()

    def load_plugins(self):
        # Dynamically load all plugins in the plugins directory
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, Command):
                            # Register the command dynamically using the plugin name
                            self.command_handler.register_command(plugin_name, item())
                    except TypeError:
                        continue
        
        # Register the MenuCommand
        self.command_handler.register_command("menu", MenuCommand(self.command_handler))

    def start(self):
        self.load_plugins()
        print("Usage: <command> <num1> <num2> | eg: add 2 3")
        print("Type 'menu' to see all available commands.")
        print("Type 'exit' to exit.")
        while True:
            input_str = input(">>> ").strip()
            if input_str == 'exit':
                sys.exit()  # Explicitly call sys.exit() to raise SystemExit
            self.command_handler.execute_command(input_str)