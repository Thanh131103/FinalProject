import streamlit as st
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load your dataset
data = pd.read_csv('data.csv')

# Get the column names
numeric_columns = data.select_dtypes(include=np.number).columns
# Select the column for K-means
selected_column = st.sidebar.selectbox('Select a column for K-means', numeric_columns)

# Extract the selected column as the feature
feature = data[selected_column]

# Perform K-means clustering
kmeans = KMeans(n_clusters=3)  # Specify the number of clusters
kmeans.fit(feature.values.reshape(-1, 1))

# Retrieve cluster labels
labels = kmeans.labels_

# Visualize the clustering results
st.write('Selected Column:', selected_column)
fig, ax = plt.subplots()
scatter = ax.scatter(feature, labels)
ax.set_xlabel(selected_column)
ax.set_ylabel('Cluster Label')
st.pyplot(fig)