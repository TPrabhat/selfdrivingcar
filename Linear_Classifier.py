import numpy as np
import csv


# Setting the random seed, feel free to change it and see different solutions.
np.random.seed(42)


def stepFunction(t):
    if t >= 0:
        return 1
    return 0


def prediction(X, W, b, y):
    output = np.empty_like(y)
    for i in range(len(y)):
        output[i] = stepFunction((np.matmul(X, W) + b)[i])
    return (output)


# TODO: Fill in the code below to implement the perceptron trick.
# The function should receive as inputs the data X, the labels y,
# the weights W (as an array), and the bias b,
# update the weights and bias W, b, according to the perceptron algorithm,
# and return W and b.
def perceptronStep(X, y, W, b, learn_rate=0.01):
    for i in range(len(y)):
        if prediction(X, W, b, y)[i] > y[i]:
            W[0] = W[0] - X[i, 0] * learn_rate
            W[1] = W[1] - X[i, 1] * learn_rate
            b = b - learn_rate
        elif prediction(X, W, b, y)[i] < y[i]:
            W[0] = W[0] + X[i, 0] * learn_rate
            W[1] = W[1] + X[i, 1] * learn_rate
            b = b + learn_rate
    return W, b


# This function runs the perceptron algorithm repeatedly on the dataset,
# and returns a few of the boundary lines obtained in the iterations,
# for plotting purposes.
# Feel free to play with the learning rate and the num_epochs,
# and see your results plotted below.
def trainPerceptronAlgorithm(X, y, learn_rate=0.01, num_epochs=75):
    x_min, x_max = min(X.T[0]), max(X.T[0])
    y_min, y_max = min(X.T[1]), max(X.T[1])
    W = np.array(np.random.rand(2, 1))
    b = np.random.rand(1)[0] + x_max
    # These are the solution lines that get plotted below.
    boundary_lines = []
    for i in range(num_epochs):
        # In each epoch, we apply the perceptron step.
        W, b = perceptronStep(X, y, W, b, learn_rate)
        boundary_lines.append((-W[0] / W[1], -b / W[1]))
    return boundary_lines


with open('data.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    X1 = np.array([])
    X2 = []
    y = []
    for row in readCSV:
        np.append(X1,row[0],0)
        X2.append(row[1])
        y.append(row[2])
    print (X1)