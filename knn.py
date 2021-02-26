#-------------------------------------------------------------------------
# AUTHOR: Matthew Le
# FILENAME: knn.py
# SPECIFICATION: This program uses 1KNN to predict the value of each instance.
# FOR: CS 4200- Assignment #2
# TIME SPENT: 1 Hour (approx)
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn.neighbors import KNeighborsClassifier
import csv

db = []

#reading the data in a csv file
with open('binary_points.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)

incorrect = 0.0
total = 0.0

#loop your data to allow each instance to be your test set
for i, instance in enumerate(db):

    #add the training features to the 2D array X removing the instance that will be used for testing in this iteration. For instance, X = [[1, 3], [2, 1,], ...]]
    #--> add your Python code here
    X = []
    for j, instance in enumerate(db):
        Xtemp = []
        if i != j:
            Xtemp.append(instance[0])
            Xtemp.append(instance[1])
            X.append(Xtemp)

    #transform the original training classes to numbers and add to the vector Y removing the instance that will be used for testing in this iteration. For instance, Y = [1, 2, ,...]
    #--> add your Python code here
    Y = []
    for j, instance in enumerate(db):
        if i != j:
            if instance[2] == '-':
                Y.append(1)
            elif instance[2] == '+':
                Y.append(2)

    #store the test sample of this iteration in the vector testSample
    #--> add your Python code here
    testSample = []
    for j, instance in enumerate(db):
            if i == j:
                testSample.append(instance[0])
                testSample.append(instance[1])

    #fitting the knn to the data
    clf = KNeighborsClassifier(n_neighbors=1, p=2)
    clf = clf.fit(X, Y)

    #use your test sample in this iteration to make the class prediction. For instance:
    #class_predicted = clf.predict([[1, 2]])[0]
    #--> add your Python code here
    testClass = 0
    for j, instance in enumerate(db):
            if i == j:
                if instance[2] == '-':
                    testClass = 1
                elif instance[2] == '+':
                    testClass = 2

    class_predicted = clf.predict([testSample])[0]

    #compare the prediction with the true label of the test instance to start calculating the error rate.
    #--> add your Python code here

    if class_predicted != testClass:
        incorrect += 1
    total += 1

#print the error rate
#--> add your Python code here
error_rate = (incorrect / total) * 100
print('\nError Rate: ', error_rate, '%', sep='')





