# -------------------------------------------------------------------------
# AUTHOR: Matthew Le
# FILENAME: naive_bayes.py
# SPECIFICATION: This program is trained using a training set and naive bayes method and tested with a test set. The predictions with a confidence >= 0.75 are printed.
# FOR: CS 4200- Assignment #2
# TIME SPENT: 1.5 Hours (approx)
# -----------------------------------------------------------*/

# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

# importing some Python libraries
from sklearn.naive_bayes import GaussianNB
import csv

# reading the training data
# --> add your Python code here
dbTraining = []
X = []
Y = []
with open('weather_training.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            dbTraining.append(row)

# transform the original training features to numbers and add to the 4D array X. For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
# --> add your Python code here
# 1 = Overcast, 2 = Rain, 3 = Sunny
# 1 = Cool, 2 = Hot, 3 = Mild
# 1 = High, 2 = Normal
# 1 = Strong, 2 = Weak
for day in dbTraining:
    Xtemp = []

    if day[1] == 'Sunny':
        Xtemp.append(1)
    elif day[1] == 'Overcast':
        Xtemp.append(2)
    elif day[1] == 'Rain':
        Xtemp.append(3)

    if day[2] == 'Cool':
        Xtemp.append(1)
    elif day[2] == 'Mild':
        Xtemp.append(2)
    elif day[2] == 'Hot':
        Xtemp.append(3)

    if day[3] == 'Normal':
        Xtemp.append(1)
    elif day[3] == 'High':
        Xtemp.append(2)

    if day[4] == 'Weak':
        Xtemp.append(1)
    elif day[4] == 'Strong':
        Xtemp.append(2)

    X.append(Xtemp)

# transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
# --> add your Python code here
# 1 = Yes, 2 = No
for day in dbTraining:
    if day[5] == 'Yes':
        Y.append(1)
    elif day[5] == 'No':
        Y.append(2)

# fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

# reading the data in a csv file
# --> add your Python code here
dbTest = []
X = []
Y = []
with open('weather_test.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            dbTest.append(row)

# printing the header os the solution
print("Day".ljust(15) + "Outlook".ljust(15) + "Temperature".ljust(15) +
      "Humidity".ljust(15) + "Wind".ljust(15) + "PlayTennis".ljust(15) + "Confidence".ljust(15))

# use your test samples to make probabilistic predictions.
# --> add your Python code here
# -->predicted = clf.predict_proba([[3, 1, 2, 1]])[0]
for day in dbTest:
    Xtemp = []

    if day[1] == 'Sunny':
        Xtemp.append(1)
    elif day[1] == 'Overcast':
        Xtemp.append(2)
    elif day[1] == 'Rain':
        Xtemp.append(3)

    if day[2] == 'Cool':
        Xtemp.append(1)
    elif day[2] == 'Mild':
        Xtemp.append(2)
    elif day[2] == 'Hot':
        Xtemp.append(3)

    if day[3] == 'Normal':
        Xtemp.append(1)
    elif day[3] == 'High':
        Xtemp.append(2)

    if day[4] == 'Weak':
        Xtemp.append(1)
    elif day[4] == 'Strong':
        Xtemp.append(2)

    predicted = clf.predict_proba([Xtemp])[0]
    #print(day[0], 'Predicted:', predicted)

    if (predicted[0] > predicted[1]) and (predicted[0] >= 0.75):
        print(day[0].ljust(15), day[1].ljust(15), day[2].ljust(15), day[3].ljust(15), day[4].ljust(15), 'Yes'.ljust(15), "{:.2f}".format(predicted[0]), sep="")
    elif (predicted[1] > predicted[0]) and (predicted[1] >= 0.75):
        print(day[0].ljust(15), day[1].ljust(15), day[2].ljust(15), day[3].ljust(15), day[4].ljust(15), 'No'.ljust(15), "{:.2f}".format(predicted[1]), sep="")         
