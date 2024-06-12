# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

class DataAnalyzer:
    """
    A class to analyze financial data.
    """

    def __init__(self, data):
        """
        Initialize the DataAnalyzer with data.

        Args:
            data (DataFrame): The financial data to analyze.
        """
        self.data = data

    def calculate_statistics(self):
        """
        Calculate statistics for the financial data.

        Returns:
            dict: A dictionary containing mean, median, and standard deviation.
        """
        statistics = {
            'mean': self.data.mean(),
            'median': self.data.median(),
            'std_dev': self.data.std()
        }
        return statistics

    def plot_data(self, column_name):
        """
        Plot the specified column of data.

        Args:
            column_name (str): The name of the column to plot.
        """
        plt.figure(figsize=(10, 6))
        plt.plot(self.data[column_name], label=column_name)
        plt.title(f'{column_name} over Time')
        plt.xlabel('Time')
        plt.ylabel(column_name)
        plt.legend()
        plt.show()

# Example usage
if __name__ == "__main__":
    # Load the data from a CSV file
    data = pd.read_csv('financial_data.csv')

    # Initialize the DataAnalyzer with the loaded data
    analyzer = DataAnalyzer(data)

    # Calculate statistics
    stats = analyzer.calculate_statistics()
    print("Statistics:", stats)

    # Plot data for a specific column
    analyzer.plot_data('column_name')
