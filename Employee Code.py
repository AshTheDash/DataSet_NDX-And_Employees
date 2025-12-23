import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("Employee.csv")


df.columns = df.columns.str.strip()


if 'PaymentTier' not in df.columns or 'Gender' not in df.columns:
    raise ValueError("CSV must have 'PaymentTier' and 'Gender' columns")


male_data = df[df['Gender'].str.lower() == 'male']
female_data = df[df['Gender'].str.lower() == 'female']

plt.figure(figsize=(10, 6))
plt.scatter(male_data['Gender'], male_data['PaymentTier'], color='blue', label='Male', alpha=0.7)
plt.scatter(female_data['Gender'], female_data['PaymentTier'], color='red', label='Female', alpha=0.7)


plt.xlabel('Gender')
plt.show()
