import random
import math

# Euclidean distance between two points
def euclidean_distance(point1, point2):
    squared_distance = 0
    for i in range(len(point1)):
        squared_distance += (point1[i] - point2[i]) ** 2
    return math.sqrt(squared_distance)

# Initialize centroids randomly
def initialize_centroids(data, k):
    centroids = random.sample(data, k)
    return centroids

# Assign each data point to the closest centroid
def assign_clusters(data, centroids):
    clusters = [[] for _ in centroids]
    for point in data:
        distances = [euclidean_distance(point, centroid) for centroid in centroids]
        closest_centroid_index = distances.index(min(distances))
        clusters[closest_centroid_index].append(point)
    return clusters

# Update centroids based on the mean of the assigned points
def update_centroids(clusters):
    centroids = []
    for cluster in clusters:
        centroid = [sum(dim) / len(cluster) for dim in zip(*cluster)]
        centroids.append(centroid)
    return centroids

# K-means clustering algorithm
def k_means(data, k, max_iterations):
    centroids = initialize_centroids(data, k)

    for _ in range(max_iterations):
        clusters = assign_clusters(data, centroids)
        new_centroids = update_centroids(clusters)
        
        # Check for convergence
        if new_centroids == centroids:
            break
        
        centroids = new_centroids

    return clusters, centroids

# Example usage
data = [
    [2, 10],
    [2, 5],
    [8, 4],
    [5, 8],
    [7, 5],
    [6, 4],
    [1, 2],
    [4, 9]
]
k = 2
max_iterations = 100

clusters, centroids = k_means(data, k, max_iterations)

# Print the results
print("Clusters:")
for i, cluster in enumerate(clusters):
    print(f"Cluster {i+1}: {cluster}")
print("Centroids:")
for i, centroid in enumerate(centroids):
    print(f"Centroid {i+1}: {centroid}")