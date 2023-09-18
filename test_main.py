import main
import pandas as pd
def test_calculate_statistics():
    # Creating a test CSV file
    data = {'Column1': [0, 1, 0, 0], 'Column2': [3, 3, 1, 3]}
    df = pd.DataFrame(data)
    df.to_csv('test_data.csv', index=False)
    # Calling the function with the test CSV file
    result = main.calculate_statistics('test_data.csv')
    # Checking the results
    assert result['mean']['Column1'] == 0.25
    assert result['median']['Column1'] == 0
    # Cleaning up
    import os
    os.remove('test_data.csv')
test_calculate_statistics()
