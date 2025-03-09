# import pytest
'''test for menu'''
from app import App

def test_menu_command_output(capfd, monkeypatch):
    """Test that the menu command outputs the correct list of commands."""
    # Simulate user input of 'menu' followed by 'exit' to stop the REPL.
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()

    try:
        app.start()  # Start the application, expect it to run the commands
    except SystemExit:
        pass  # Handle SystemExit to prevent the test from failing

    # Capture the output from the menu command
    captured = capfd.readouterr()
    # Ensure the menu output lists the expected commands (e.g., 'add', 'subtract', etc.)
    assert "Available commands:" in captured.out
    assert "add" in captured.out
    assert "subtract" in captured.out
    assert "multiply" in captured.out
    assert "divide" in captured.out
    assert "menu" in captured.out  # Ensure 'menu' command itself is listed