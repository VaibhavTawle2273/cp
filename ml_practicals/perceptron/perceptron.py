import numpy as np

class Perceptron:
    def __init__(self, num_features, learning_rate=0.01, max_epochs=100):
        self.num_features = num_features
        self.learning_rate = learning_rate
        self.max_epochs = max_epochs
        self.weights = np.random.rand(num_features)
        self.bias = np.random.rand()

    def predict(self, x):
        weighted_sum = np.dot(self.weights, x) + self.bias
        return 1 if weighted_sum >= 0 else -1

    def train(self, X, y):
        for _ in range(self.max_epochs):
            errors = 0
            for xi, target in zip(X, y):
                prediction = self.predict(xi)
                update = self.learning_rate * (target - prediction)
                self.weights += update * xi
                self.bias += update
                errors += int(update != 0.0)
            if errors == 0:
                break

# Example usage
X = np.array([[2, 3], [1, 2], [3, 5], [2, 4], [5, 1], [4, 2]])
y = np.array([1, -1, 1, -1, 1, -1])

perceptron = Perceptron(num_features=2)
perceptron.train(X, y)

# Test the trained perceptron
test_data = np.array([[3, 4], [1, 1], [4, 3]])
for xi in test_data:
    prediction = perceptron.predict(xi)
    print(f"Input: {xi}, Predicted Class: {prediction}")
