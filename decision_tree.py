# -------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4200- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
# -----------------------------------------------------------*/

# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

# importing some Python libraries
from sklearn import tree
import csv

dataSets = ['contact_lens_training_1.csv',
            'contact_lens_training_2.csv', 'contact_lens_training_3.csv']

for ds in dataSets:

    dbTraining = []
    X = []
    Y = []

    # reading the training data in a csv file
    with open(ds, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i > 0:  # skipping the header
                dbTraining.append(row)

    # transform the original training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3, so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    # --> add your Python code here
    # 1 = Young, 2 = Presbyopic, 3 = Prepresbyopic
    # 1 = Myope, 2 = Hypermetrope
    # 1 = No, 2 = Yes
    # 1 = Normal, 2 = Reduced
    for instance in dbTraining:
        Xtemp = []

        if instance[0] == 'Young':
            Xtemp.append(1)
        elif instance[0] == 'Presbyopic':
            Xtemp.append(2)
        elif instance[0] == 'Prepresbyopic':
            Xtemp.append(3)

        if instance[1] == 'Myope':
            Xtemp.append(1)
        elif instance[1] == 'Hypermetrope':
            Xtemp.append(2)

        if instance[2] == 'No':
            Xtemp.append(1)
        elif instance[2] == 'Yes':
            Xtemp.append(2)

        if instance[3] == 'Normal':
            Xtemp.append(1)
        elif instance[3] == 'Reduced':
            Xtemp.append(2)

        X.append(Xtemp)

    # transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    # --> add your Python code here
    # 1 = Yes, 2 = No
        Ytemp = 0

        if instance[4] == 'Yes':
            Ytemp = 1
        elif instance[4] == 'No':
            Ytemp = 2

        Y.append(Ytemp)

    # loop your training and test tasks 10 times here
    for i in range(10):

        # fitting the decision tree to the data setting max_depth=3
        clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=3)
        clf = clf.fit(X, Y)

        # read the test data and add this data to dbTest
        # --> add your Python code here
        dbTest = []

        with open('contact_lens_test.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for i, row in enumerate(reader):
                if i > 0:  # skipping the header
                    dbTest.append(row)

        correct = 0.0
        total = 0.0
        accuracy = 1.0

        for data in dbTest:
            # transform the features of the test instances to numbers following the same strategy done during training, and then use the decision tree to make the class prediction. For instance:
            # class_predicted = clf.predict([[3, 1, 2, 1]])[0]           -> [0] is used to get an integer as the predicted class label so that you can compare it with the true label
            # --> add your Python code here
            Xtemp = []

            if data[0] == 'Young':
                Xtemp.append(1)
            elif data[0] == 'Presbyopic':
                Xtemp.append(2)
            elif data[0] == 'Prepresbyopic':
                Xtemp.append(3)

            if data[1] == 'Myope':
                Xtemp.append(1)
            elif data[1] == 'Hypermetrope':
                Xtemp.append(2)

            if data[2] == 'No':
                Xtemp.append(1)
            elif data[2] == 'Yes':
                Xtemp.append(2)

            if data[3] == 'Normal':
                Xtemp.append(1)
            elif data[3] == 'Reduced':
                Xtemp.append(2)

            #print('Xtemp: ', Xtemp)
            class_predicted = clf.predict([Xtemp])[0]

            # print('class_predicted: ', class_predicted)

            # compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
            # --> add your Python code here
            true_label = 0
            if data[4] == 'Yes':
                true_label = 1
            elif data[4] == 'No':
                true_label = 2

            # print('true_label: ', true_label)

            if true_label == class_predicted:
                correct += 1.0
            total += 1.0

            # print('correct: ', correct)
            # print('\n')
        # find the lowest accuracy of this model during the 10 runs (training and test set)
        # --> add your Python code here
        tempAccuracy = correct / total
        #print('tempAccuracy: ', tempAccuracy)
        if tempAccuracy < accuracy:
            accuracy = tempAccuracy

    # print the lowest accuracy of this model during the 10 runs (training and test set).
    # your output should be something like that:
        # final accuracy when training on contact_lens_training_1.csv: 0.2
        # final accuracy when training on contact_lens_training_2.csv: 0.3
        # final accuracy when training on contact_lens_training_3.csv: 0.4
    # --> add your Python code here
    print('final accuracy when training on ', ds,': ', accuracy, sep='')