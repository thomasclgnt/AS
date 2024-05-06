import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load data
csv_features = "/home/mecaliff/Bureau/5A/Apprentissage/AS/acsincome_ca_features.csv"
csv_labels = "/home/mecaliff/Bureau/5A/Apprentissage/AS/acsincome_ca_labels.csv"
features = pd.read_csv(csv_features)
labels = pd.read_csv(csv_labels)

# print(features.head(50))
print(features.shape)

"""
sns.set_theme(style="ticks")
sns.pairplot(features)
plt.show()
"""
