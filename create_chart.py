import matplotlib.pyplot as plt
import pandas as pd

# Load data from the "dataset" file
df = pd.read_csv("dataset")

# Create the chart (replace with your specific chart code)
plt.plot(df["x"], df["y"])
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Chart Title")
plt.show()