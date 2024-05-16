import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load data
csv_features = "./Dataset/acsincome_ca_features.csv"
csv_labels = "./Dataset/acsincome_ca_labels.csv"
features = pd.read_csv(csv_features)
labels = pd.read_csv(csv_labels)

# print(features.head(50))
print(features.shape)

# plt.figure(figsize=(20,10))
# sns.heatmap(features.isna())
# plt.show()

print(labels.value_counts())

"""
sns.set_theme(style="ticks")
sns.pairplot(features)
plt.show()
"""
