import main  
if __name__ == "__main__":
    file_path = 'playlist.csv'  # Replace with the actual path to your dataset

    # Test calculate_statistics function
    statistics_result = main.calculate_statistics(file_path)
    print("Descriptive Statistics:")
    print(statistics_result)

    # Test visualize_data function
    data = main.readfile(file_path)
    main.visualize_data(data)

    # Test calculate_correlation function
    correlation_result = main.calculate_correlation(file_path)
    print("\nCorrelation of artist_popularity with other columns:")
    print(correlation_result)
