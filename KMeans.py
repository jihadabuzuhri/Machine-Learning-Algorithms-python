from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=2, random_state=0).fit(X)

kmeans.labels_

kmeans.predict([[0, 0], [12, 3]])

kmeans.cluster_centers_