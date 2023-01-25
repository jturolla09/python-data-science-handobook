import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# This function prints a correlation matrix chart
# Using the chosen correlation calculation method (pearson, spearman, ...)
# And a minimum coefficient threshold to filter the matrix (ex only correlations above 0.7)

def print_simplified_correlation_matrix(df, min_correl_coef, correl_method):
  # Calculate correlations df using method = correl_method
  corr_df = df.corr(method = correl_method)

  # Keep only correlations above min_correl_coef
  condition = (abs(corr_df) > min_correl_coef)

  # Use boolean indexing to filter the DataFrame
  filtered_corr = corr_df[condition]

  # Get upper matrix only
  filtered_corr = filtered_corr.where(np.tril(np.ones(filtered_corr.shape)).astype(bool))

  # Drop all columns that have less then 2 non null values (that means drop when it's just the self correlation = 1)
  filtered_corr.dropna(axis = 1, how = 'all', thresh = 2, inplace = True)
  # And drop all rows with no correlation anymore
  filtered_corr.dropna(how = 'all', inplace = True)

  # Increase the size of the heatmap.
  plt.figure(figsize=(16, 6))
  heatmap = sns.heatmap(filtered_corr, vmin=-1, vmax=1, annot=True)
  # Give a title to the heatmap. Pad defines the distance of the title from the top of the heatmap.
  heatmap.set_title('Correlation Heatmap', fontdict={'fontsize':12}, pad=12);
  return

 # How to use (example):
 # seg_df = pd.read_csv(fpath+fname)
 # print_simplified_correlation_matrix(seg_df, 0.4, 'spearman')