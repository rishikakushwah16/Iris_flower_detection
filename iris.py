from sklearn.datasets import load_iris  #installing packages
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

IRIS = load_iris()

print(IRIS.keys())

feature = IRIS.data.T    # creating sublists using transpose

sepal_length = feature[0] # diving sublists into feature keys
sepal_width = feature[1]
petal_length = feature[2]
petal_width = feature[3]

sepal_length_labels = IRIS.feature_names[0]  #extracting each components name with values
sepal_width_labels = IRIS.feature_names[1]   # and store them into the variables
petal_length_labels = IRIS.feature_names[2]
petal_width_labels = IRIS.feature_names[3]

plt.scatter(sepal_length, sepal_width, c= IRIS.target) #plotting sepal_length & sepal_width
plt.xlabel(sepal_length_labels)
plt.ylabel(sepal_width_labels)
plt.show()

X_train, X_test, Y_train, Y_test = train_test_split(IRIS['data'], IRIS['target'], random_state=0)


KNN = KNeighborsClassifier(n_neighbors=1)
KNN.fit(X_train, Y_train)
X_N =np.array([[4.0, 3.8, 2.0, 0.4]])

predictions = KNN.predict(X_N)

print(predictions)

print(KNN.score(X_test, Y_test))
