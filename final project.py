import pandas as pd

# Load the CSV file
file_path = '/Users/carolinabarandica/Downloads/IMDB Top 250 Movies.csv'
df = pd.read_csv(file_path)

# Print the actual column names
print("Actual Column Names in CSV:", df.columns.tolist())
