import pandas as pd
import os

class ShowHistoryManager:
    FILE_PATH = "calculation_history.csv"

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
        cls.load_history()  # Load history before showing
        print("\nCalculation History:")
        if cls.history_df.empty:
            print("No history available.")
        else:
            print(cls.history_df)

# Ensure history is loaded on import
ShowHistoryManager.load_history()