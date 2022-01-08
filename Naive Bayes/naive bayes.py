# load the iris dataset
from sklearn.datasets import load_iris
iris = load_iris()

print("\nLAB_FAT_Web_Mining_CSE 3024_PRITHISH_SAMANTA_19BCE2261\n")

# store the feature matrix (X) and response vector (y)
X = iris.data
y = iris.target
print("X features", X)
print("Y features", y)

# splitting X and y into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=1)

print("X features train", X_train)
print("Y features train", y_train)

print("X features train", X_test)
print("Y features train", y_test)

# training the model on training set
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb.fit(X_train, y_train)

# making predictions on the testing set
y_pred = gnb.predict(X_test)

# comparing actual response values (y_test) with predicted response values (y_pred)
from sklearn import metrics
print("Gaussian Naive Bayes model accuracy(in %):", metrics.accuracy_score(y_test, y_pred)*100)
