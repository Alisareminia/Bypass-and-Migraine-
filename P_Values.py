# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZjfQxcIuGpGjPOJaIHIc6iHjEI9NvX_8
"""

import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

# Load the data
before_data = pd.read_csv('/content/before_with_bmi.csv')  # Adjust path if needed
after_data = pd.read_csv('/content/After_with_bmi.csv')  # Adjust path if needed

# List of columns to analyze
columns = ['BMI', 'Frequency', 'Severity', 'MSQ_score', 'MIDAS_score']

# Initialize a list to store results
results = []

# Perform t-tests and calculate the statistics for each column
for column in columns:
    # Check if the column exists in both datasets
    if column in before_data.columns and column in after_data.columns:
        # Calculate mean and standard deviation
        mean_before = before_data[column].mean()
        std_before = before_data[column].std()
        mean_after = after_data[column].mean()
        std_after = after_data[column].std()

        # Perform t-test
        t_stat, p_value = stats.ttest_ind(before_data[column].dropna(), after_data[column].dropna())

        # Append the results (mean, std, p-value)
        results.append({
            'Parameter': column,
            'Before Mean ± SD': f"{mean_before:.1f} ± {std_before:.1f}",
            'After Mean ± SD': f"{mean_after:.1f} ± {std_after:.1f}",
            'p-value': f"{p_value:.4f}"
        })

# Convert the results into a DataFrame
results_df = pd.DataFrame(results)

# Create a plot for the results
fig, ax = plt.subplots(figsize=(10, 6))

# Plotting bars for Before and After Means
bar_width = 0.35
index = np.arange(len(columns))

# Set up the positions of bars for Before and After
bars_before = ax.bar(index, [float(r.split(" ± ")[0]) for r in results_df['Before Mean ± SD']], bar_width, label='Before')
bars_after = ax.bar(index + bar_width, [float(r.split(" ± ")[0]) for r in results_df['After Mean ± SD']], bar_width, label='After')

# Set labels and title
ax.set_xlabel('Parameters')
ax.set_ylabel('Mean Value')
ax.set_title('Comparison of Parameters: Before vs After')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(columns)
ax.legend()

# Adding p-values on top of bars
for i in range(len(columns)):
    ax.text(index[i], bars_before[i].get_height() + 0.5, f"{results_df['p-value'][i]}", ha='center', va='bottom')

# Show plot
plt.tight_layout()
plt.show()

# Display results as table
print(results_df)