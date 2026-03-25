import numpy as np

def r2_score(y_true, y_pred):
    ss_res = np.sum((y_true - y_pred)**2)
    ss_tot = np.sum((y_true - np.mean(y_true))**2)
    return 1 - ss_res/ss_tot if ss_tot != 0 else 0

def fit_linear_regression(x, y):
    x = np.array(x).reshape(-1,1)
    y = np.array(y)
    x_mean, y_mean = np.mean(x), np.mean(y)
    num = np.sum((x.flatten() - x_mean)*(y - y_mean))
    den = np.sum((x.flatten() - x_mean)**2)
    w1 = num/den if den != 0 else 0
    w0 = y_mean - w1*x_mean
    return w0, w1
