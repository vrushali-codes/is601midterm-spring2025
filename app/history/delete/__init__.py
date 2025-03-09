import os
import pandas as pd
import logging

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
    def delete_calculation(cls, index):
        """Delete a calculation from the history by index."""
        cls.load_history()  # Load history to ensure it is up to date
        if index < 0 or index >= len(cls.history_df):
            logging.error("Invalid index for deletion: %d", index)
            return f"Invalid index: {index}. Please provide a valid index between 0 and {len(cls.history_df) - 1}."

        deleted_row = cls.history_df.iloc[index]
        cls.history_df = cls.history_df.drop(index).reset_index(drop=True)
        cls.history_df.to_csv(cls.FILE_PATH, index=False)  # Save updated history
        logging.info("Deleted calculation at index %d: %s", index, deleted_row.to_dict())
        return f"Deleted row at index {index}: {deleted_row.to_dict()}"


class DeleteHistoryCommand:
    """Command to delete a specific entry from the calculation history."""

    def execute(self, index):
        """Execute the delete command."""
        return ShowHistoryManager.delete_calculation(index)