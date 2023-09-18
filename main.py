import pandas as pd
import matplotlib.pyplot as plt
import os  # Import the os module to manage files

# Function to calculate statistics for specific columns
def calculate_statistics(file_path):
    try:
        # Reading the dataset from the CSV file
        data = pd.read_csv(file_path)

        # Selecting specific columns of interest
        selected_columns = ['danceability', 'energy', 'artist_popularity', 'loudness']
        data = data[selected_columns]

        # Calculating mean, median
        
        mean = data.mean()
        median = data.median()

        mean = mean.round(1)
        median = median.round(1)
        
        return {'mean': mean, 'median': median}
        # return {'mean': mean.to_dict(), 'median': median.to_dict()}
    except pd.errors.EmptyDataError as e:
        return str(e)



# Function to visualize specific columns as histograms
def visualize_data(file_path, save_path=None):
    try:
        # Check if the input is a DataFrame
        data = pd.read_csv(file_path)
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Input is not a pandas DataFrame")

        # Create a directory to store the plots if save_path is provided
        if save_path:
            os.makedirs(save_path, exist_ok=True)

        # Iterate over each numeric column and create a histogram
        histogram_paths = []
        for col in data.columns:
            plt.figure(figsize=(8, 6))
            plt.hist(data[col], bins=20, edgecolor='k', alpha=0.7)
            plt.xlabel(col)
            plt.ylabel("Frequency")
            plt.title(f"Histogram of {col}")
            plt.grid(True)

            if save_path:
                histogram_path = os.path.join(save_path, f"{col}_histogram.png")
                plt.savefig(histogram_path)
                plt.close()
                histogram_paths.append(histogram_path)
            else:
                plt.show()
    
        if save_path:
            return histogram_paths
    except ValueError as e:
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
    except pd.errors.EmptyDataError as e:
        return str(e)

if __name__ == "__main__":
    dataset_path = "playlist.csv"  
    
    # Calculate statistics for specific columns
    statistics_result = calculate_statistics(dataset_path)
    print("Descriptive Statistics:")
    print(statistics_result)

    # Visualize specific columns as histograms
    visualize_data(dataset_path)

    # Calculate and print the correlation of artist_popularity with other columns
    correlation_result = calculate_correlation(dataset_path)
    print("\nCorrelation of artist_popularity with other columns:")
    print(correlation_result)
