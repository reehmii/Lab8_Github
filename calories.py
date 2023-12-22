# Example code for reading from a local CSV file:
import pandas as pd

df = pd.read_csv("calories.csv")
df.to_csv("dataset", index=False)  # Write to the "dataset" file