"""Tests for commands"""

import pytest
from app.plugins.add import AddCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.divide import DivideCommand
from app.plugins.menu import MenuCommand
from app.plugins.exit import ExitCommand
from app.commands import CommandHandler


@pytest.mark.parametrize("command_class, args, expected_output", [
    (AddCommand, ('2', '3'), "The result of 2 + 3 is 5\n"),
    (SubtractCommand, ('5', '3'), "The result of 5 - 3 is 2\n"),
    (MultiplyCommand, ('2', '3'), "The result of 2 * 3 is 6\n"),
    (DivideCommand, ('6', '3'), "The result of 6 / 3 is 2.0\n"),
])
def test_command_execute(command_class, args, expected_output, capfd):
    """Test the execute method of various commands."""
    command = command_class()
    command.execute(*args)
    out, _ = capfd.readouterr()
    assert out == expected_output


@pytest.mark.parametrize("command_class, args", [
    (AddCommand, ('two', 'three')),
    (SubtractCommand, ('two', 'three')),
    (MultiplyCommand, ('two', 'three')),
    (DivideCommand, ('two', 'three')),
])
def test_command_invalid_input(command_class, args, capfd):
    """Test commands with invalid input."""
    command = command_class()
    with pytest.raises(ValueError):
        command.execute(*args)


@pytest.mark.parametrize("command_class, args", [
    (AddCommand, ('2',)),
    (SubtractCommand, ('2',)),
    (MultiplyCommand, ('2',)),
    (DivideCommand, ('2',)),
])
def test_command_insufficient_arguments(command_class, args):
    """Test commands with insufficient arguments."""
    command = command_class()
    with pytest.raises(TypeError):
        command.execute(*args)


@pytest.mark.parametrize("command_class, args", [
    (AddCommand, ('1', '2', '3')),
    (SubtractCommand, ('1', '2', '3')),
    (MultiplyCommand, ('1', '2', '3')),
    (DivideCommand, ('1', '2', '3')),
])
def test_command_too_many_arguments(command_class, args):
    """Test commands with too many arguments."""
    command = command_class()
    with pytest.raises(TypeError):
        command.execute(*args)


def test_divide_by_zero(capfd):
    """Test the divide command to ensure it handles division by zero."""
    command = DivideCommand()
    with pytest.raises(ZeroDivisionError):
        command.execute('6', '0')


@pytest.mark.parametrize("command_class", [AddCommand, SubtractCommand, MultiplyCommand, DivideCommand])
def test_command_instance(command_class):
    """Test that command instances can be created."""
    command = command_class()
    assert isinstance(command, command_class)

def test_menu_command(capfd):
    """Test the menu command to ensure it lists all registered commands."""
    handler = CommandHandler()
    handler.register_command('add', AddCommand())
    handler.register_command('subtract', SubtractCommand())
    handler.register_command('multiply', MultiplyCommand())
    handler.register_command('divide', DivideCommand())
    handler.register_command('menu', MenuCommand(handler))
    command = handler.commands['menu']
    command.execute()
    out, _ = capfd.readouterr()
    assert "Available commands:" in out
    assert "- add" in out
    assert "- subtract" in out
    assert "- multiply" in out
    assert "- divide" in out
    assert "- menu" in out

def test_exit_command():
    """Test the exit command to ensure it raises SystemExit."""
    command = ExitCommand()
    with pytest.raises(SystemExit):
        command.execute()