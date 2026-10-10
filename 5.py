import pandas as pd
# Load the dataset
db = pd.read_csv(“diabetes.csv”)
# Display the first few rows
print(db.head())
print(db.info())
print(db.describe())
import matplotlib.pyplot as plt
import seaborn as sns
db.hist(bins=50,figsize=(20,15))
plt.show()
sns.pairplot(db)
plt.show()