import pandas            as pd
import numpy             as np
import matplotlib.pyplot as pyplot
import sklearn
import pickle
from sklearn import linear_model
from matplotlib import style

data = pd.read_csv("student-mat.csv", sep=";")

data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]

predict = "G3"

x = np.array(data.drop([predict], 1))
y = np.array(data[predict])
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

best = 0
for i in range(100):

    linear = linear_model.LinearRegression()

    line = linear.fit(x_train, y_train)
    accuracy = linear.score(x_test, y_test)

    if accuracy > best:
        best = accuracy
        with open("student_Model.pickle", "wb") as f:
            pickle.dump(linear, f)

print(best)

pickle_in = open("student_Model.pickle", "rb")
linear = pickle.load(pickle_in)

predictions = linear.predict(x_test)
for x in range(len(predictions)):
    print(predictions[x], x_test[x], y_test[x])

p = "G1"
style.use("ggplot")
pyplot.scatter(data[p], data[predict])
pyplot.xlabel(p)
pyplot.ylabel(predict)
pyplot.show()
