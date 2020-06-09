# K-Nearest Neighbors Classifier
A supervised machine learning algorithm that is used to solve both classification and regression problems.

This basic classifier, built from scratch using Python, is used to classify 5x5 pixelated images and output the results. The model I have implemented classifies new data based on the L2 norm or Euclidean
distance from all available data. The algorithm is known as K nearest neighbors and is used for
classification and regression problems. Furthermore, the algorithm computes the distances from
the test data to the training data set, then sorts the distances of the test data to all of the training
data. Then it finds the K smallest neighbors or neighbors with the smallest distance available.
Among these neighbors, the algorithm determines the most common class label and classifies the
test data to be of that specific class.Also, utilizing feature embedding on the data allows us to
transform our data into a higher dimension and draw better distinctions to the features at hand.
Below is the formula for the Euclidean distance, in which q is a feature of the training data and p
is a feature of the test data.

Steps taken to avoid overfitting:
In order to prevent overfitting in our model, we can attempt to choose the best value for
K. Furthermore, if we have a large data set and choose a K that is too small, we run the risk of
overfitting the data. If we choose a large value of K for a small data set, then we end up
eliminating important distinctions in the distribution of the data. Thus, in order to choose a K that
ensures we do not overfit the data, we must tune the value to best match the distribution of the
given data. Ultimately, knowing the size of the training dataset will ensure that K is being
correctly chosen

<img width="412" alt="Screen Shot 2020-06-08 at 8 24 34 PM" src="https://user-images.githubusercontent.com/39894720/84092795-75037100-a9c6-11ea-98cc-fbf4857b45e4.png">
