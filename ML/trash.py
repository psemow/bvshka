def moving_average(series, window):
    return series.rolling(window).mean()

def linear_trend(x, y):
    from scipy.stats import linregress
    slope, intercept, r_value, _, _ = linregress(x, y)
    return slope, intercept, r_value**2


def knapsack_01(values, weights, capacity):
    n = len(values)
    dp = [0]*(capacity+1)
    for i in range(n):
        for w in range(capacity, weights[i]-1, -1):
            dp[w] = max(dp[w], dp[w-weights[i]] + values[i])
    return dp[capacity]

import matplotlib.pyplot as plt
def scatter_with_line(x, y, line_x, line_y):
    plt.scatter(x, y, alpha=0.5)
    plt.plot(line_x, line_y, 'r-')
    plt.show()

import re
from collections import Counter
def clean_and_count(texts):
    words = []
    for t in texts:
        t = re.sub(r'[^\w\s]', ' ', t.lower())
        words.extend(t.split())
    return Counter(words).most_common(10)
