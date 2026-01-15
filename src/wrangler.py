import pandas as pd
import numpy as np


class FinancialWrangler:
    """
    A wrapper class for pandas DataFrames to streamline
    financial data cleaning and analysis.
    """

    def __init__(self, filepath: str):
        try:
            self.df = pd.read_csv(filepath)
            self.filename = filepath
            print(f"Successfully loaded: {filepath}")
        except Exception as e:
            raise RuntimeError(f"Error loading file: {e}")

    def clean_currency(self, columns: list[str]):
        """
        Removes currency symbols and commas from columns
        and converts them to float.
        """
        for col in columns:
            if col in self.df.columns and self.df[col].dtype == "object":
                self.df[col] = (
                    self.df[col]
                    .replace(r"[\$,]", "", regex=True)
                    .astype(float)
                )
        return self

    def remove_outliers(self, column: str):
        """
        Removes rows where values are beyond 3 standard deviations.
        """
        if column not in self.df.columns:
            raise ValueError(f"Column '{column}' not found")

        mean = self.df[column].mean()
        std = self.df[column].std()

        self.df = self.df[
            np.abs(self.df[column] - mean) <= (3 * std)
        ]
        return self

    def get_monthly_report(self, date_col: str, value_col: str):
        """
        Groups data by month and calculates total values.
        """
        if date_col not in self.df.columns:
            raise ValueError(f"Column '{date_col}' not found")

        self.df[date_col] = pd.to_datetime(self.df[date_col])

        report = (
            self.df
            .groupby(self.df[date_col].dt.to_period("M"))[value_col]
            .sum()
        )
        return report

    def save_clean_data(self, output_path: str):
        """
        Exports the cleaned DataFrame to a CSV file.
        """
        self.df.to_csv(output_path, index=False)
        print(f"Cleaned data saved to {output_path}")
