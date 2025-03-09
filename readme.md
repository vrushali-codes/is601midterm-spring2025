# Advanced Python Calculator

## Demonstration

A video demonstration of the calculator, showcasing its key features, is available [here](#). *(Link to project video)*

## Project Overview

This project is an advanced Python-based calculator application developed as part of my Software Engineering Graduate Course midterm. The calculator offers a comprehensive command-line interface (REPL) for real-time user interaction, utilizing clean and maintainable code, design patterns, professional logging, dynamic configuration via environment variables, and data handling with Pandas for managing calculation history. The project integrates various professional software development practices, such as:

- **REPL Interface**: Supports basic arithmetic operations, calculation history management, and extended functionalities via dynamically loaded plugins.
- **Plugin System**: Implements a flexible plugin architecture to allow the seamless integration of new features without modifying the core application code.
- **Calculation History Management**: Utilizes Pandas for loading, saving, clearing, and deleting calculation history.
- **Design Patterns**: Facade, Command, Factory Method, Singleton, and Strategy patterns to ensure scalable and maintainable architecture.
- **Professional Logging**: Configurable logging levels and output destinations via environment variables, following professional practices.
- **Testing and Code Quality**: Achieved over 90% code coverage with Pytest, while adhering to PEP 8 standards as verified by Pylint.
- **Version Control**: Commits are logically grouped to showcase feature development and corresponding tests, following best practices in version control.
 

## Key Design Patterns Used

- **Facade Pattern**: Simplifies interaction with complex Pandas operations for history management.
- **Command Pattern**: Organizes REPL commands for efficient operation and history management.
- **Factory Method, Singleton, and Strategy Patterns**: Enhance flexibility and scalability of the application.

## Environment Variables and Logging

This project uses environment variables to configure logging settings such as log levels and output destinations. The logging system records all key operations and errors, ensuring comprehensive monitoring of the application.

## Exception Handling: LBYL and EAFP

The project follows both "Look Before You Leap" (LBYL) and "Easier to Ask for Forgiveness than Permission" (EAFP) approaches in exception handling. This ensures robust error handling while maintaining clean and efficient code.

## Testing and Code Coverage

The project achieves over 90% test coverage using Pytest, with all tests running successfully via GitHub Actions. PEP 8 compliance is enforced and verified by Pylint.