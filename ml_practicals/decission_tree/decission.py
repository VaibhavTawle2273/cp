#import necessary libraries 
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Load the iris dataset
iris = load_iris()

# Split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3)

# Create a decision tree classifier and fit it to the training data
clf = DecisionTreeClassifier()
clf.fit(x_train, y_train)

# Plot the decision tree 
plt.figure(figsize=(10, 8))
plot_tree(clf, filled=True)
plt.show()

# Make predictions on the testing set and calculate accuracy
predictions = clf.predict(x_test)
accuracy = clf.score(x_test, y_test)
