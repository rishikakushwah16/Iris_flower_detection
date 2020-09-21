# Iris_flower_detection
This is conceivably the best-known example to start your itinerary of machine learning or data science. The objective is to classify the iris flower between three species (Setosa, Versicolor, or Virginica). We will be using iris flower data set or Fisher's Iris data set, it is a multivariate data set introduced by British statistician, biologist, eugenicist Robert Fisher. The data set contains 50 samples from each of the three species of Iris. This is a classification project, since variable to be anticipated are categorical. First, run pip install sklearn on your command prompt. Now import iris data set, train_test_split and KNeighbours classifier using sklearn, also import matplotlib for plotting. It will allow us to use its scatter plot functionality to plot our iris dataset. If you don't have it installed just run a pip install matplotlib command on command prompt. After that we will load our iris dataset.

Our dataset is in the form of python dictionary stores some keys like data, target key, target name, DESCR etc.
Data, the corresponding value of the key is NumPy array.  It contains the features of the given sample like sepal length, sepal width, petal length, and petal width.
Target key, value corresponding is NumPy array and this contains either 0, 1 or 2. So this is the numeric encoding of what species-particular row corresponds in the array.
Target name, each of the target name is the species which we are trying to classify.
DESCR is a description of the data set.

Now we will create four sub lists using transpose. Then we will store these sub lists and plot them to show how they are interrelated. Furthermore, we will print the names of features that will give us all the values of the feature keys.
Now we want to extract each of these components and store them in the variables. Followed by plotting the scatter plot of all the features with the help of matplotlib. We will be plotting sepal length against sepal width and see how they relate with respect to the target value and we get the generated plot corresponding to different targets. Likewise, you can plot every feature.

Now we will be using the KNN classifier that is k nearest classifier for the iris flower classification. Here we have to decide how many neighbours’ we have to consider for classification, this is the general idea of this algorithm.
So now we will be dividing our datasets into two sets one would be the training set and the other would be a testing test. We will be feeding the training dataset into the machine learning model.

Sklearn provides the facility to split the data. It takes three parameters, the data, and the target and random which will randomly split the data. Moreover, we will make use of k neighbors classifier with n_neighbor =1. Finally, we will be fitting the model with respect to our data. Now we will take an input of features from the user and store it in X_N then we will be using predictions to predict the specimen of iris to which these features relate.
Now let's see the accuracy of our model. Here we have got the accuracy of 97.36% which is quite good.
