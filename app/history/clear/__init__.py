import pandas as pd
import os

class HistoryManager:
    FILE_PATH = "calculation_history.csv"

    @classmethod
    def clear_history(cls):
        """Clear the history both in memory and in the file."""
        if os.path.exists(cls.FILE_PATH):
            os.remove(cls.FILE_PATH)
        print("History cleared.")