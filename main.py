import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to read the dataset
def readfile(a):
    df = pd.read_csv(a)
    return df

# Function to calculate statistics for specific columns
def calculate_statistics(file_path):
    try:
        # Reading the dataset from the CSV file
        data = pd.read_csv(file_path)

        # Selecting specific columns of interest
        selected_columns = ['danceability', 'energy', 'artist_popularity', 'loudness']
        data = data[selected_columns]

        # Calculating mean, median, and standard deviation
        mean = data.mean()
        median = data.median()
        std = data.std()
        
        return {'mean': mean, 'median': median, 'std': std}
    except Exception as e:
        return str(e)

# Function to visualize specific columns as histograms
def visualize_data(data):
    try:
        # Check if the input is a DataFrame
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Input is not a pandas DataFrame")

        # Iterate over each numeric column and create a histogram
        for col in data.columns:
            plt.figure(figsize=(8, 6))
            plt.hist(data[col], bins=20, edgecolor='k', alpha=0.7)
            plt.xlabel(col)
            plt.ylabel("Frequency")
            plt.title(f"Histogram of {col}")
            plt.grid(True)
            plt.show()
    
    except Exception as e:
        return str(e)

# Function to calculate the correlation of artist_popularity with other columns
def calculate_correlation(file_path):
    try:
        # Reading the dataset from the CSV file
        data = pd.read_csv(file_path)

        # Selecting specific columns of interest
        selected_columns = ['danceability', 'energy', 'artist_popularity', 'loudness']
        data = data[selected_columns]

        # Calculating the correlation matrix
        correlation_matrix = data.corr()

        # Extracting the correlation of 'artist_popularity' with other columns
        artist_popularity_correlation = correlation_matrix['artist_popularity']
        
        return artist_popularity_correlation
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    dataset_path = "playlist.csv"

    # Calculate statistics for specific columns
    statistics_result = calculate_statistics(dataset_path)
    print("Descriptive Statistics:")
    print(statistics_result)

    # Visualize specific columns as histograms
    data = readfile(dataset_path)
    visualize_data(data)

    # Calculate and print the correlation of artist_popularity with other columns
    correlation_result = calculate_correlation(dataset_path)
    print("\nCorrelation of artist_popularity with other columns:")
    print(correlation_result)
