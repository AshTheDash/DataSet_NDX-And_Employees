import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")  # or full path
df["DateTime"] = pd.to_datetime(df["DateTime"])
df = df.sort_values("DateTime")

# Close Price chart
plt.figure()
plt.plot(df["DateTime"], df["Close"])
plt.xlabel("DateTime")
plt.ylabel("Close Price")
plt.title("Close Price Over Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Tick Volume chart
plt.figure()
plt.plot(df["DateTime"], df["TickVolume"])
plt.xlabel("DateTime")
plt.ylabel("Tick Volume")
plt.title("Tick Volume Over Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
# Make sure Employee.csv is in the same folder as this script
df = pd.read_csv("Employee.csv")

# Strip extra spaces in column names (common if exported from Numbers)
df.columns = df.columns.str.strip()

# Ensure PaymentTier and Gender columns exist
if 'PaymentTier' not in df.columns or 'Gender' not in df.columns:
    raise ValueError("CSV must have 'PaymentTier' and 'Gender' columns")

# Split data by gender
male_data = df[df['Gender'].str.lower() == 'male']
female_data = df[df['Gender'].str.lower() == 'female']

# Create the dot plot
plt.figure(figsize=(10, 6))
plt.scatter(male_data['Gender'], male_data['PaymentTier'], color='blue', label='Male', alpha=0.7)
plt.scatter(female_data['Gender'], female_data['PaymentTier'], color='red', label='Female', alpha=0.7)

# Add labels and title
plt.xlabel('Gender')








