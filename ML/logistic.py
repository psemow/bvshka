import math

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

def logistic_predict(w0, w1, w2, x1, x2, p):
    z = w0 + w1*x1 + w2*x2
    return 1 if sigmoid(z) > p else -1

def accuracy(y_true, y_pred):
    return np.mean(np.array(y_true) == np.array(y_pred))
