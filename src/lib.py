"""
    Tthe following are important modules for this python file
"""
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def maximum(data, column):
    """
    Input:
        data: Dataframe to calculate maximum
        column: Target column
    Output:
        return the maximum of the Target column
    """

    max_value = data[column].max()

    return max_value


def minimum(data, column):
    """
    Input:
        data: Dataframe to calculate minimum
        column: Target column
    Output:
        return the minimum of the Target column
    """

    min_value = data[column].min()

    return min_value


def get_mean(data, column):
    """
    Input:
        data: Dataframe to calculate mean
        column: Target column
    Output:
        return the mean of the Target column
    """

    mean_value = data[column].mean()

    return mean_value


def get_median(data, column):
    """
    Input:
        data: Dataframe to calculate median
        column: Target column
    Output:
        return the median of the Target column
    """

    median_value = data[column].median()

    return median_value


def get_std_dev(data, column):
    """
    Input:
        data: Dataframe to calculate standard deviation
        column: Target column
    Output:
        return the standard deviation of the Target column
    """

    std_dev_value = data[column].std()

    return std_dev_value


def visualize_dataset(data, jupyter: bool = False):
    """Visualizes the data and their specified columns.
    Replaces NAN values for mean or median.
    Creates a heatmap of
    predictor variable correlations.
    Created a scatter plot with a line of
    best fit for each predictor
    variable. Includes legend
     with mean,median, maximum, minimum, and standard deviation"""
    # Drop the null values
    removed_NaN_data = data[["Glucose", "Insulin", "BMI"]].replace(0, np.NaN)
    removed_NaN_data["Outcome"] = data["Outcome"]
    removed_NaN_data["Glucose"].fillna(removed_NaN_data["Glucose"].mean(), inplace=True)
    removed_NaN_data["Insulin"].fillna(
        removed_NaN_data["Insulin"].median(), inplace=True
    )
    removed_NaN_data["BMI"].fillna(removed_NaN_data["BMI"].median(), inplace=True)

    # Creating a countplot based on datatype
    sns.countplot(y=data.dtypes, data=removed_NaN_data)
    plt.xlabel("data type count of diabetes predictors")
    plt.ylabel("data types of diabetes predictors")
    plt.title("Count Plot of Diabetes Predictors Data Types")
    plt.show()

    if not jupyter:
        count_visualization_path = "output/Count.png"
        plt.savefig(count_visualization_path)
        # saving to repo

    # Data for the first plot
    categories1 = removed_NaN_data["Glucose"]
    values1 = removed_NaN_data["Outcome"]

    # Data for the second plot
    categories2 = removed_NaN_data["BMI"]
    values2 = removed_NaN_data["Outcome"]

    # Data for the third plot
    categories3 = removed_NaN_data["Insulin"]
    values3 = removed_NaN_data["Outcome"]

    # Create subplots with 1 row and 3 columns
    fig, axs = plt.subplots(1, 3, figsize=(15, 5))

    # Plot 1
    axs[0].bar(categories1, values1, color="skyblue")
    axs[0].set_xlabel("Glucose(mg/dL)")
    axs[0].set_ylabel("Diabetes")
    axs[0].set_title("Glucose vs. Is Diabetic?")

    # Plot 2
    axs[1].bar(categories2, values2, color="lightgreen")
    axs[1].set_xlabel("BMI (kg/m^2)")
    axs[1].set_ylabel("Diabetes")
    axs[1].set_title("BMI vs. Is Diabetic?")

    # Plot 3
    axs[2].bar(categories3, values3, color="lightcoral")
    axs[2].set_xlabel("Insulin (mu/ml)")
    axs[2].set_ylabel("Diabetes")
    axs[2].set_title("Insulin vs. Is Diabetic?")

    # Adjust layout to prevent overlapping
    plt.tight_layout()

    # Display the plots
    plt.show()
    bar_visualization_path = "output/Barplots.png"

    if not jupyter:
        plt.savefig(bar_visualization_path)
        full_report_path = r"output/full_report.md"
        with open(full_report_path, "w", encoding="utf-8") as report:
            report.write("\n![Visualization](Barplots.png)\n")
            report.write("\n![Count_viz](Count.png)\n")


def display_statistics(data, jupyter=True):
    """displays statistics for Glucose, Insulin, and BMI
    (mean, max, min, median, std_dev).

    Parameters:
        data (pd.DataFrame): The DataFrame containing the data.
    """
    columns_of_interest = ["Glucose", "Insulin", "BMI"]
    statistics = ["Mean", "Median", "Std Dev", "Max", "Min"]

    # Create a dictionary to hold the statistics for each column
    stats_dict = {}

    for column_of_interest in columns_of_interest:
        mean_value = get_mean(data, column_of_interest)
        median_value = get_median(data, column_of_interest)
        std_dev_value = get_std_dev(data, column_of_interest)
        max_value = maximum(data, column_of_interest)
        min_value = minimum(data, column_of_interest)

        stats_dict[column_of_interest] = [
            mean_value,
            median_value,
            std_dev_value,
            max_value,
            min_value,
        ]

    # Create a DataFrame from the dictionary
    stats_df = pd.DataFrame(stats_dict, index=statistics)

    # Set the display width to make the table visually larger
    pd.set_option("display.width", 1000)

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.axis("off")
    table = ax.table(
        cellText=stats_df.values,
        colLabels=stats_df.columns,
        cellLoc="center",
        loc="center",
    )
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1, 1.5)
    plt.show()
    plt.close()
    # stats_df.plot()
    # table_visualization_path = "output/Table_Stats.png"

    if jupyter:
        print("Visualization of Diabetes Dataset")

    if not jupyter:
        print("Visualizing the Diabetes Dataset")
    #     plt.savefig(table_visualization_path)
    #     full_report_path = r"output/full_report.md"
    #     with open(full_report_path, "w", encoding="utf-8") as report:
    #         report.write("\n![Visualization](Table_Stats.png)\n")


if __name__ == "__main__":
    column = "Glucose"
    data = pd.read_csv("data/diabetes.csv")
    print("Maximum Value: ", maximum(data, column))
    print("Minimum Value: ", minimum(data, column))
    print("Mean: ", get_mean(data, column))
    print("Median: ", get_median(data, column))
    print("Standard Deviation: ", get_std_dev(data, column))

    visualize_dataset(data, jupyter=False)
